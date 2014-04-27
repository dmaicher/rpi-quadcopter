class Motor:
    def __init__(self, id):
        self.id = id
        self.speed = 0 #percent 0-100

    def change_speed(self, diff):
        self.speed = max(0, min(100, self.speed + diff))

    def set_speed(self, speed):
        self.speed = max(0, min(100, speed))

    def __str__(self):
        return "motor #" + self.id + ", " + str(self.speed)