import eventlet

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




# initialize the video stream and allow the camera sensor to
# warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0,framerate = 30).start()
print(vs)
eventlet.sleep(2.0)
print("[INFO] started...")



    
@app.route('/')
def controlUnit():
    return render_template("index.html")

def gen():
    """Video streaming generator function."""
    global dataFrame
    while True:
        frame = vs.read()
        # frame = imutils.resize(frame, width=400)
        
        (flag, encodedImage) = cv2.imencode(".jpg", frame.copy())
        if not flag: continue
        # print (encodedImage)
        dataFrame = yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
  

    app.run(host='0.0.0.0', port =1991, debug=False, threaded=True)

# vs.stop()