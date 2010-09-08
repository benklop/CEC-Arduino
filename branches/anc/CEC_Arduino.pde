#include "CEC_Device.h"
//#include "cli.h"
#include <Wire.h>
#include "edid.h"
#include "MemoryFree.h"
#include "packetserial.h"
#include "status.h"
#include "cmdcodes.h"
#define IN_LINE 2
#define OUT_LINE 3
//#define HOTPLUG 4
#define LED1 4
#define LED2 5
#define LED3 6
#define LED4 7
#define LED5 8
#define LED6 9

//21 bytes
//ptype
//length
//src
//dest
//byte[15]

//checksum

//extern CEC_Device device(0x3000);
CEC_Device device = NULL;

void set_led(byte led, bool on){
  int pin = LED1;
  switch(led){
    case 1:
      pin = LED1;
      break;
    case 2:
      pin = LED2;
      break;
    case 3:
      pin = LED3;
      break;
    case 4:
      pin = LED4;
      break;
    case 5:
      pin = LED5;
      break;
    case 6:
      pin = LED6;
      break;
    default:
      return;
  }
  digitalWrite(pin, on ? HIGH : LOW);
  }

void handle_packet(byte* payload, byte length){
  //send_mem_status();
  if (payload[0] == REQ_ADD){
    send_addr(device.getPhysical(), device.getLogical());
  }
  if (payload[0] == SEND_PACKET){
    //read target addr from packet
    device.TransmitFrame(payload[2], &payload[3], length -3);
  }
}

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

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  pinMode(LED6, OUTPUT);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);
  digitalWrite(LED5, LOW);
  digitalWrite(LED6, LOW);
  
  
  digitalWrite(OUT_LINE, LOW);
  delay(1000);
  Serial.begin(115200);

  //device.MonitorMode = true;
  //int id = readEDID();
  device = CEC_Device(0x2000);

  device.Promiscuous = true; //Relay all line traffic
  device.Initialize(CEC_LogicalDevice::CDT_PLAYBACK_DEVICE);
  send_addr(device.getPhysical(), device.getLogical());
  send_mem_status();
  digitalWrite(LED1, HIGH);

}

void loop()
{
  //digitalWrite(LED2, HIGH);
  packet_serial_run();
  device.Run();
}
