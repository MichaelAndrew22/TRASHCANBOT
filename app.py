from flask import Flask, render_template, request
from motors import Motors
import pyfirmata
import time
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

motors = Motors("/dev/cu.usbmodem2201")

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('my response', json)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    socketio.emit('message', message)

    if message == 'forward':
        motors.set_speed(0.5)
        motors.backward()
        print(motors)
    elif message == 'left':
        motors.set_speed(0.5)
        motors.turn_left()
        print(motors)
    elif message == 'right':
        motors.set_speed(0.5)
        motors.turn_right()
        print(motors)
    elif message == 'stop':
        motors.stop()
        print(motors)
    else:
        print('Unknown message')


if __name__ == '__main__':
    socketio.run(app, debug=True)



