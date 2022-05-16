from RPi import GPIO
from time import sleep
from threading import Thread
from encoder import Encoder
from gpiozero import Button
from hcsr04sensor import sensor
import flask
import json
import typing
from SensorData import *


try:

    data = {
        "data":
        {
        "rotationG": -28,
        "rotationD": -12,
        "distance": 20,

        "savon": 5555,
        "temps" : 1000
        }
    }


    clkRight = 17
    dtRight = 18
    clkLeft = 22
    dtLeft = 23

    trigPin=19
    echoPin=16

    buttonGPIO = 27

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
    distance = 0
    sensorData=None


    # threadLeft = Thread(target=startRotary,args=(22,23, 'l'))
    # threadRight = Thread(target=startRotary,args=(17,18, 'r'))

    leftEncoderDirection = None
    rightEncoderDirection = None
    rightEncoderValue = 0
    leftEncoderValue = 0



    def leftEncoderValueChanged(value, direction):
        # print("rIGHT")
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
        # print("rIGHT")
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


    GPIO.setmode(GPIO.BCM)
    global buttonSavon
    buttonSavon = Button(buttonGPIO, None,True)
    global leftEncoder
    leftEncoder = Encoder(clkLeft, dtLeft, callback=leftEncoderValueChanged)
    global rightEncoder
    rightEncoder = Encoder(clkRight, dtRight, callback=rightEncoderValueChanged)
    

    def btnPress():
        if buttonSavon.is_pressed:
            global nombrePushSavon
            nombrePushSavon+=1
            sleep(0.5)
#region cassé
    # def getData():
    #     distance = sensor.Measurement(trigPin, echoPin)
    #     raw_measurement = distance.raw_distance()
    #     global leftEncoder
    #     global rightEncoder
    #     global buttonSavon
    #     print('\033c')
    #     print('\r'+"leftEncoderValue: ", leftEncoderValue, "leftEncoderDirection: ", leftEncoderDirection, "rightOpen: ", rightRobinetIsOpen)
    #     print('\r'+"rightEncoderValue: ", rightEncoderValue, "rightEncoderDirection: ", rightEncoderDirection, "leftOpen: ", leftRobinetIsOpen)
    #     print('\r'+"nombrePushSavon: ", nombrePushSavon)
    #     print('\r'+'Raw distance: ', raw_measurement)
    #     # obj = Data(rotation_d=rightEncoderValue, rotation_g=leftEncoderValue, savon=nombrePushSavon, distance=raw_measurement, temps=0).to_dict
    #     # sensorData=SensorData(obj)
    #     # print(leftEncoder.getValue())
    #     data = {
    #         "data":
    #         {
    #         "rotationG": leftEncoderValue,
    #         "rotationD": rightEncoderValue,
    #         "distance": raw_measurement,

    #         "savon": nombrePushSavon,
    #         "temps" : 0
    #         }
    #     }


    #     # print(data)
    #     # sleep(0.05)
    #     return data



    # @app.route('/getData', methods=['GET'])
    # def home():
    #     dat = getData()
    #     print(dat)
    #     return json.dumps(dat)
    #     # return json.dumps(dat)


    # buttonSavon.when_activated=btnPress
    # app.run()
#endregion
    
    GPIO.setmode(GPIO.BCM)
    buttonSavon = Button(buttonGPIO, None,True)
    leftEncoder = Encoder(clkLeft, dtLeft, callback=leftEncoderValueChanged)
    rightEncoder = Encoder(clkRight, dtRight, callback=rightEncoderValueChanged)
    
    while True:
        distance = sensor.Measurement(trigPin, echoPin)
        raw_measurement = distance.raw_distance()
        buttonSavon.when_activated
        if buttonSavon.is_pressed:
            nombrePushSavon+=1
            sleep(0.5)
        print('\033c')
        print('\r'+"leftEncoderValue: ", leftEncoderValue, "leftEncoderDirection: ", leftEncoderDirection, "rightOpen: ", rightRobinetIsOpen)
        print('\r'+"rightEncoderValue: ", rightEncoderValue, "rightEncoderDirection: ", rightEncoderDirection, "leftOpen: ", leftRobinetIsOpen)
        print('\r'+"nombrePushSavon: ", nombrePushSavon)
        print('\r'+'Raw distance: ', raw_measurement)
        # obj = Data(rotation_d=rightEncoderValue, rotation_g=leftEncoderValue, savon=nombrePushSavon, distance=raw_measurement).to_dict
        # sensorData=SensorData(obj)
        # data=sensorData.to_dict()
        print(data)
        sleep(0.05)
        data = {
            "data":
                {
                "rotationG": leftEncoderValue,
                "rotationD": rightEncoderValue,
                "distance": raw_measurement,

                "savon": nombrePushSavon,
                "temps" : 0
                }
            }
        #output data in json format, if file is not found, create it
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    # clkLastState = GPIO.input(clk)
    
            
finally:
    GPIO.cleanup()


