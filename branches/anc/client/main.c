#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <stdio.h>
#include <ctype.h>
#include <strings.h>
#include <unistd.h>

#define BAUDRATE B115200
#define MODEMDEVICE "/dev/ttyUSB0"
#define _POSIX_SOURCE 1 /* POSIX compliant source */
#define FALSE 0
#define TRUE 1

volatile int STOP=FALSE;

int  main()
{
  int fd,c, res;
  struct termios oldtio,newtio;
  char buf[255];

  fd = open(MODEMDEVICE, O_RDWR | O_NOCTTY ); 
  if (fd <0) {perror(MODEMDEVICE); return -1; }

  tcgetattr(fd,&oldtio); /* save current port settings */

  bzero(&newtio, sizeof(newtio));
  newtio.c_cflag = BAUDRATE | CRTSCTS | CS8 | CLOCAL | CREAD;
  newtio.c_iflag = IGNPAR;
  newtio.c_oflag = 0;
  /* set input mode (non-canonical, no echo,...) */
  newtio.c_lflag = 0;

  newtio.c_cc[VTIME]    = 0;   /* inter-character timer unused */
  newtio.c_cc[VMIN]     = 1;   /* blocking read until 5 chars received */
        
  tcflush(fd, TCIFLUSH);
  tcsetattr(fd,TCSANOW,&newtio);
        
        
  while (STOP==FALSE) {       /* loop for input */
    res = read(fd,buf,1);
    buf[res]=0;               /* so we can printf... */
    char c = buf[0];
    if (isprint(c))
    printf("%c\n", c);
    else
    printf("%02X\n", c);

  }
  tcsetattr(fd,TCSANOW,&oldtio);
}
