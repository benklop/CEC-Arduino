BROADCAST = 0x0F

CEC_FEATURE_ABORT = 0x00 
CEC_OTP_IMAGE_ON = 0x04 
CEC_TUNER_UP = 0x05 
CEC_TUNER_DOWN = 0x06 
CEC_TUNER_STATUS = 0x07 
CEC_TUNER_STATUS_REQ = 0x08 
CEC_OTR_REC_ON = 0x09 
CEC_OTR_REC_STATUS = 0x0A 
CEC_OTR_REC_OFF = 0x0B 
CEC_OTP_TEXT_ON = 0x0D 
CEC_OTR_REC_SCREEN = 0x0F 
CEC_DECK_REQ_STATUS = 0x1A 
CEC_DECK_STATUS = 0x1B 
CEC_INFO_LANG = 0x32 
CEC_TIMER_CLEAR_ANALOG = 0x33 
CEC_TIMER_SET_ANALOG = 0x34 
CEC_TIMER_STATUS = 0x35 
CEC_STANDBY = 0x36 
CEC_DECK_PLAY = 0x41 
CEC_DECK_CTRL = 0x42 
CEC_TIMER_STATUS_CLEARED = 0x43 
CEC_MENU_UC_PRESSED = 0x44 
CEC_RCP_PRESSED = 0x44 
CEC_AUDIO_UC_PRESSED = 0x44 
CEC_MENU_UC_RELEASED = 0x45 
CEC_RCP_RELEASED = 0x45 
CEC_AUDIO_UC_RELEASED = 0x45 
CEC_OSD_REQ_OSD = 0x46 
CEC_OSD_SET_OSD = 0x47 
CEC_OSD_SEND = 0x64 
CEC_TIMER_SET_TITLE = 0x67 
CEC_AUDIO_MODE_REQ = 0x70 
CEC_AUDIO_STATUS_REQ = 0x71 
CEC_AUDIO_MODE_SET = 0x72 
CEC_AUDIO_STATUS = 0x7A 
CEC_AUDIO_MODE_REQ = 0x7D 
CEC_AUDIO_MODE = 0x7E 
CEC_ROUTING_CHANGED = 0x80 
CEC_ROUTING_INFO = 0x81 
CEC_OTP_ACTIVE_SRC = 0x82 
CEC_ROUTING_ACTIVE = 0x82 
CEC_INFO_REQ_PHYS_ADDR = 0x83 
CEC_INFO_PHYS_ADDR = 0x84 
CEC_ROUTING_REQ_ACTIVE = 0x85 
CEC_ROUTING_REQ_PATH = 0x86 
CEC_VENDOR_ID = 0x87 
CEC_VENDOR_COMMAND = 0x89 
CEC_VENDOR_REMOTE_BDOWN = 0x8A 
CEC_VENDOR_REMOTE_BUP = 0x8B 
CEC_VENDOR_ID_REQ = 0x8C 
CEC_MENU_REQ = 0x8D 
CEC_MENU_STATUS = 0x8E 
CEC_POWER_REQ_STATUS = 0x8F 
CEC_POWER_STATUS = 0x90 
CEC_INFO_LANG_REQ = 0x91 
CEC_TUNER_SELECT_ANALOG = 0x92 
CEC_TUNER_SELECT_DIGITAL = 0x93 
CEC_TIMER_SET_DIGITAL = 0x97 
CEC_TIMER_CLEAR_DIGITAL = 0x99 
CEC_AUDIO_RATE = 0x9A 
CEC_ROUTING_INACTIVE = 0x9D 
CEC_INFO_VERSION = 0x9E 
CEC_VENDOR_CEC_VERSION = 0x9E 
CEC_INFO_VERSION_REQ = 0x9F 
CEC_VENDOR_CEC_VERSION_REQ = 0x9F 
CEC_VENDOR_COMMAND_ID = 0xA0 
CEC_TIMER_CLEAR_EXTERNAL = 0xA1 
CEC_TIMER_SET_EXTERNAL = 0xA2 

