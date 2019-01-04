#!/usr/bin/env python3
import socket
import ev3dev.brickpi3 as ev3


p = ev3.LegoPort(ev3.INPUT_2)
p.mode = "nxt-analog"
p.set_device = "lego-nxt-touch"

ts1 = ev3.TouchSensor(ev3.INPUT_2)
m = ev3.LargeMotor(ev3.OUTPUT_C)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if(buf == b'go'):
      print('received go command')
      m.run_forever(speed_sp=360)   # equivalent to power=20 in EV3-G
    elif(buf == b'stop'):
      print('received stop command')
      m.stop(stop_action="brake")
