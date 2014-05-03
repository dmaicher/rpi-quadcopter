class Motor:
    MIN_TICK = 150
    MAX_TICK = 600
    DIFF_TICK = MAX_TICK - MIN_TICK

    def __init__(self, id, pwm, channel):
        self.id = id
        self.power = 0 #percent 0-100
        self.pwm = pwm
        self.channel = channel
        self.pwm_set_power()

    def change_power(self, diff):
        self.set_power(self.power + diff)

    def set_power(self, power):
        self.power = max(0, min(100, power))
        self.pwm_set_power()

    def __str__(self):
        return "motor #" + self.id + ", " + str(self.power)

    def pwm_set_power(self):
        self.pwm.setPWM(self.channel, 0, int(self.MIN_TICK + self.power/100.0 * self.DIFF_TICK))

