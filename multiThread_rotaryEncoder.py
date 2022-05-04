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

# global leftEncoderValue
# global rightEncoderValue
# global leftEncoderDirection
# global rightEncoderDirection

leftEncoderCallback = None
rightEncoderCallback = None
# global leftRobinetIsOpen
leftRobinetIsOpen = False # True si le robinet de gauche s'ouvre, False si le robinet se referme
# global rightRobinetIsOpen
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
    global leftEncoderValue
    leftEncoderValue = value
    global leftEncoderDirection
    leftEncoderDirection = direction
    global leftRobinetIsOpen
    leftRobinetIsOpen=False
    if leftEncoderDirection == 'L':
        leftRobinetIsOpen = True
    elif leftEncoderDirection == 'R':
        leftRobinetIsOpen = False

def rightEncoderValueChanged(value, direction):
    global rightEncoderValue
    rightEncoderValue = value
    global rightEncoderDirection
    rightEncoderDirection = direction
    global rightRobinetIsOpen
    rightRobinetIsOpen=False
    if rightEncoderDirection == 'R':
        rightRobinetIsOpen = True
    elif rightEncoderDirection == 'L':
        rightRobinetIsOpen = False

try:
    GPIO.setmode(GPIO.BCM)
    leftEncoder = Encoder(clkLeft, dtLeft, callback=leftEncoderValueChanged)
    rightEncoder = Encoder(clkRight, dtRight, callback=rightEncoderValueChanged)
    while True:
        print('\033c')
        print('\r'+"leftEncoderValue: ", leftEncoderValue, "leftEncoderDirection: ", leftEncoderDirection, "rightOpen: ", rightRobinetIsOpen)
        print('\r'+"rightEncoderValue: ", rightEncoderValue, "rightEncoderDirection: ", rightEncoderDirection, "leftOpen: ", leftRobinetIsOpen)
        sleep(0.05)
    # clkLastState = GPIO.input(clk)
    
            
finally:
        GPIO.cleanup()

