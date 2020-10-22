#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    for (int i = 1; i <= 100; i++) {
        char *x = (char *)(malloc(i * 100));
        if (i % 25 == 0) {
            printf("Iterations: %i\n", i);
            sleep(1);
        }
    }
    return 0;
}
