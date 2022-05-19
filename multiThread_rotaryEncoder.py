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
from Timer import Timer

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
    timerLavage = Timer()

    timerGauche = Timer()
    timerDroit = Timer()


    # threadLeft = Thread(target=startRotary,args=(22,23, 'l'))
    # threadRight = Thread(target=startRotary,args=(17,18, 'r'))

    leftEncoderDirection = None
    rightEncoderDirection = None
    rightEncoderValue = 0
    leftEncoderValue = 0

    seLaveLesMains = False


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
        if raw_measurement < 20: personneEstDevantRobinet = True 
        else: personneEstDevantRobinet = False
        
        if leftEncoderValue > 5: leftRobinetIsOpen = True
        else: leftRobinetIsOpen = False
        
        if rightEncoderValue > 5: rightRobinetIsOpen = True
        else: rightRobinetIsOpen = False

        seLaveLesMains=(personneEstDevantRobinet and (leftRobinetIsOpen or rightRobinetIsOpen))
        if seLaveLesMains and timerLavage.timestarted is None: timerLavage.start()
        elif not seLaveLesMains and timerLavage.timestarted is not None: timerLavage.pause()

        if leftRobinetIsOpen and timerGauche.timestarted is None: #Gauche ouvert et pas encore démarré
            timerGauche.start()
        
        if rightRobinetIsOpen and timerDroit.timestarted is None: #Droit ouvert et pas encore démarré
            timerDroit.start()
        
        if not leftRobinetIsOpen and timerGauche.timestarted is not None: #Gauche fermé et démarré
            timerGauche.pause()
        elif leftRobinetIsOpen and timerGauche.paused: #Gauche ouvert et en pause
            timerGauche.resume()
        
        if not rightRobinetIsOpen and timerDroit.timestarted is not None: #Droit fermé et démarré
            timerDroit.pause()
        elif rightRobinetIsOpen and timerDroit.paused: #Droit ouvert et en pause
            timerDroit.resume()
        
        

        if buttonSavon.is_pressed:
            nombrePushSavon+=1
            sleep(0.5)

        if seLaveLesMains:
            print('\033c')
            print('\r'+"leftEncoderValue: ", leftEncoderValue, "leftEncoderDirection: ", leftEncoderDirection, "rightOpen: ", rightRobinetIsOpen)
            print('\r'+"rightEncoderValue: ", rightEncoderValue, "rightEncoderDirection: ", rightEncoderDirection, "leftOpen: ", leftRobinetIsOpen)
            print('\r'+"nombrePushSavon: ", nombrePushSavon)
            print('\r'+'Raw distance: ', raw_measurement)
            print('\r'+'seLaveLesMains: ', seLaveLesMains)
            print('\r'+'timerLavage.timestarted: ', timerLavage.timestarted, 'timerLavage.timeleft: ', timerLavage.get(), 'timerLavage.elapsedPaused: ', timerLavage.getElapsedPaused())
            print('\r'+'timerGauche.timestarted: ', timerGauche.timestarted, 'timerGauche.timeleft: ', timerGauche.get())
            print('\r'+'timerDroit.timestarted: ', timerDroit.timestarted, 'timerDroit.timeleft: ', timerDroit.get())

            # obj = Data(rotation_d=rightEncoderValue, rotation_g=leftEncoderValue, savon=nombrePushSavon, distance=raw_measurement).to_dict
            # sensorData=SensorData(obj)
            # data=sensorData.to_dict()
            # print(data)
            sleep(0.05)
            data = {
                "data":
                    {
                    "rotationG": leftEncoderValue,
                    "rotationD": rightEncoderValue,
                    "distance": raw_measurement,

                    "savon": nombrePushSavon,
                    "temps" : timerLavage.get(),
                    "tempsGauche" : timerGauche.get(),
                    "tempsDroit" : timerDroit.get(),
                    }
                }
            #output data in json format, if file is not found, create it
            if timerLavage.getElapsedPaused().seconds>30:
                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile)
                break
        
    # clkLastState = GPIO.input(clk)
    
            
finally:
    GPIO.cleanup()


