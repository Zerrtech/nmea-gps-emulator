import re
import sys


def emulator_option_input():
    """
    The function asks for emulator option.
    """
    while True:
        try:
            print('\n### Choose emulator option: ###')
            print('1 - NMEA Serial')
            print('2 - NMEA Telnet Server')
            print('3 - NMEA TCP or UDP Stream')
            print('### "Ctrl + c" for exit ###')
            emulator_option = input('>>> ')
            if emulator_option in ['1', '2', '3']:
                return emulator_option
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def position_input() -> dict:
    """
    The function asks for position and checks validity of entry data.
    Function returns position.
    """
    while True:
        try:
            print('\n### Enter unit position (format - 5430N 01920E): ###')
            position_data = input('>>> ')
            if position_data == '':
                # Default position
                position_dict = {
                    'latitude_value': '5430.000',
                    'latitude_direction': 'N',
                    'longitude_value': '01920.000',
                    'longitude_direction': 'E',
                }
                return position_dict
            position_regex_pattern = re.compile(r'''^(
                ([0-8]\d[0-5]\d|9000)                               # Latitude
                (N|S)
                \s?
                (([0-1][0-7]\d[0-5]\d)|(0[0-9]\d[0-5]\d)|18000)     # Longitude
                (E|W)
                )$''', re.VERBOSE)
            mo = position_regex_pattern.fullmatch(position_data)
            if mo:
                # Returns position data
                position_dict = {
                    'latitude_value': f'{float(mo.group(2)):08.3f}',
                    'latitude_direction': mo.group(3),
                    'longitude_value': f'{float(mo.group(4)):09.3f}',
                    'longitude_direction': mo.group(7),
                }
                return position_dict
            print('\nError: Wrong entry! Try again.')
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def ip_port_input(option: str) -> tuple:
    """
    The function asks for IP address and port number for connection.
    """
    while True:
        try:
            if option == 'telnet':
                print('\n### Enter Local IP address and port number [0.0.0.0:10110]: ###')
                ip_port_socket = input('>>> ')
                if ip_port_socket == '':
                    # All available interfaces and default NMEA port.
                    return ('0.0.0.0', 10110)
            elif option == 'stream':
                print('\n### Enter Remote IP address and port number [127.0.0.1:10110]: ###')
                ip_port_socket = input('>>> ')
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
            print(f'\nError: Wrong format use - 192.168.10.10:2020.')
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
            stream_proto = input('>>> ').strip().lower()
            if stream_proto == '' or stream_proto == 'tcp':
                return 'tcp'
            elif stream_proto == 'udp':
                return 'udp'
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def course_input() -> float:
    """
    The function asks for the unit's course.
    """
    while True:
        try:
            print('\n### Enter unit course - range 000-359 [090]: ###')
            course_data = input('>>> ')
            if course_data == '':
                return 90.0
            course_regex_pattern = r'(3[0-5]\d|[0-2]\d{2}|\d{1,2})'
            mo = re.fullmatch(course_regex_pattern, course_data)
            if mo:
                return float(mo.group())
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def speed_input() -> float:
    """
    The function asks for the unit's speed.
    """
    while True:
        try:
            print('\n### Enter unit speed in knots - range 0-999 [10.5]: ###')
            speed_data = input('>>> ')
            if speed_data == '':
                return 10.500
            speed_regex_pattern = r'(\d{1,3}(\.\d)?)'
            mo = re.fullmatch(speed_regex_pattern, speed_data)
            if mo:
                match = mo.group()
                if match.startswith('0') and match != '0':
                    match = match.lstrip('0')
                return float(match)
        except KeyboardInterrupt:
            print('\n*** Closing the script... ***\n')
            sys.exit()


def course_speed_input() -> tuple:
    """
    The function asks for the unit's course and speed (online).
    """
    try:
        while True:
            course_data = input('New course >>> ')
            course_regex_pattern = r'(3[0-5]\d|[0-2]\d{2}|\d{1,2})'
            mo = re.fullmatch(course_regex_pattern, course_data)
            if mo:
                course_new = float(mo.group())
                break
        while True:
            speed_data = input('New speed >>> ')
            speed_regex_pattern = r'(\d{1,3}(\.\d)?)'
            mo = re.fullmatch(speed_regex_pattern, speed_data)
            if mo:
                match = mo.group()
                if match.startswith('0') and match != '0':
                    match = match.lstrip('0')
                speed_new = float(match)
                break
        return course_new, speed_new
    except KeyboardInterrupt:
        print('\n*** Closing the script... ***\n')
        sys.exit()



