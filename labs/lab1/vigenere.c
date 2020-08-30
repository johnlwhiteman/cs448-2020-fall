#include <stdio.h>
#include <unistd.h>

int decrypt(char *k, char *c, char *result);
int encrypt(char *k, char *p, char *result);
void showUsage(void);

int main(int argc, char **argv) {
    /* Add your code here */
    showUsage();
    return 0;
}

int decrypt(char *k, char *c, char *result) {
    /* Add your code here */
    return 1;
}

int encrypt(char *k, char *p, char *result) {
    /* Add your code here */
    return 1;
}

void showUsage() {

    printf("\nVigenère is a simple substitution cipher program\n");

    printf("\nUse Case: Argument-Based\
\n\nE(k,p): vigenere -e -k 'ktext' -i 'ptext'\
\nD(k,c): vigenere -d -k 'ktext' -i 'ctext'\n");

    printf("\nUse Case: File-Based\
\n\nE(k,p): vigenere -E -k 'kpath' -i 'ppath' -o 'cpath'\
\nD(k,c): vigenere -D -k 'kpath' -i 'cpath' -o 'ppath'\n\n");

}

