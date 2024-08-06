import logging
import threading
import time
import socket
import re
import sys
import uuid

import serial.tools.list_ports

from utils import exit_script


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
                # The following commands allow the same copies of NMEA data is sent on all threads
                # Only first thread in a list can iterate over NMEA object (the same nmea output in all threads)
                thread_list = [thread.name for thread in threading.enumerate() if thread.name.startswith('nmea_srv')]
                current_thread_name = threading.current_thread().name
                if len(thread_list) > 1 and current_thread_name != thread_list[0]:
                    nmea_list = [f'{_}' for _ in self.nmea_object.nmea_sentences]
                else:
                    nmea_list = [f'{_}' for _ in next(self.nmea_object)]
                try:
                    for nmea in nmea_list:
                        self.conn.sendall(nmea.encode())
                        time.sleep(0.05)
                except (BrokenPipeError, OSError):
                    self.conn.close()
                    # print(f'\n*** Connection closed with {self.ip_add[0]}:{self.ip_add[1]} ***')
                    logging.info(f'Connection closed with {self.ip_add[0]}:{self.ip_add[1]}')
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
            with serial.Serial(self.serial_config['port'], baudrate=self.serial_config['baudrate'],
                               bytesize=self.serial_config['bytesize'],
                               parity=self.serial_config['parity'],
                               stopbits=self.serial_config['stopbits'],
                               timeout=self.serial_config['timeout']) as ser:
                print(
                    f'Serial port settings: {self.serial_config["port"]} {self.serial_config["baudrate"]} '
                    f'{self.serial_config["bytesize"]}{self.serial_config["parity"]}{self.serial_config["stopbits"]}')
                print('Sending NMEA data...')
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
                        nmea_list = [f'{_}' for _ in next(self.nmea_object)]
                        for nmea in nmea_list:
                            ser.write(str.encode(nmea))
                            time.sleep(0.05)
                    time.sleep(1 - (time.perf_counter() - timer_start))
        except serial.serialutil.SerialException as error:
            # Remove error number from output [...]
            error_formatted = re.sub(r'\[(.*?)\]', '', str(error)).strip().replace('  ', ' ').capitalize()
            logging.error(f"{error_formatted}. Please try \'sudo chmod a+rw {self.serial_config['port']}\'")
            exit_script()
