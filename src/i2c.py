import smbus

class I2C:

    def __init__(self, address, bus_number):
        self.address = address
        self.bus = smbus.SMBus(bus_number)

    def write_byte_data(self, reg, data):
        self.bus.write_byte_data(self.address, reg, data)

    def read_byte_data(self, reg):
        return self.bus.read_byte_data(self.address, reg)

    def read_block_data(self, reg, length):
        return self.bus.read_i2c_block_data(self.address, reg, length)