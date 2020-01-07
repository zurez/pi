import RPi.GPIO as GPIO
import time
gpios = {
    "X":{
        "gpio":21,
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
        "stepSize":30,
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
        try:
            GPIO_PIN = values["gpio"]
            print("[INFO] Setting up GPIO PIN "+ str(GPIO_PIN))
            GPIO.setup(GPIO_PIN, GPIO.OUT)
            temp = GPIO.PWM(GPIO_PIN,50)
            temp.start(1)
            gpios[key]["instance"] = temp
       
            gpios[key]["state"] = "running"
        except expression as identifier:
            print(iden)
            pass

        
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
    if  nextPosition > 180 or nextPosition < 0 : return False
    print("[INFO] Moving to degree "+ str(nextPosition))
    dc = (nextPosition/totalDegrees) * maxDC
    if dc < 1: dc = minDC 
    gpios[axis]["currentPosition"] = nextPosition
    print("[INFO] Passing DC Value "+ str(dc))
    gpioInstance.ChangeDutyCycle(dc)
    pass



