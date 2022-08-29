# coding=utf-8

from gpiozero import DistanceSensor,PWMLED
from time import sleep

import PySimpleGUI as sg
import threading

rows = []
filename =''
header = "Tensão de saída(%)"," Distância "

start_A=1
stop_A=15
start_B=1
stop_B=15

data=[]

layout =[
        [sg.Text("Pressione o botão SHOW para recolher dados")],
        [sg.Table(values=data,
                            headings=header,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='right',
                            alternating_row_color='blue',
                            key='-TABLE-',
                            num_rows=(20),
                            size=(150,150),
                            expand_x=True,
        )],
        [sg.Push(),
        sg.Button('Some data',key='-SHOW-'),sg.Spin(initial_value=1,values=list(range(start_A,stop_A)),enable_events=True,size=(5,5),key='-MAXSPIN-'),sg.Spin(initial_value=1,values=list(range(start_B,stop_B)),enable_events=True,size=(5,5),key='-MINSPIN-'), 
        sg.Button('All Data',key='-ALL-'),sg.Button('CLEAR'), sg.Button('EXIT'),sg.Push()]
        ]

sensor = DistanceSensor(echo=23, trigger=24)
led= PWMLED(17)
a=0

def update():
    valores =[1.0,0.8,0.6,0.4,0.2,0,0.0,0.2,0.4,0.6,0.8,1.0]
    for i in valores:
        a=a+1
        distance = sensor.distance * 100     
        led.value = i
        print("Distância : %.1f" % distance)
        print("PWD : %.1f" % i)
        sleep(0.7)
        print(a)
        window['-TABLE-'].Update(values=rows)
        window['-TABLE-'].Update(alternating_row_color='green')
    if a==len(valores):
        print("programa terminado")
        a=1000
        



window = sg.Window('My CSV File',layout,resizable=True)

while True:
    event,values=window.read(timeout=500)
    
    
    if event in (sg.WIN_CLOSED,"EXIT"):
        break

    if event =='CLEAR':
            print('clear')
            window['-TABLE-'].Update(values='')
            rows=[]
    if event =='SHOW':
        threading.Thread(target=update,daemon=True).start()    
   
window.close()   

