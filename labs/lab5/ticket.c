#include <stdio.h>

extern unsigned short authenticate(const char *pwd);
extern void getNumbers(unsigned short *);
extern void showNumbers(const unsigned short *);

int main(int argc, char **argv) {
    unsigned short numbers[6];
    if (argc < 2) {
        printf("Usage: %s <password>\n", argv[0]);
        return 1;
    }
    return 0;
}
