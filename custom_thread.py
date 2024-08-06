import logging
import threading
import time
import socket
import re
import sys
import uuid

import serial.tools.list_ports

from utils import exit_script

path = [
    (-99.8939869, 48.3112302),
    (-99.8939297, 48.3112274),
    (-99.8938665, 48.3112208),
    (-99.8937973, 48.3112173),
    (-99.8937304, 48.3112156),
    (-99.8936575, 48.3112153),
    (-99.8935859, 48.3112132),
    (-99.8935148, 48.3112108),
    (-99.8934365, 48.3112096),
    (-99.8933554, 48.3112079),
    (-99.8932797, 48.3112071),
    (-99.8932032, 48.3112075),
    (-99.8931273, 48.3112088),
    (-99.8930474, 48.3112101),
    (-99.8929706, 48.3112109),
    (-99.8928956, 48.3112103),
    (-99.892818, 48.3112087),
    (-99.8928091, 48.3112086),
    (-99.8928067, 48.3112908),
    (-99.8928157, 48.311291),
    (-99.8928918, 48.3112925),
    (-99.8929691, 48.3112932),
    (-99.8930493, 48.3112924),
    (-99.8931303, 48.311291),
    (-99.8932064, 48.3112897),
    (-99.8932807, 48.3112894),
    (-99.8933535, 48.3112902),
    (-99.8934327, 48.3112918),
    (-99.893512, 48.3112931),
    (-99.8935797, 48.3112954),
    (-99.8936521, 48.3112975),
    (-99.8937297, 48.3112979),
    (-99.8937926, 48.3112995),
    (-99.8938573, 48.3113028),
    (-99.893911, 48.3113086),
    (-99.893978, 48.3113122),
    (-99.8939869, 48.3112302),
]

for pi, p in enumerate(path, start=1):
    prev = path[pi - 1]
    prev_longitude = prev[0]
    prev_latitude = prev[1]
    longitude = p[0]
    latitude = p[1]
    # compute heading between 2 points
    # compute speed

hs_pairs = [
    (90.0, 10.0),
    (90.0, 10.0),
    (90.0, 10.0),
    (90.0, 10.0),
    (45.0, 10.0),
    (45.0, 10.0),
    (45.0, 10.0),
    (45.0, 10.0),
    (20.0, 10.0),
    (20.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (0.0, 10.0),
    (30.0, 10.0),
    (30.0, 10.0),
    (30.0, 10.0),
    (30.0, 10.0),
    (60.0, 10.0),
    (60.0, 10.0),
    (60.0, 10.0),
    (60.0, 10.0),
    (60.0, 10.0),
    (90.0, 10.0),
    (90.0, 10.0),
    (90.0, 10.0),
]


class NmeaSrvThread(threading.Thread):
    """
    A class that represents a thread dedicated for TCP (telnet) server-client connection.
    """

    def __init__(self, nmea_object, ip_add=None, conn=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heading = None
        self.speed = None
        self._heading_cache = 0
        self._speed_cache = 0
        self.conn = conn
        self.ip_add = ip_add
        self.nmea_object = nmea_object
        self._lock = threading.RLock()

    def set_speed(self, speed):
        with self._lock:
            self.speed = speed

    def set_heading(self, heading):
        with self._lock:
            self.heading = heading

    def run(self):
        total_pairs = len(hs_pairs)
        hs_count = 0
        while True:
            hs = hs_pairs[hs_count % total_pairs]
            self.set_heading(hs[0])
            self.set_speed(hs[1])
            hs_count += 1
            # calculate the
            timer_start = time.perf_counter()
            with self._lock:
                # Nmea object speed and heading update
                if self.heading and self.heading != self._heading_cache:
                    self.nmea_object.heading_targeted = self.heading
                    self._heading_cache = self.heading
                if self.speed and self.speed != self._speed_cache:
                    self.nmea_object.speed_targeted = self.speed
                    self._speed_cache = self.speed
                # The following commands allow the same copies of NMEA data is sent on all threads
                # Only first thread in a list can iterate over NMEA object (the same nmea output in all threads)
                thread_list = [
                    thread.name
                    for thread in threading.enumerate()
                    if thread.name.startswith("nmea_srv")
                ]
                current_thread_name = threading.current_thread().name
                if len(thread_list) > 1 and current_thread_name != thread_list[0]:
                    nmea_list = [f"{_}" for _ in self.nmea_object.nmea_sentences]
                else:
                    nmea_list = [f"{_}" for _ in next(self.nmea_object)]
                try:
                    for nmea in nmea_list:
                        self.conn.sendall(nmea.encode())
                        time.sleep(0.05)
                except (BrokenPipeError, OSError):
                    self.conn.close()
                    # print(f'\n*** Connection closed with {self.ip_add[0]}:{self.ip_add[1]} ***')
                    logging.info(
                        f"Connection closed with {self.ip_add[0]}:{self.ip_add[1]}"
                    )
                    # Close thread
                    sys.exit()
            time.sleep(1 - (time.perf_counter() - timer_start))


class NmeaSerialThread(NmeaSrvThread):
    """
    A class that represents a thread dedicated for serial connection.
    """

    def __init__(self, serial_config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serial_config = serial_config

    def run(self):
        # Open serial port.
        try:
            with serial.Serial(
                self.serial_config["port"],
                baudrate=self.serial_config["baudrate"],
                bytesize=self.serial_config["bytesize"],
                parity=self.serial_config["parity"],
                stopbits=self.serial_config["stopbits"],
                timeout=self.serial_config["timeout"],
            ) as ser:
                print(
                    f'Serial port settings: {self.serial_config["port"]} {self.serial_config["baudrate"]} '
                    f'{self.serial_config["bytesize"]}{self.serial_config["parity"]}{self.serial_config["stopbits"]}'
                )
                print("Sending NMEA data...")
                while True:
                    timer_start = time.perf_counter()
                    with self._lock:
                        # Nmea object speed and heading update
                        if self.heading and self.heading != self._heading_cache:
                            self.nmea_object.heading_targeted = self.heading
                            self._heading_cache = self.heading
                        if self.speed and self.speed != self._speed_cache:
                            self.nmea_object.speed_targeted = self.speed
                            self._speed_cache = self.speed
                        nmea_list = [f"{_}" for _ in next(self.nmea_object)]
                        for nmea in nmea_list:
                            ser.write(str.encode(nmea))
                            time.sleep(0.05)
                    time.sleep(1 - (time.perf_counter() - timer_start))
        except serial.serialutil.SerialException as error:
            # Remove error number from output [...]
            error_formatted = (
                re.sub(r"\[(.*?)\]", "", str(error))
                .strip()
                .replace("  ", " ")
                .capitalize()
            )
            logging.error(
                f"{error_formatted}. Please try 'sudo chmod a+rw {self.serial_config['port']}'"
            )
            exit_script()