cec={
CEC_FEATURE_ABORT   : "CEC_FEATURE_ABORT",
CEC_OTP_IMAGE_ON    : "CEC_OTP_IMAGE_ON",
CEC_TUNER_UP    : "CEC_TUNER_UP",
CEC_TUNER_DOWN  : "CEC_TUNER_DOWN",
CEC_TUNER_STATUS    : "CEC_TUNER_STATUS",
CEC_TUNER_STATUS_REQ    : "CEC_TUNER_STATUS_REQ",
CEC_OTR_REC_ON  : "CEC_OTR_REC_ON",
CEC_OTR_REC_STATUS  : "CEC_OTR_REC_STATUS",
CEC_OTR_REC_OFF : "CEC_OTR_REC_OFF",
CEC_OTP_TEXT_ON : "CEC_OTP_TEXT_ON",
CEC_OTR_REC_SCREEN  : "CEC_OTR_REC_SCREEN",
CEC_DECK_REQ_STATUS : "CEC_DECK_REQ_STATUS",
CEC_DECK_STATUS : "CEC_DECK_STATUS",
CEC_INFO_LANG   : "CEC_INFO_LANG",
CEC_TIMER_CLEAR_ANALOG  : "CEC_TIMER_CLEAR_ANALOG",
CEC_TIMER_SET_ANALOG    : "CEC_TIMER_SET_ANALOG",
CEC_TIMER_STATUS    : "CEC_TIMER_STATUS",
CEC_STANDBY : "CEC_STANDBY",
CEC_DECK_PLAY   : "CEC_DECK_PLAY",
CEC_DECK_CTRL   : "CEC_DECK_CTRL",
CEC_TIMER_STATUS_CLEARED    : "CEC_TIMER_STATUS_CLEARED",
CEC_MENU_UC_PRESSED : "CEC_MENU_UC_PRESSED",
CEC_RCP_PRESSED : "CEC_RCP_PRESSED",
CEC_AUDIO_UC_PRESSED    : "CEC_AUDIO_UC_PRESSED",
CEC_MENU_UC_RELEASED    : "CEC_MENU_UC_RELEASED",
CEC_RCP_RELEASED    : "CEC_RCP_RELEASED",
CEC_AUDIO_UC_RELEASED   : "CEC_AUDIO_UC_RELEASED",
CEC_OSD_REQ_OSD : "CEC_OSD_REQ_OSD",
CEC_OSD_SET_OSD : "CEC_OSD_SET_OSD",
CEC_OSD_SEND    : "CEC_OSD_SEND",
CEC_TIMER_SET_TITLE : "CEC_TIMER_SET_TITLE",
CEC_AUDIO_MODE_REQ  : "CEC_AUDIO_MODE_REQ",
CEC_AUDIO_STATUS_REQ    : "CEC_AUDIO_STATUS_REQ",
CEC_AUDIO_MODE_SET  : "CEC_AUDIO_MODE_SET",
CEC_AUDIO_STATUS    : "CEC_AUDIO_STATUS",
CEC_AUDIO_MODE_REQ  : "CEC_AUDIO_MODE_REQ",
CEC_AUDIO_MODE  : "CEC_AUDIO_MODE ",
CEC_ROUTING_CHANGED : "CEC_ROUTING_CHANGED",
CEC_ROUTING_INFO    : "CEC_ROUTING_INFO",
CEC_OTP_ACTIVE_SRC  : "CEC_OTP_ACTIVE_SRC",
CEC_ROUTING_ACTIVE  : "CEC_ROUTING_ACTIVE",
CEC_INFO_REQ_PHYS_ADDR  : "CEC_INFO_REQ_PHYS_ADDR",
CEC_INFO_PHYS_ADDR  : "CEC_INFO_PHYS_ADDR ",
CEC_ROUTING_REQ_ACTIVE  : "CEC_ROUTING_REQ_ACTIVE",
CEC_ROUTING_REQ_PATH    : "CEC_ROUTING_REQ_PATH",
CEC_VENDOR_ID   : "CEC_VENDOR_ID",
CEC_VENDOR_COMMAND  : "CEC_VENDOR_COMMAND ",
CEC_VENDOR_REMOTE_BDOWN : "CEC_VENDOR_REMOTE_BDOWN",
CEC_VENDOR_REMOTE_BUP   : "CEC_VENDOR_REMOTE_BUP",
CEC_VENDOR_ID_REQ   : "CEC_VENDOR_ID_REQ",
CEC_MENU_REQ    : "CEC_MENU_REQ",
CEC_MENU_STATUS : "CEC_MENU_STATUS",
CEC_POWER_REQ_STATUS    : "CEC_POWER_REQ_STATUS",
CEC_POWER_STATUS    : "CEC_POWER_STATUS",
CEC_INFO_LANG_REQ   : "CEC_INFO_LANG_REQ",
CEC_TUNER_SELECT_ANALOG : "CEC_TUNER_SELECT_ANALOG",
CEC_TUNER_SELECT_DIGITAL    : "CEC_TUNER_SELECT_DIGITAL",
CEC_TIMER_SET_DIGITAL   : "CEC_TIMER_SET_DIGITAL",
CEC_TIMER_CLEAR_DIGITAL : "CEC_TIMER_CLEAR_DIGITAL",
CEC_AUDIO_RATE  : "CEC_AUDIO_RATE ",
CEC_ROUTING_INACTIVE    : "CEC_ROUTING_INACTIVE",
CEC_INFO_VERSION    : "CEC_INFO_VERSION",
CEC_VENDOR_CEC_VERSION  : "CEC_VENDOR_CEC_VERSION",
CEC_INFO_VERSION_REQ    : "CEC_INFO_VERSION_REQ",
CEC_VENDOR_CEC_VERSION_REQ  : "CEC_VENDOR_CEC_VERSION_REQ ",
CEC_VENDOR_COMMAND_ID   : "CEC_VENDOR_COMMAND_ID",
CEC_TIMER_CLEAR_EXTERNAL    : "CEC_TIMER_CLEAR_EXTERNAL",
CEC_TIMER_SET_EXTERNAL  : "CEC_TIMER_SET_EXTERNAL"}

