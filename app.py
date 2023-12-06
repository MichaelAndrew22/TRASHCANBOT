from flask import Flask, render_template, Response
from motors import Motors
from flask_socketio import SocketIO
import cv2
from gpiozero import Servo
from gpiozero import LED
from time import sleep
from threading import Thread

servo = Servo(25)
grn = LED(4)
grn_state = False

def rotate():
    while True:
        servo.min()
        sleep(1)
        servo.mid()
        sleep(1)
        servo.max()
        sleep(1)

t = Thread(target=rotate)
t.start()


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

motors = Motors()
speed = 0

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('motor_control')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

    message = json['data']
    message = message.lower()

    if message == 'forward':
        motors.forward()
        sleep(2)
        motors.stop()

    elif message == 'backward':
        motors.backward()
        sleep(2)
        motors.stop()

    elif message == 'left':
        motors.turn_left()
        sleep(2)
        motors.stop()

    elif message == 'right':
        motors.turn_right()
        sleep(2)
        motors.stop()

    elif message == 'stop':
        motors.stop()

    elif message == 'green':
        if grn_state:
            grn.off()
            global grn_state = False
        else:
            grn.on()
            global grn_state = True


#OPENCV PORTION

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = cv2.resize(frame, (480, 320))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':
    socketio.run(app,debug=True)







