#include <stdio.h>

int main(int argc, char **argv) {
   char name[1];
   printf("What's your name: ");
   gets(name);
   printf("You entered: %s", name);
   return(0);
}
