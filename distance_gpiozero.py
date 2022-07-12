from gpiozero import DistanceSensor,PWMLED
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)
led= PWMLED(17)
a=0
#f = -0.1
try:
    valores =[1.0,0.8,0.6,0.4,0.2,0,0.0,0.2,0.4,0.6,0.8,1.0]
    for i in valores:
        a=a+1
        distance = sensor.distance * 100     
        led.value = i
        print("Distância : %.1f" % distance)
        print("PWD : %.1f" % i)
        sleep(10)
        print(a)
        if a==len(valores):
            print("programa terminado")
    
    
    '''
    while f <= 1:
        f=f+0.1  
            
            
        print (f)
        distance = sensor.distance * 100
        if f>1:
            f=1.0
            break
        led.value = f
        print("Distance : %.1f" % distance)
        print("PWD : %.1f" % f)
        sleep(1)
        
        f=f-0.1
    while f >= 0:
            f=f-0.1  
                        
            print (f)
            distance = sensor.distance * 100
            
            led.value = f
            print("Distance : %.1f" % distance)
            print("PWD : %.1f" % f)
            sleep(1)
       '''
    
except KeyboardInterrupt:
    print("programa interrompido")