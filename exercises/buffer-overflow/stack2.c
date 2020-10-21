#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    int isAuthenticated = 0;
    char b[5];

    if (argc < 2) return 1;

    strcpy(b, argv[1]);

    printf("Input [%d]: %d\n", strlen(argv[1]),
                               isAuthenticated);

    if (isAuthenticated) {
        printf("ACCEPTED :)\n");
        return 0;
    }

    printf("REJECTED <:(\n");

    return 1;
}

