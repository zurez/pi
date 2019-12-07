import eventlet
from flask import Flask, render_template, Response, request
from imutils.video import VideoStream
import cv2
import os
import math
import time
import busio
import board
import numpy as np
from scipy.interpolate import griddata
from XYZController import initializeServos, moveServos
from colour import Color
 
import adafruit_amg88xx

app = Flask(__name__)
outputFrame = None




# initialize the video stream and allow the camera sensor to
# warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0,framerate = 30).start()
print(vs)
eventlet.sleep(2.0)
print("[INFO] started...")

print("[INFO] starting thermal cam stream...")

#low range of the sensor (this will be blue on the screen)
MINTEMP = 26.
 
#high range of the sensor (this will be red on the screen)
MAXTEMP = 32.
 
#how many color values we can have
COLORDEPTH = 1024
 
os.putenv('SDL_FBDEV', '/dev/fb1')
is_i2c = False
try:
    i2c_bus = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus)
    is_i2c = True
    print(sensor)
except :
    pass

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

eventlet.sleep(2.0)

print("[Initialising Servos]")
initializeServos()
time.sleep(2)
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
 
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def genThermalFrame():
    while True:
        pixels = []
        for row in sensor.pixels:
            pixels = pixels + row
        pixels = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
        bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
        (flag, encodedImage) = cv2.imencode(".jpg", bicubic)
        if not flag: continue
        # print (encodedImage)
        dataFrame = yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    pass
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
        
@app.route('/')
def controlUnit():	
    return render_template("index.html")
        
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/thermal_feed')
def thermal_feed():
    if is_i2c == False: return "False"
    return Response(genThermalFrame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/moveServos', methods= ["POST"])
def moveServos():
    
    body = request.form
    print(body)
    axis = body["axis"] 
    direction = body["direction"]
    moveServos(axis, direction)
if __name__ == '__main__':
  

    app.run(host='0.0.0.0', port =1991, debug=False, threaded=True)

# vs.stop()
