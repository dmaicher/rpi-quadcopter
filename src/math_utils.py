import math


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x,y,z):
    return -math.degrees(math.atan2(x, dist(y,z)))


def get_x_rotation(x,y,z):
    return math.degrees(math.atan2(y, dist(x,z)))