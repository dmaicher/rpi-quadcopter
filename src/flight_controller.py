from motor import Motor
import sys

X = 0
Y = 1

FRONT_LEFT = 0
FRONT_RIGHT = 1
BACK_RIGHT = 2
BACK_LEFT = 3

class FlightController:
    def __init__(self, filter):
        self.filter = filter
        self.desired_rotation = [0, 0]
        self.motors = [
            Motor("front_left"),
            Motor("front_right"),
            Motor("back_right"),
            Motor("back_left")
        ]

    def update(self):
        current_rotation = self.filter.get_current_rotation()

        #TODO: PID
        error_x = current_rotation[X] - self.desired_rotation[X]
        error_y = current_rotation[Y] - self.desired_rotation[Y]

        print error_x, error_y
        for m in self.motors:
            print m
        sys.stdout.write("\033[F\033[F\033[F\033[F\033[F")