#VERSION 
V11= 0x00
V12= 0x01
V12A= 0x02
V13= 0x03
V13A= 0x04

cec_version = { V11 : "1.1", V12 : "1.2", V12A : "1.2a", V13 : "1.3", V13A : "1.3a" }

cec_abort_reason = { 
0 : "Unrecognized opcode",
1 : "Not in correct mode to respond",
2 : "Cannot provide source",
3 : "Invalid operand",
4 : "Refused" }

cec_analog_brodcast_type = { 0x00 : "Cable", 0x01 : "Satellite", 0x02 : "Terrestrial" }

cec_audio_rate = { 0 : "Rate Control Off", 1 : "Standard rate (IEEE 1394)", 2 : "Fast rate (IEEE 1394)", 3 : "Slow rate (IEEE 1394)", 4 : "Standard Rate (HDMI)", 5 : "Fast Rate (HDMI)", 6 : "Slow Rate (HDMI)"}

cec_deck_control_mode = { 1 : "Skip Forward", 2:"Skip Reverse", 3:"Stop", 4:"Eject"}
cec_deck_info = {
0x11:"Play",
0x12:"Record",
0x13:"Play Reverse",
0x14:"Still",
0x15:"Slow",
0x16:"Slow Reverse",
0x17:"Fast Forward",
0x18:"Fast Reverse",
0x19:"No Media",
0x1B:"Skip Forward",
0x1C:"Skip Reverse",
0x1D:"Index Search Forward",
0x1E:"Index Search Reverse",
0x1F:"Other"}
cec_device_type = {
0:"TV",
1:"Recording Device",
2:"Reserved",
3:"Tuner",
4:"Playback Device",
5:"Audio System"}
cec_menu_req_type = { 0:"Activate", 1:"Deactivate", 2:"Query"}
cec_menu_state = {0:"Activated",1:"Deactivated"}
cec_system_information = [0x32,0x83,0x84,0x91,0x9E,0x9F]

SYS_INFO = [
CEC_INFO_LANG,
CEC_INFO_REQ_PHYS_ADDR,
CEC_INFO_PHYS_ADDR,
CEC_INFO_LANG_REQ,
CEC_INFO_VERSION,
CEC_INFO_VERSION_REQ,
CEC_VENDOR_ID_REQ ]

STATE = [
CEC_POWER_REQ_STATUS ]

ROUTING = [
CEC_ROUTING_REQ_PATH ]

REQUESTS = [
CEC_AUDIO_MODE_REQ,
CEC_AUDIO_MODE_REQ,
CEC_AUDIO_STATUS_REQ,
CEC_DECK_REQ_STATUS,
CEC_INFO_LANG_REQ,
CEC_INFO_REQ_PHYS_ADDR,
CEC_INFO_VERSION_REQ,
CEC_MENU_REQ,
CEC_OSD_REQ_OSD,
CEC_POWER_REQ_STATUS,
CEC_ROUTING_REQ_ACTIVE,
CEC_ROUTING_REQ_PATH,
CEC_TUNER_STATUS_REQ,
CEC_VENDOR_CEC_VERSION_REQ,
CEC_VENDOR_ID_REQ,
CEC_OTR_REC_OFF,
CEC_OTR_REC_SCREEN
]