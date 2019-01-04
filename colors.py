#!/usr/bin/env python3
import socket
import ev3dev.ev3 as ev3
import time



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

delay=0.1

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if(buf == b'go'):
      print('received go command')
      ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
      ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
      time.sleep(delay)
      ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
      ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
      time.sleep(delay)
      ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
      ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
      time.sleep(delay)
    elif(buf == b'stop'):
      print('received stop command')
      

