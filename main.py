# import eventlet

# eventlet.monkey_patch()

from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from flask_socketio import emit
from TankController import *
from imutils.video import VideoStream
import imutils
import threading
import json
import cv2
import argparse
from imutils.video import FPS
from flask import render_template

app = Flask(__name__)
outputFrame = None

# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*')
#BootStrap

# Start Tank
motor_init()


@socketio.on('command')
def commandFunction(payload):
    
    command = payload["actionType"]
    print(command)
    if command == "moveUp":
        run(1)
    elif command == "moveDown" :
        back(1)
    elif command == "moveRight" :
        right(1)
    elif command == "moveLeft" :
        left(1)
        pass
    elif command == "stopTankMovement" :
        brake(1)
        pass
    elif command == "spinTankRight" :
        spin_right(1)
        pass
    elif command == "spinTankLeft" :
        spin_left(1)
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass
    elif command == "" :
        pass

@socketio.on('connect')
def handle_connection():
    print('Connected')
    




if __name__ == '__main__':
  
    # socketio.start_background_task(gen)
    socketio.run(app,debug=True, use_reloader=False)
    # app.run(host='0.0.0.0', port =8000, debug=False, threaded=True)

# vs.stop()