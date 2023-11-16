import pyfirmata
import time

class Motors:
    def __init__(self,address='/dev/ttyACM0'):
        self.speed = float(0)
        self.direction = 0

        self.board = pyfirmata.Arduino(address)

        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()

#motor 1
        self.board.digital[3].mode = pyfirmata.PWM
        self.board.digital[4].mode = pyfirmata.OUTPUT
        self.board.digital[5].mode = pyfirmata.OUTPUT
#motor 2
        self.board.digital[9].mode = pyfirmata.PWM
        self.board.digital[10].mode = pyfirmata.OUTPUT
        self.board.digital[11].mode = pyfirmata.OUTPUT


    def set_speed(self, speed):
        self.speed = float(speed)

        self.board.digital[3].write(speed)
        self.board.digital[9].write(speed)

    def forward(self):
        self.direction = 1

        self.board.digital[4].write(0)
        self.board.digital[5].write(1)

        self.board.digital[10].write(0)
        self.board.digital[11].write(1)

    def backward(self):
        self.direction = -1

        self.board.digital[4].write(1)
        self.board.digital[5].write(0)

        self.board.digital[10].write(1)
        self.board.digital[11].write(0)

    def turn_left(self):
        self.direction = -2

        self.board.digital[4].write(1)
        self.board.digital[5].write(0)

        self.board.digital[10].write(0)
        self.board.digital[11].write(1)

    def turn_right(self):
        self.direction = 2

        self.board.digital[4].write(0)
        self.board.digital[5].write(1)

        self.board.digital[10].write(1)
        self.board.digital[11].write(0)

    def stop(self):
        self.speed = 0
        self.direction = 0

        self.board.digital[4].write(0)
        self.board.digital[5].write(0)

        self.board.digital[10].write(0)
        self.board.digital[11].write(0)

    def accelerate(self, toSpeed):
        if (self.speed < 0.2):
            for i in range(toSpeed * 100):
                self.set_speed(self, i / 100)
                time.sleep(0.01)

    def decelerate(self, toSpeed):
        if(self.speed > 0.8):
            for i in range (toSpeed*100):
                self.set_speed(self, i / 100)
                time.sleep(0.01)

    def get_speed(self):
        return self.speed

    def get_direction(self):
        if self.direction == 0:
            print("direction: stopped")
        elif self.direction == 1:
            print("direction: forward")
        elif self.direction == -1:
            print("direction: backward")
        elif self.direction == 2:
            print("direction: right")
        elif self.direction == -2:
            print("direction: left")
        return self.direction

    def __str__(self):
        return "Motors: speed = " + str(self.speed) + ", direction = " + str(self.direction)
