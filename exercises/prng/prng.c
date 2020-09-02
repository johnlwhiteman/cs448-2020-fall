#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv) {
    int i = 0;
    int seed = time(0);
    if (argc > 1) {
        seed = atoi(argv[1]);
    }
    srand(seed);
    printf("Seed: %i\n", seed);
    for (i = 1; i <= 5; i++) {
        printf("%d: %i\n", i, rand());
    }
    return 0;
}
