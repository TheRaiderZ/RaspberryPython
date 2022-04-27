from RPi import GPIO
from time import sleep
from threading import Thread
from encoder import Encoder


# clk = 17
# dt = 18

clkRight = 17
dtRight = 18
clkLeft = 22
dtLeft = 23

leftEncoderCallback = None
rightEncoderCallback = None

leftRobinetIsOpen = False # True si le robinet de gauche s'ouvre, False si le robinet se referme
rightRobinetIsOpen = False  #True si le robinet de droite s'ouvre, false si il se ferme
nombrePushSavon = 0  
personneEstDevantRobinet = False


# threadLeft = Thread(target=startRotary,args=(22,23, 'l'))
# threadRight = Thread(target=startRotary,args=(17,18, 'r'))

leftEncoderDirection = None
rightEncoderDirection = None
rightEncoderValue = 0
leftEncoderValue = 0

def leftEncoderValueChanged(value, direction):
    leftEncoderValue = value
    leftEncoderDirection = direction
    if leftEncoderDirection == 'R':
        global leftRobinetIsOpen
        leftRobinetIsOpen = True
    elif leftEncoderDirection == 'L':
        global leftRobinetIsOpen
        leftRobinetIsOpen = False

def rightEncoderValueChanged(value, direction):
    rightEncoderValue = value
    rightEncoderDirection = direction
    if rightEncoderDirection == 'R':
        global rightRobinetIsOpen
        rightRobinetIsOpen = True
    elif rightEncoderDirection == 'L':
        global rightRobinetIsOpen
        rightRobinetIsOpen = False

try:
    GPIO.setmode(GPIO.BCM)
    while True:
        leftEncoder = Encoder(clkLeft, dtLeft, callback=leftEncoderValueChanged)
        rightEncoder = Encoder(clkRight, dtRight, callback=rightEncoderValueChanged)
        print("leftEncoderValue: ", leftEncoderValue, "leftEncoderDirection: ", leftEncoderDirection, "rightOpen: ", rightRobinetIsOpen)
        print("rightEncoderValue: ", rightEncoderValue, "rightEncoderDirection: ", rightEncoderDirection, "leftOpen: ", leftRobinetIsOpen)
    # clkLastState = GPIO.input(clk)
    
            
finally:
        GPIO.cleanup()
