from ceccodes import *
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
  #if there is no oppcode, it is a ping message
  if (len(payload) < 4):
    print "Ping"
    return
  #identify message type
  opp = payload[3]
  if (opp == CEC_INFO_PHYS_ADDR):
    print cec[opp]
    print "New source: ",
    printaddr(payload[4],payload[5])
  elif (opp == CEC_ROUTING_ACTIVE):
    print "CEC_ROUTING_ACTIVE"
    print "Active Source: ",
    printaddr(payload[4],payload[5])
  elif (opp == CEC_ROUTING_CHANGED):
    print cec[opp]
    print "Previous Source: %s New Source: %s" % ( addrstring(payload[4],payload[5]), addrstring(payload[6],payload[7]) )
  elif (opp == CEC_VENDOR_ID):
    print cec[opp]
    print "Vendor ID: %x" % ( (payload[4]<<16) + (payload[5]<<8) + payload[6])
  elif (opp == CEC_OSD_SET_OSD):
    print cec[opp]
    osd = str()
    for c in (payload[4:]):
      osd = osd + chr(c)
    print "OSD Name: %s"%osd
    #$osd = osd.decode('ascii')
    #print osd
    #printpacket(payload)
  elif (opp == CEC_INFO_LANG):
    print cec[opp]
    lang = str()
    for c in (payload[4:]):
      lang = lang + chr(c)
    print "Lang: %s" % lang
    
  elif (opp == CEC_VENDOR_COMMAND_ID):
    print cec[opp]
    print "Vendor command: ",
    printpacket(payload[4:])
  elif (opp == CEC_INFO_VERSION):
    print "CEC Version: %s" % cec_version[payload[4]]
  else:
    if opp in cec:
      print cec[opp]
      if (("_REQ" not in cec[opp]) and ("FEATURE_ABORT" not in cec[opp])):
        printpacket(payload)