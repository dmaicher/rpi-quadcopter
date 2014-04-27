#!/usr/bin/python

import time

from gyro_acc_sensor import GyroAccSensor
from complementary_filter import ComplementaryFilter


sensor = GyroAccSensor()
sensor.start()

interval = 1.0/150.0 #sec

filter = ComplementaryFilter(interval, sensor)

while True:
    now = time.time()
    data = filter.update()
    elapsed = time.time() - now
    left = interval-elapsed
    if left > 0:
        print data.rx, data.ry
        time.sleep(left)