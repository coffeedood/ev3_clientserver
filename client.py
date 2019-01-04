#!/usr/bin/env python3
import ev3dev.brickpi3 as ev3
import socket

p = ev3.LegoPort(ev3.INPUT_2)
p.mode = "nxt-analog"
p.set_device = "lego-nxt-touch"

ts1 = ev3.TouchSensor(ev3.INPUT_2)
m=ev3.LargeMotor(ev3.OUTPUT_C)

ip='10.0.0.97'
b1 = True
while True:
    if ts1.value() == 0:
      if(b1 == False):
        print('sending stop')
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ip, 8089))
        clientsocket.send(b'stop')
        clientsocket.close()
      b1 = True
    else:
      if(b1 == True):
        print('sending go')
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ip, 8089))
        clientsocket.send(b'go')
        clientsocket.close()
        b1 = False

