#!/usr/bin/python

import serial, time, sys

# Serial port settings
port    = '/dev/ttyUSB0'
speed   = 38400

# Display related stuffs
max_len    = 32
clear      = '\x0C'
feed       = '\x0B'

def display_clock():

  ser = serial.Serial(port, speed)
  ser.write(clear)
  counter = 0

  while True:
    current_time = time.asctime(time.localtime(time.time()))

    if counter == 0:
      text = 'GPS locked        '
      counter = 1

    else:
      text = 'GPS locked ' +  chr(254)        
      counter = 0
    
    while (len(current_time)) != max_len:
      current_time = current_time + ' ' 
    
    ser.write(feed + current_time + text)
    time.sleep(1)

display_clock()
ser.close()

