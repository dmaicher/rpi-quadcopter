import math_utils


class FilteredRotation:
    rx = ry = 0


# reads data from sensor and calculates rotation based on gyro and acc data using a complem
class ComplementaryFilter:
    K = 0.98
    K1 = 1 - K

    def __init__(self, interval, sensor):
        self.interval = interval
        self.sensor = sensor

        data = self.sensor.update()

        self.gyro_offset_x = data.gx
        self.gyro_offset_y = data.gy
        self.gyro_offset_z = data.gz
        self.rotation = FilteredRotation()
        self.rotation.rx = math_utils.get_x_rotation(data.ax, data.ay, data.az)
        self.rotation.ry = math_utils.get_y_rotation(data.ax, data.ay, data.az)
        self.gyro_total_x = self.rotation.rx - self.gyro_offset_x
        self.gyro_total_y = self.rotation.ry - self.gyro_offset_y

    def update(self):
        data = self.sensor.update()

        gyro_x = data.gx - self.gyro_offset_x
        gyro_y = data.gy - self.gyro_offset_y

        gyro_x_delta = (gyro_x * self.interval)
        gyro_y_delta = (gyro_y * self.interval)

        self.gyro_total_x += gyro_x_delta
        self.gyro_total_y += gyro_y_delta

        rotation_x = math_utils.get_x_rotation(data.ax, data.ay, data.az)
        rotation_y = math_utils.get_y_rotation(data.ax, data.ay, data.az)

        self.rotation.rx = self.K * (self.rotation.rx + gyro_x_delta) + (self.K1 * rotation_x)
        self.rotation.ry = self.K * (self.rotation.ry + gyro_y_delta) + (self.K1 * rotation_y)

        return self.rotation




