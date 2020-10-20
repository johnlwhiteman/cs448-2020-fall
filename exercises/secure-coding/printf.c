#include <stdio.h>
#include <string.h>

void sayHi(const char *name) {
	printf("Hi ");
	printf(name);
	printf("\n");
}

int main(int argc, char **argv) {
	char name[64];
	strncpy(name, argv[1], sizeof(name));
	sayHi(name);
	return 0;
}
