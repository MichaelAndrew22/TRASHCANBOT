from flask import Flask, render_template, Response
from motors import Motors
from flask_socketio import SocketIO
import cv2


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

    message = json['data']
    message = message.lower()

    if message == 'forward':
        motors.set_speed(0.5)
        motors.backward()
        print(motors)

    elif message == 'backward':
        motors.set_speed(0.5)
        motors.forward()
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


    socketio.emit('my response', json)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    socketio.emit('message', message)


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

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    socketio.run(app,debug=True)







