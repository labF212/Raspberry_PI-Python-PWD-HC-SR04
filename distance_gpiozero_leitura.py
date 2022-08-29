from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)

try:
    while 1:
        distance = sensor.distance * 100     
        print("Distância : %.1f" % distance)
        sleep(3)
       
    
except KeyboardInterrupt:
    print("programa interrompido")