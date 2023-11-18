HARDWARE: RASPI, ARDUINO

SOFTWARE: FLASK, OPENCV, P5.JS, SOCKETIO, & PYFIRMATA




error running pyfirmata on newest python need to replace 

len_args = len(inspect.getargspec(func)[0])

with

len_args = len(inspect.getfullargspec(func)[0])
