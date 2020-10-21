#include <stdio.h>
#include <string.h>

#define B1_LEN 21
#define B2_LEN 5

void showAddresses(char *b1, char *b2) {
    printf("b1 length:     %i\n", B1_LEN);
    printf("b2 length:     %i\n", B2_LEN);
    printf("b1 address:    %p [%i]\n", (void *)b1, 0);
    printf("b2 address:    %p [%i]\n", (void *)b2, b2 - b1);
    printf("b2+%d address:  %p [%i]\n", B2_LEN, (void *)b2 + B2_LEN, b2 + B2_LEN - b1);
}

int main(int argc, char **argv) {
    char b1[B1_LEN] = "You can't change me!";
    char b2[B2_LEN];
    showAddresses(b1, b2);
    if (argc > 1) {
        strcpy(b2, argv[1]);
        printf("b1 value:      %s\n", b1);
        printf("b2 value:      %s\n", b2);
    }
}
