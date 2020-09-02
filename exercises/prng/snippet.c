#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv) {
    int seed = time(0);
    if (argc > 1)
        seed = atoi(argv[1]);
    srand(seed);
    printf("%i\n", rand());
    return 0;
}
