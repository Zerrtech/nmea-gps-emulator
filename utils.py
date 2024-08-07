import re
import sys
import os
import time
import platform

import psutil
import serial.tools.list_ports


def exit_script():
    """
    The function enables to terminate the script (main thread) from the inside of child thread.
    """
    current_script_pid = os.getpid()
    current_script = psutil.Process(current_script_pid)
    print('*** Closing the script... ***\n')
    time.sleep(1)
    current_script.terminate()


def position_input() -> dict:
    """
    The function asks for position and checks validity of entry data.
    Function returns position.
    """
    # Default position
    position_dict = {
        'latitude_value': '4846.585',
        'latitude_direction': 'N',
        'longitude_value': '10140.319',
        'longitude_direction': 'W',
    }
    return position_dict



def ip_port_input(option: str) -> tuple:
    """
    The function asks for IP address and port number for connection.
    """
    while True:
        try:
            if option == 'telnet':
                print('\n### Enter Local IP address and port number [0.0.0.0:10110]: ###')
                try:
                    ip_port_socket = input('>>> ')
                except KeyboardInterrupt:
                    print('\n\n*** Closing the script... ***\n')
                    sys.exit()
                if ip_port_socket == '':
                    # All available interfaces and default NMEA port.
                    return ('0.0.0.0', 10110)
            elif option == 'stream':
                print('\n### Enter Remote IP address and port number [127.0.0.1:10110]: ###')
                try:
                    ip_port_socket = input('>>> ')
                except KeyboardInterrupt:
                    print('\n\n*** Closing the script... ***\n')
                    sys.exit()
                if ip_port_socket == '':
                    return ('127.0.0.1', 10110)
            # Regex matchs only unicast IP addr from range 0.0.0.0 - 223.255.255.255
            # and port numbers from range 1 - 65535.
            ip_port_regex_pattern = re.compile(r'''^(
                ((22[0-3]\.|2[0-1][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.)  # 1st octet
                (25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.){2}  # 2nd and 3th octet
                (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2}))            # 4th octet
                :
                ([1-9][0-9]{0,3}|[1-6][0-5]{2}[0-3][0-5])   # port number
                )$''', re.VERBOSE)
            mo = ip_port_regex_pattern.fullmatch(ip_port_socket)
            if mo:
                # return tuple with IP address (str) and port number (int).
                return (mo.group(2), int(mo.group(6)))
            print(f'\n\nError: Wrong format use - 192.168.10.10:2020.')
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def trans_proto_input() -> str:
    """
    The function asks for transport protocol for NMEA stream.
    """
    while True:
        try:
            print('\n### Enter transport protocol - TCP or UDP [TCP]: ###')
            try:
                stream_proto = input('>>> ').strip().lower()
            except KeyboardInterrupt:
                print('\n\n*** Closing the script... ***\n')
                sys.exit()
            if stream_proto == '' or stream_proto == 'tcp':
                return 'tcp'
            elif stream_proto == 'udp':
                return 'udp'
        except KeyboardInterrupt:
            print('\n\n*** Closing the script... ***\n')
            sys.exit()


def heading_input() -> float:
    """
    The function asks for the unit's course.
    """
    return 90.0



def speed_input() -> float:
    """
    The function asks for the unit's speed.
    """
    return 10.500


def heading_speed_input() -> tuple:
    """
    The function asks for the unit's heading and speed (online).
    """
    try:
        while True:
            try:
                heading_data = input('New course >>> ')
            except KeyboardInterrupt:
                print('\n\n*** Closing the script... ***\n')
                sys.exit()
            heading_regex_pattern = r'(3[0-5]\d|[0-2]\d{2}|\d{1,2})'
            mo = re.fullmatch(heading_regex_pattern, heading_data)
            if mo:
                heading_new = float(mo.group())
                break
        while True:
            try:
                speed_data = input('New speed >>> ')
            except KeyboardInterrupt:
                print('\n\n*** Closing the script... ***\n')
                sys.exit()
            speed_regex_pattern = r'(\d{1,3}(\.\d)?)'
            mo = re.fullmatch(speed_regex_pattern, speed_data)
            if mo:
                match = mo.group()
                if match.startswith('0') and match != '0':
                    match = match.lstrip('0')
                speed_new = float(match)
                break
        return heading_new, speed_new
    except KeyboardInterrupt:
        print('\n\n*** Closing the script... ***\n')
        sys.exit()


def serial_config_input() -> dict:
    """
    The function asks for serial configuration.
    """
    # serial_port = '/dev/ttyUSB0'
    # Dict with all serial port settings.
    serial_set = {'bytesize': 8,
                  'parity': 'N',
                  'stopbits': 1,
                  'timeout': 1,
                  'port': '/dev/ttyUSB0',
                  'baudrate': '115200'}

    # List of available serial ports.
    ports_connected = serial.tools.list_ports.comports(include_links=False)
    # List of available serial port's names.
    ports_connected_names = [port.device for port in ports_connected]
    print('\n### Connected Serial Ports: ###')
    for port in sorted(ports_connected):
        print(f'   - {port}')
    # Asks for serial port name and checks the name validity.

    if serial_set['port'] not in ports_connected_names:
        raise Exception("Port not found")

    return serial_set



