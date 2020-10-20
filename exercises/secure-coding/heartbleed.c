#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 512

void showMemory(char *, long len);

int main(int argc, char **argv) {
    long responseLen = 0;
    char *response = NULL;

    if (argc < 3) {
        printf("heartbleed <string> <len>\n");
        return 1;
    }

    responseLen = atol(argv[2]);
    response = (char *)malloc(responseLen * sizeof(char));
    memcpy(response, argv[1], responseLen);
    showMemory(response, responseLen);
    return 0;
}

void showMemory(char *ptr, long len) {
    long i;
    printf("\n");
    for (i = 0; i < len; i++) {
        //printf("%.2x ", ptr[i]);
        printf("%c", ptr[i]);
    }
    printf("\n\n");
}
