#!/usr/bin/python

import serial, time, sys

port    = '/dev/ttyUSB0'
max_len = 32

ser = serial.Serial(port, 38400)

def display_clock():

  counter = 0

  while True:
    current_time = time.asctime(time.localtime(time.time()))

    if counter == 0:
      text = 'GPS locked  '
      counter = 1

    else:
      text = 'GPS locked ' +  chr(254)        
      counter = 0
    
    while (len(current_time)) != max_len:
      current_time = current_time + ' ' 
    
    ser.write('\x0B')
    ser.write(current_time+text)
    time.sleep(1)

display_clock()
ser.close()

