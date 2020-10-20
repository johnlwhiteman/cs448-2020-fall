#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void foo(const char *imagePath) {

    char *buffy = (char *)malloc(512 * sizeof(char));

    if (access(imagePath, F_OK) == -1) exit(1);

    printf("Opening %s\n", imagePath);

    FILE *fd = fopen(imagePath, "rb");

    fscanf(fd, "%s", buffy);

    fclose(fd);

    return;
}

int main(void) {

    foo("./buffy.c");

    return 0;
}
