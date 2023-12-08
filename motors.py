from gpiozero import Motor
from time import sleep

class Motors:
    def __init__(self):
        self.leftMotor = Motor("GPIO23", "GPIO24")
        self.rightMotor = Motor("GPIO5", "GPIO6")

    def forward(self):
        self.leftMotor.forward(0.4)
        self.rightMotor.backward(0.4)

    def backward(self):
        self.leftMotor.backward(0.4)
        self.rightMotor.forward(0.4)

    def turn_left(self):
        #self.leftMotor.backward(0.0)
        self.leftMotor.forward(0.2)
        self.rightMotor.backward(0.7)

    def turn_right(self):
        self.leftMotor.forward(0.7)
        #self.rightMotor.forward(0.0)
        self.rightMotor.backward(0.2)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()

