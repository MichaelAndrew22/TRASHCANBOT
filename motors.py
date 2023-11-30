from gpiozero import Motor
from time import sleep

class Motors:
    def __init__(self):
        self.leftMotor = Motor("GPIO23", "GPIO24")
        self.rightMotor = Motor("GPIO5", "GPIO6")

    def forward(self):
        self.leftMotor.forward(0.6)
        self.rightMotor.backward(0.6)

    def backward(self):
        self.leftMotor.backward(0.6)
        self.rightMotor.forward(0.6)

    def turn_left(self):
        self.leftMotor.backward(0.0)
        self.rightMotor.backward(0.6)

    def turn_right(self):
        self.leftMotor.forward(0.6)
        self.rightMotor.forward(0.0)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()
