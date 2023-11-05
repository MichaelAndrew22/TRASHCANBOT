from flask import Flask, render_template, request
from motors import Motors
import pyfirmata
import time
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/forward', methods=['GET'])
def forward():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.set_speed(0.5)
    motors.forward()
    print(motors)
    return render_template('index.html',motors=motors)

@app.route('/backward', methods=['GET'])
def backward():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.set_speed(0.5)
    motors.backward()
    print(motors)
    return render_template('index.html',motors=motors)

@app.route('/left', methods=['GET'])
def left():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.set_speed(0.5)
    motors.turn_left()
    print(motors)
    return render_template('index.html',motors=motors)

@app.route('/right', methods=['GET'])
def right():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.set_speed(0.5)
    motors.turn_right()
    print(motors)
    return render_template('index.html',motors=motors)

@app.route('/stop', methods=['GET'])
def stop():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.stop()
    print(motors)
    return render_template('index.html',motors=motors)

if __name__ == '__main__':
    app.run()


