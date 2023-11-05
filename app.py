from flask import Flask, render_template, request
from motors import Motors
import pyfirmata
import time
app = Flask(__name__)


@app.route('/')
def index():
    motors = Motors("/dev/cu.usbmodem2201")
    motors.set_speed(0.5)
    motors.turn_left()
    time.sleep(5)
    motors.turn_right()
    time.sleep(5)
    motors.stop()
    print(motors)

    return render_template('index.html',motors=motors)


if __name__ == '__main__':
    app.run()


