import math_utils


K = 0.98
K1 = 1 - K

X = 0
Y = 1
Z = 2

# reads data from sensor and calculates rotation based on gyro and acc data
class ComplementaryFilter:

    def __init__(self, interval, sensor):
        self.interval = interval
        self.sensor = sensor

        gyro_scaled_values = self.sensor.get_gyro_scaled_values()
        acc_scaled_values = self.sensor.get_acc_scaled_values()

        self.gyro_offset = gyro_scaled_values
        self.rotation = [
            math_utils.get_x_rotation(
                acc_scaled_values[X],
                acc_scaled_values[Y],
                acc_scaled_values[Z]
            ),
            math_utils.get_y_rotation(
                acc_scaled_values[X],
                acc_scaled_values[Y],
                acc_scaled_values[Z]
            )
        ]
        self.gyro_total_sum_x = self.rotation[X] - self.gyro_offset[X]
        self.gyro_total_sum_y = self.rotation[Y] - self.gyro_offset[Y]

    def get_current_rotation(self):
        gyro_scaled_values = self.sensor.get_gyro_scaled_values()
        acc_scaled_values = self.sensor.get_acc_scaled_values()

        gyro_delta_x = (gyro_scaled_values[X] - self.gyro_offset[X]) * self.interval
        gyro_delta_y = (gyro_scaled_values[Y] - self.gyro_offset[Y]) * self.interval

        self.gyro_total_sum_x += gyro_delta_x
        self.gyro_total_sum_y += gyro_delta_x

        rotation_new_x = math_utils.get_x_rotation(
            acc_scaled_values[X],
            acc_scaled_values[Y],
            acc_scaled_values[Z]
        )
        rotation_new_y = math_utils.get_y_rotation(
            acc_scaled_values[X],
            acc_scaled_values[Y],
            acc_scaled_values[Z]
        )

        self.rotation[X] = K * (self.rotation[X] + gyro_delta_x) + (K1 * rotation_new_x)
        self.rotation[Y] = K * (self.rotation[Y] + gyro_delta_y) + (K1 * rotation_new_y)

        return self.rotation





