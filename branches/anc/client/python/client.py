#!/usr/bin/env python
import serial
from cmdcodes import *
import sys
import struct
from cecprocess import *


  
def process_status(payload):
  print "Device Status"
  printpacket(payload);
  if payload[1] == 0xf0:
    memfree = payload[2] + (payload[3]<<8)
    print "Memory free: %i bytes" % memfree
  elif payload[1] == 0xa0:
    print "CEC Physical Address: %02x%02x" % (payload[3] , payload[2])

def process(payload):
  #printpacket(payload)
  messagetype = payload[0]
  if (messagetype == RECV_PACKET):
    print "CECPacket",
    process_cec(payload)
    #process cec
  elif (messagetype == STATUS):
    process_status(payload)
  else:
    print "Packet received: ", 
    printpacket(payload)
    

def checksum(array):
  cb = array.pop()
  checksum = 256 - sum(array) % 256
  if (cb == checksum):
    #print "valid checksum"
    del array[0]
    return True
  else:
    return False  

def readserial():
  x = ord(ser.read(1))
  #print "byte read %#x" % x
  if (x == 0x02):
    length = ord(ser.read(1))
    packet = [length] 
    for i in range(length):
      packet.append(ord(ser.read(1)))
#    packet = ser.read(length)
    packet.append(ord(ser.read(1)))
    ret = checksum(packet)
    #print ret
    if (ret):
      process(packet)
    else:
      print "invalid packet"
      printpacket(packet)
    
PORT = '/dev/ttyUSB0'
if len(sys.argv) > 1:
    PORT = sys.argv[1]

ser = serial.Serial(PORT, 115200)

while True:
  readserial()