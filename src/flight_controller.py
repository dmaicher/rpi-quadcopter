from motor import Motor
from Adafruit_PWM_Servo_Driver import PWM
import time

X = 0
Y = 1

FRONT_LEFT = 0
FRONT_RIGHT = 1
BACK_RIGHT = 2
BACK_LEFT = 3

class FlightController:
    def __init__(self, filter, frequency):
        self.filter = filter
        self.target_rotation = [0, 0]
        pwm = PWM(0x40)
        pwm.setPWMFreq(frequency)
        self.motors = [
            Motor("front_left", pwm, 4),
            Motor("front_right", pwm, 5),
            Motor("back_right", pwm, 6),
            Motor("back_left", pwm, 7)
        ]

        #let the motor'ss/ecu's init properly
        time.sleep(3)

    def update(self):
        #current_rotation = self.filter.get_current_rotation()

        #TODO: PID
        #error_x = current_rotation[X] - self.target_rotation[X]
        #error_y = current_rotation[Y] - self.target_rotation[Y]

        #print error_x, error_y
        for m in self.motors:
            m.set_power(100)
            print m

        #sys.stdout.write("\033[F\033[F\033[F\033[F\033[F")