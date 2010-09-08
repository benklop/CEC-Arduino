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
  
def genchecksum(array):
  checksum = 256 - sum(array) % 256
  return checksum

def getascii(bytes):
  newstring = str()
  for c in bytes:
    newstring = newstring + chr(c)
  return newstring
