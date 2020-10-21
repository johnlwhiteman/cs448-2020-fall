#include <stdio.h>
#include <string.h>
#define MAX 7

int main(int argc, char **argv) {

    char password[MAX] = "secret";
    char attempt[MAX];

    if (argc < 2) return 1;

    strcpy(attempt, argv[1]);

    printf("Password: [%s]\n", password);
    printf("Attempt:  [%s]\n", attempt);

    if (0 == strncmp(attempt, password, MAX)) {
        printf("[PASS]: Passwords Match\n");
        return 0;
    }
    printf("[FAIL]: Passwords Don't Match\n");

    return 1;
}

