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
def initializeServos():
    for key, values in gpios.items():
        GPIO_PIN = values["gpio"]
        GPIO.setup(GPIO_PIN, GPIO.OUT)
        temp = GPIO.PWM(GPIO_PIN,50)
        temp.start(1)
        gpios[key]["instance"] = temp
        
initializeServos()

print(gpios)