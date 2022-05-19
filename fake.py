import json
from time import sleep
from Timer import Timer
import random
leftEncoderValue=0
rightEncoderValue=0
raw_measurement=0
nombrePushSavon=0
timerLavage=Timer()
timerGauche=Timer()
timerDroit=Timer()

timerDroit.start()
timerGauche.start()
timerLavage.start()
# while True:
sleep(5)
leftEncoderValue=random.randint(0,10)
rightEncoderValue=random.randint(0,10)
raw_measurement=random.randint(0,10)
nombrePushSavon=random.randint(0,10)
data = {
    "data":
        {
        "rotationG": leftEncoderValue,
        "rotationD": rightEncoderValue,
        "distance": raw_measurement,

        "savon": nombrePushSavon,
        "temps" : timerLavage.get().total_seconds(),
        "tempsGauche" : timerGauche.get().total_seconds(),
        "tempsDroit" : timerDroit.get().total_seconds(),
        }
    }
#output data in json format, if file is not found, create it
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, default=str)

timerDroit.pause()
timerGauche.pause()
timerLavage.pause()



        