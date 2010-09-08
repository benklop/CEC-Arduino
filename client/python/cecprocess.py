from ceccodes import *
from cmdcodes import *
#from client import *
from helper import *
import array
import time

class CECDevice:
  serial = None
  vendor=0x001337
  OSDName= "HTPC"
  physical = 0x2000
  logical = 4
  CECVersion=V13A
  def physa(self):
    return self.physical>>8
  def physb(self):
    return self.physical&0xFF
  def venb1(self):
    return (self.vendor)>>16
  def venb2(self):
    return ((self.vendor)&0x00FF00)>>8
  def venb3(self):
    return (self.vendor)&0x0000FF
  
  def handle_sys_info(self, payload):
    op = payload[3]
    print cec[op]
    if (op == CEC_INFO_LANG_REQ):
      self.send_packet(self.logical, BROADCAST, [CEC_INFO_LANG, 'e', 'n', 'g' ])   #FIXME
    elif (op == CEC_INFO_REQ_PHYS_ADDR):
      self.send_packet(self.logical, BROADCAST, [CEC_INFO_PHYS_ADDR, self.physa(), self.physb(), self.logical])
    elif (op == CEC_INFO_VERSION_REQ):
      self.send_packet(self.logical, BROADCAST, [CEC_INFO_VERSION, self.CECVersion])
    elif (op == CEC_OSD_REQ_OSD):
      data = [CEC_OSD_SET_OSD]
      for c in self.OSDName:
        data.append(ord(c))
      self.send_packet(self.logical, payload[1], data)
    elif (op == CEC_VENDOR_ID_REQ):
      self.send_packet(self.logical, BROADCAST, [CEC_VENDOR_ID, self.venb1(), self.venb2(), self.venb3()])
  
  def handle_routing(self, payload):
    op = payload[3]
    print cec[op]
    if (op == CEC_ROUTING_REQ_PATH):
      self.send_packet(self.logical, BROADCAST, [CEC_ROUTING_ACTIVE, self.physa(), self.physb()])
      
  def handle_state(self, payload):
    op = payload[3]
    print cec[op]
    if (op == CEC_POWER_REQ_STATUS):
      self.send_packet(self.logical, payload[1], [CEC_POWER_STATUS, 0x00], True)
  
  def send_packet(self, src, dest, data, pp=False):
    ba = [SEND_PACKET]
    ba.append(src)
    ba.append(dest)
    ba.extend(data)
    self.send_serial(ba, pp)
  def send_serial(self, bytes, pp=False):
    #if ser is None:
    #  print "SER is none!"
    #  sys.exit()
    packet = [0x02]
    packet.append(len(bytes))
    packet.extend(bytes)
    packet.append(genchecksum(packet[1:]))
    if pp:
      printpacket(packet)
    self.serial.write(array.array('B',packet).tostring())
    time.sleep(.01)
  def process_cec(self, payload):
    print "%x -> %x" % (payload[1],payload[2]),
    #print "Destination: %x" % payload[2],
    #if there is no opcode, it is a ping message
    if (len(payload) < 4):
      print "Ping"
      return
  
    #identify message type
    op = payload[3]
    print cec[op]
    if ((op in SYS_INFO or op == CEC_OSD_REQ_OSD) and payload[2] == self.logical):
      self.handle_sys_info(payload)
    elif (op in STATE and payload[2] == self.logical):
      self.handle_state(payload)
    elif (op in ROUTING):
      self.handle_routing(payload)
    elif (op == CEC_INFO_PHYS_ADDR):
      print "New source: ",
      printaddr(payload[4],payload[5])
      printpacket(payload)
      
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
  
    elif (op == CEC_MENU_REQ):
      print "Menu Request: %i" % payload[4]
  
    elif (op == CEC_INFO_VERSION):
      print "CEC Version: %s" % cec_version[payload[4]]
  
    elif (op == CEC_FEATURE_ABORT):
      print "Abort reason: %i" % payload[5]
  
    else:
      if op in cec:
        if op in REQUESTS and payload[1] == self.logical:
          print "Feature Abort"
          #send feature abort, since not handled above
          self.send_packet(self.logical, payload[1], [CEC_FEATURE_ABORT, 4])
        #Only print packet if it has a payload
        if (("_REQ" not in cec[op]) and ("FEATURE_ABORT" not in cec[op]) ):
          printpacket(payload)

#def send_osd(dest):
#  payload = [SEND_PACKET, device.logical, dest, CEC_OSD_SET_OSD ]
#  for c in device.OSDName:
#   payload.append(ord(c))
#  send_serial( payload)



#def send_serial(bytes):
#  packet = [0x02]
#  packet.append(len(bytes))
#  packet.extend(bytes)
#  packet.append(genchecksum(packet[1:]))
#  printpacket(packet)
#  device.serial.write(array.array('B',packet).tostring())


  
#def send_phys():
#  send_packet(device.logical, BROADCAST, [CEC_INFO_PHYS_ADDR, device.physa(), device.physb(), 0x04 ])

#def send_vendor():
#  send_packet(device.logical, BROADCAST, [CEC_VENDOR_ID, device.vendor1, device.vendor2, device.vendor3])

def send_ping(target):
  send_serial([SEND_PACKET, device.logical,target])

#
# Process CEC packets
#
