/* DELAY AFTER APPLYING SERIAL DEVICE SETTINGS */
#define INIT_DELAY 100000  /* uSec */

/* MAXIMUM STRING LENGTHS */
#define MAXREADCHARS 1024
#define MAXSENDCHARS 512
#define MAXFILECHARS 16

/* BOOLEAN DEFINITIONS */
#define TRUE  (1==1)
#define FALSE (0==1)
#define ON     TRUE
#define OK     TRUE
#define OFF    FALSE
#define ERROR  FALSE
#define IGNORE FALSE

/* EXIT CODES */
#define EXIT_OK      0
#define EXIT_ERROR  -1
#define EXIT_INTRPT 10

typedef struct {
  char *device;
  int baudrate;
  int databits;
  char parity;
  int stopbits;
  int xonxoff;
  int rtscts;
} tCommParms;

typedef struct {
  int dtr;
  int rts;
} tMdLines;

typedef int tRS232; /* serial device handle */

extern tRS232 rs232_open  (char const *, int);
extern int    rs232_init  (tRS232, tCommParms *, int);
extern int    rs232_mdlns (tRS232, tMdLines *, int);
extern int    rs232_send  (tRS232, char *, float, int, int);
extern void   rs232_wait  (float, int, int);
extern char   *rs232_read (tRS232, char *, int, int);
extern int    rs232_close (tRS232);