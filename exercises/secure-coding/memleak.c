#include <stdlib.h>

int main(void) {
    int i;
    for (i = 0; i < 100; i++) {
        char *x = (char *)(malloc(i * 100));
    }
    return 0;
}
