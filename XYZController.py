import RPi.GPIO as GPIO
import time
gpios = {
    "X":{
        "gpio":12,
        "currentPosition":0,
        "stepSize":5,
        "state": "stopped",
        "total_degrees": 180,
        "maxDC":13,
        "minDC":1,
        "instance":"",
        "pause":1
    },
    "Y":{
        "gpio":13,
        "currentPosition":0,
        "stepSize":5,
        "state": "stopped",
        "total_degrees": 180,
        "maxDC":13,
        "minDC":1,
        "instance":"",
        "pause":1
    },
    "Z":{
        "gpio":26,
        "currentPosition":0,
        "stepSize":5,
        "state": "stopped",
        "total_degrees": 180,
        "maxDC":13,
        "minDC":1,
        "instance":"",
        "pause":1
    }
}
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def initializeServos():
    for key, values in gpios.items():

        GPIO_PIN = values["gpio"]
        GPIO.setup(GPIO_PIN, GPIO.OUT)
        temp = GPIO.PWM(GPIO_PIN,50)
        temp.start(1)
        gpios[key]["instance"] = temp
       
        gpios[key]["state"] = "running"
        
def moveServos(axis, direction):
    gpio = gpios[axis]
    gpioInstance = gpio["instance"]
    nextPosition = gpio["currentPosition"]
    stepSize = gpio["stepSize"]
    totalDegrees = gpio["total_degrees"]
    maxDC = gpio["maxDC"]
    minDC = gpio["minDC"]
    if direction ==  "plus":
        nextPosition += stepSize
    else :
        nextPosition -= stepSize
    
    dc = (nextPosition/totalDegrees) * maxDC
    if dc < 1: dc = minDC 
    gpios[axis]["currentPosition"] = nextPosition
    gpioInstance.ChangeDutyCycle(dc)
    pass


initializeServos()

print(gpios)

moveServos("Z","plus")
time.sleep(3)
moveServos("Z","plus")
time.sleep(3)
moveServos("Z","minus")
time.sleep(3)
moveServos("Z","plus")
time.sleep(3)
moveServos("Z","minus")