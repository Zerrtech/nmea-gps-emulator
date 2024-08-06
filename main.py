#!/usr/bin/env python3

import time
import sys
import threading
import uuid
import logging

from nmea_gps import NmeaMsg
from utils import position_input, heading_input, speed_input, serial_config_input
from custom_thread import NmeaSerialThread


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.nmea_thread = None
        self.nmea_obj = None

    def run(self):
        """
        Display the menu and respond to choices.
        """
        action = self.nmea_serial
        if action:
            # Dummy 'nav_data_dict'
            nav_data_dict = {
                'gps_speed': 10.035,
                'gps_heading': 45.0,
                'gps_altitude_amsl': 15.2,
                'position': {}
            }
            # Position, initial course and speed queries
            nav_data_dict['position'] = position_input()
            nav_data_dict['gps_heading'] = heading_input()
            nav_data_dict['gps_speed'] = speed_input()

            # Initialize NmeaMsg object
            self.nmea_obj = NmeaMsg(position=nav_data_dict['position'],
                                    altitude=nav_data_dict['gps_altitude_amsl'],
                                    speed=nav_data_dict['gps_speed'],
                                    heading=nav_data_dict['gps_heading'])
            action()

        # Changing the unit's course and speed by the user in the main thread.
        first_run = True
        # TODO: loop over lat/long points goes here
        while True:
            if not self.nmea_thread.is_alive():
                print('\n\n*** Closing the script... ***\n')
                sys.exit()

            if first_run:
                time.sleep(2)
                first_run = False

            # TODO: take lat/long pair of points and determine heading and speed
            # new_head, new_speed = heading_speed_input()
            # new_head = 90.0
            # new_speed = 10.5

            # # Get all 'nmea_srv*' telnet server threads
            # thread_list = [thread for thread in threading.enumerate() if thread.name.startswith('nmea_srv')]
            # if thread_list:
            #     for thr in thread_list:
            #         # Update speed and heading
            #         # a = time.time()
            #         thr.set_heading(new_head)
            #         thr.set_speed(new_speed)
            #         # print(time.time() - a)
            # else:
            #     # Set targeted head and speed without connected clients
            #     self.nmea_obj.heading_targeted = new_head
            #     self.nmea_obj.speed_targeted = new_speed


    def nmea_serial(self):
        """
        Runs serial which emulates NMEA server-device
        """
        # serial_port = '/dev/ttyUSB0'
        # Serial configuration query
        serial_config = serial_config_input()
        self.nmea_thread = NmeaSerialThread(name=f'nmea_srv{uuid.uuid4().hex}',
                                       daemon=True,
                                       serial_config=serial_config,
                                       nmea_object=self.nmea_obj)
        self.nmea_thread.start()

    def quit(self):
        """
        Exit script.
        """
        sys.exit(0)


if __name__ == '__main__':
    # Logging config
    log_format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt='%H:%M:%S')

    Menu().run()


