from ceccodes import *

def getascii(bytes):
  newstring = str()
  for c in bytes:
    string = string + chr(c)
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

def process_cec(payload):
  print "Source: %x," % payload[1],
  print "Destination: %x" % payload[2],
  #if there is no operand, it is a ping message
  if (len(payload) < 4):
    print "Ping"
    return
  #identify message type
  op = payload[3]
  print cec[op]
  if (op == CEC_INFO_PHYS_ADDR):
    print "New source: ",
    printaddr(payload[4],payload[5])
    
  elif (op == CEC_ROUTING_ACTIVE):
    print "Active Source: ",
    printaddr(payload[4],payload[5])
  
  elif (op == CEC_ROUTING_CHANGED):
    print "Previous Source: %s New Source: %s" % ( addrstring(payload[4],payload[5]), addrstring(payload[6],payload[7]) )
  
  elif (op == CEC_VENDOR_ID):
    print "Vendor ID: %x" % ( (payload[4]<<16) + (payload[5]<<8) + payload[6])
  
  elif (op == CEC_OSD_SET_OSD):
    print "OSD Name: %s"% getascii(payload[4:])
  
  elif (op == CEC_INFO_LANG):
    print "Lang: %s" % getascii(payload[4:])
    
  elif (op == CEC_VENDOR_COMMAND_ID):
    print "Vendor command: ",
    printpacket(payload[4:])
  
  elif (op == CEC_INFO_VERSION):
    print "CEC Version: %s" % cec_version[payload[4]]
  
  else:
    if op in cec:
      #Only print packet if it has a payload
      if (("_REQ" not in cec[op]) and ("FEATURE_ABORT" not in cec[op])):
        printpacket(payload)