import math


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)


def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


def twos_compliment(val):
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val