from gpiozero import DistanceSensor #biblioteca para comunicação entrada/saída Raspberry
from time import sleep              #biblioteca para usar funções de tempo 

import threading
import PySimpleGUI as sg

sensor = DistanceSensor(echo=23, trigger=24) #definir onde ligar o sensor

#Tema do programa
sg.change_look_and_feel('DarkGrey')

layout = [
    [sg.Text('Distância do sensor (cm):',key='-MEDIDA-',expand_x=True)],
    [sg.Button('Ok',key='-SAIR-')]
            ], #menu

window = sg.Window('Medição do avanço e recuo do cilindro pneumático',layout, resizable=True,size=(500,200))
#finalize=True

while True:
    event, values = window.read(timeout=2000)
                                      #faz loop contínuo
    distance = sensor.distance * 100     
      
    if event == sg.WIN_CLOSED or event == '-SAIR-':
        break
    window['-MEDIDA-'].update( "Distância do sensor (cm): %.1f" % distance)

window.close()
