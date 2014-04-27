import math_utils
import ctypes
from i2c import I2C


class GyroAccData:
    gx = gy = gz = 0
    ax = ay = az = 0


class GyroAccSensor:

    I2C_ADDRESS = 0x68
    I2C_BUS_NR = 1

    #for sensor documentation see: http://invensense.com/mems/gyro/documents/RM-MPU-6000A.pdf
    REG_POWER_MGMT_1 = 0x6b
    REG_GYRO_CONFIG = 0x1B
    REG_GYRO_DATA = 0x43
    REG_ACC_DATA = 0x3b
    REG_ACC_CONFIG = 0x1C

    DISABLE_SLEEP = 0b00000000
    CLOCK_PLL_XGYRO = 0b00000001

    GYRO_RANGE_2000 = 0b00011000
    ACC_RANGE_16 = 0b00011000

    GYRO_SCALE = 16.4
    ACC_SCALE = 2048.0

    def __init__(self):
        self.i2c = I2C(self.I2C_ADDRESS, self.I2C_BUS_NR)
        self.data = GyroAccData()

    def start(self):
        #disable sleep mode and use gyro x as clock source
        self.i2c.write_byte_data(self.REG_POWER_MGMT_1, self.DISABLE_SLEEP | self.CLOCK_PLL_XGYRO)

        #set gyro accuracy to full range (2000 degree/s)
        self.i2c.write_byte_data(self.REG_GYRO_CONFIG, self.GYRO_RANGE_2000)

        #set acc accuracy to full range (16g)
        self.i2c.write_byte_data(self.REG_ACC_CONFIG, self.ACC_RANGE_16)

    def update(self):
        raw_gyro_data = self.i2c.read_block_data(self.REG_GYRO_DATA, 6)
        self.data.gx = ctypes.c_int16((raw_gyro_data[0] << 8) | raw_gyro_data[1]).value / self.GYRO_SCALE
        self.data.gy = ctypes.c_int16((raw_gyro_data[2] << 8) | raw_gyro_data[3]).value  / self.GYRO_SCALE
        self.data.gz = ctypes.c_int16((raw_gyro_data[4] << 8) | raw_gyro_data[5]).value  / self.GYRO_SCALE

        raw_acc_data = self.i2c.read_block_data(self.REG_ACC_DATA, 6)
        self.data.ax = ctypes.c_int16((raw_acc_data[0] << 8) | raw_acc_data[1]).value  / self.ACC_SCALE
        self.data.ay = ctypes.c_int16((raw_acc_data[2] << 8) | raw_acc_data[3]).value  / self.ACC_SCALE
        self.data.az = ctypes.c_int16((raw_acc_data[4] << 8) | raw_acc_data[5]).value  / self.ACC_SCALE

        return self.data


