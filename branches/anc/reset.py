#!/usr/bin/python
# Reset an Arduino board by toggling DTR.
# Usage: reset-arduino PORT
   
import sys, serial, time

port = "/dev/ttyUSB0"
if (len(sys.argv) > 1):
  port = sys.argv[1]

   
ser = serial.Serial(port, 57600)
   
ser.setDTR(0)
time.sleep(0.1)
ser.setDTR(1)

ser.close()
