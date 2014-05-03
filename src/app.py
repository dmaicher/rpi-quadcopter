#!/usr/bin/python

import time

from gyro_acc_sensor import GyroAccSensor
from complementary_filter import ComplementaryFilter
from flight_controller import FlightController


def start():

    frequency = 60.0 #Hz
    interval = 1.0/frequency #sec

    #sensor = GyroAccSensor()
    #sensor.start()
    #filter = ComplementaryFilter(interval, sensor)
    flight_controller = FlightController(0, frequency)

    #max_loop_time = 0
    #sum = 0

    for i in range(0,10000):
        now = time.time()
        flight_controller.update()
        elapsed = time.time() - now
        #max_loop_time = max(max_loop_time, elapsed)
        #sum += elapsed
        left = interval-elapsed
        if left > 0:
            time.sleep(left)

    #print max_loop_time
    #print sum/10000.0

start()