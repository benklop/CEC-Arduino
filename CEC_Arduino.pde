#include "CEC_Device.h"
//#include "cli.h"
#include <Wire.h>
#include "edid.h"
#include "MemoryFree.h"
#include "packetserial.h"
#include "status.h"
#define IN_LINE 2
#define OUT_LINE 3
#define HOTPLUG 4
//21 bytes
//ptype
//length
//src
//dest
//byte[15]

//checksum

//extern CEC_Device device(0x3000);
CEC_Device device = NULL;

bool XX_GetLineState()
{
  int state = digitalRead(IN_LINE);
  return state == LOW;
}

void XX_SetLineState(CEC_Device* device, bool state)
{
  digitalWrite(OUT_LINE, state?LOW:HIGH);
  // give enough time for the line to settle before sampling
  // it
  delayMicroseconds(50);
  device->_lastLineState2 = XX_GetLineState();
}

void setup()
{
  Wire.begin();
  pinMode(OUT_LINE, OUTPUT);
  pinMode(IN_LINE, INPUT);

  digitalWrite(OUT_LINE, LOW);
  delay(1000);
  Serial.begin(115200);



  //DbgPrint("Free bytes: %i\r\n", freeMemory());
  //device.MonitorMode = true;
  int id = readEDID();
  device = CEC_Device(id);

  device.Promiscuous = true;
  device.Initialize(CEC_LogicalDevice::CDT_PLAYBACK_DEVICE);
  byte logical;
  logical = (byte)device.getLogical();
  send_addr(device.getPhysical(), logical);
  //send_addresses((byte)device.getPhysical(),(byte)device.getLogical());
  send_mem_status();


}

void loop()
{
  packet_serial_run();
  device.Run();
}
