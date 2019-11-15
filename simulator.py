#!/usr/bin/python
class PWM:
    def __init__( self, port, hz = 100):
        self.port = port
        self.hz = hz
    def start(self, dutyCycle):
        pass
    def ChangeDutyCycle( self,dutyCycle):
        pass
    
    def stop( self ):
        pass


class GPIO:
    BOARD = "board"
    BCM = "bcm"
    OUT = "out"
    IN = "in"
    HIGH = "high"
    LOW = "low"
    actuators = []
    Warning = False
    def output( pin,value):
        pass
        #print (pin, ":", value)
    
    def setmode(mode):
        pass
        #print (mode)
    
    def setup(pin,value, initial=""):
        pass
        # print (pin, ":", value)
    
    def cleanup(self):
        for actuator in actuators:
            actuator.stop()
        pass
        # print ("clean-up")
    
    def setwarnings( b):
        pass
        # print(" Warning Set ")

    def PWM(port, Hz):
        actuator = PWM(port, Hz)
        # self.actuators.append(actuator)
        return actuator
        # print(port,Hz)

    def start(dutyCycle):
        pass 
#End