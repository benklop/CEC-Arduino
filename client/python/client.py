#!/usr/bin/env python
import serial
from cmdcodes import *
import sys
import struct
#from cecprocess import *
import select
import array
import time

from ceccodes import *
from cmdcodes import *
from cecprocess import *
ser = None
  
def genchecksum(array):
  checksum = 256 - sum(array) % 256
  return checksum

def send_serial(bytes):
  global ser
  #if ser is None:
  #  print "SER is none!"
  #  sys.exit()
  packet = [0x02]
  packet.append(len(bytes))
  packet.extend(bytes)
  packet.append(genchecksum(packet[1:]))
  printpacket(packet)
  ser.write(array.array('B',packet).tostring())
  time.sleep(.01)



def getascii(bytes):
  newstring = str()
  for c in bytes:
    newstring = newstring + chr(c)
  return newstring

def printpacket(packet):
  for c in packet:
    print "%02x" % c,
  print ""

def addrstring(b1, b2):
  a1= (b1 & 0xf0)>>4
  a2= b1 & 0x0f
  a3= (b2 & 0xf0)>>4
  a4= b2 & 0x0f
  return "%i.%i.%i.%i " % (a1,a2,a3,a4)

def printaddr(b1,b2):
  print addrstring(b1,b2)


def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.read(1)
            if ("s" in input):
              send_serial([0xa1])
            elif ("q" in input):
              sys.exit()
            elif ("r" in input):
              send_phys()
            elif ("p" in input):
              #send_ping(0x00)
              send_power()
            elif ("a" in input): #announce
              #CEC_INFO_PHYS_ADDR 
              send_phys()
              #CEC_VENDOR_ID
              send_vendor()
              send_osd()
            elif ("n" in input):
              send_osd()  
            elif ("v" in input):
              send_getvendor()
              
            return True
    return False

    
def process_status(payload):
  
  
  if payload[1] == 0xf0:
    memfree = payload[2] + (payload[3]<<8)
    print "Memory free: %i bytes" % memfree
  elif payload[1] == 0xa0:
    print "CEC Physical Address: %02x%02x" % (payload[3] , payload[2])
    print "CEC Logical Address: %02x" % payload[4]
    device.logical = payload[4]
    device.physical = (payload[3]<<8) + payload[2]
  else:
    print "Device Status"
    printpacket(payload);

def process(payload):
  #printpacket(payload)
  messagetype = payload[0]
  if (messagetype == RECV_PACKET):
    print "CECPacket",
    device.process_cec(payload)
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
  ser.setTimeout(.01)
  readbyte =ser.read(1)
  if (readbyte is not ""):
    x = ord(readbyte)
  else:
    x = 0
  ser.setTimeout(None)
  #print "byte read %#x" % x
  if (x == 0xFD):
    #print "ACK"
    return
  if (x == 0xFE):
    print "NACK"
    return
  
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


def main():
  global device    
  global ser
  if ser is None:
    print "initial ser none"
  
  PORT = '/dev/ttyUSB0'
  if len(sys.argv) > 1:
      PORT = sys.argv[1]
  
  #global ser
  ser = serial.Serial(PORT, 115200)
  #global ser
  if ser is None:
    print "SER is none!"
    sys.exit()
  
  device = CECDevice();
  device.serial = ser
  
  while True:
    readserial()
    heardEnter()

if __name__ == "__main__":
    main()
