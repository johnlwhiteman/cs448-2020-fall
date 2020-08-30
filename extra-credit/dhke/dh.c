#include <stdio.h>
#include <stdlib.h>

/******************************************************************
TODO: Student enter your DH key generation code here 
    Input:
        g: Base (must be relative root modulo to p)
        p: Modulus (must be prime and larger than g)
        secret: Alice's or Bob's
    Output:
        g^(secret)(mod p)
******************************************************************/
unsigned long calculateDhKey(int g, int p, int secret) {
    printf("ERROR: calculateDhKey() is NOT IMPLEMENTED\n");
    return 0;
}

/******************************************************************
TODO: Student enter e 
    Input: 
      n: Number to check 
    Output:
      0 if not prime; otherwise 1 
******************************************************************/
short isPrime(int n) {
    printf("ERROR: isPrime() is NOT IMPLEMENTED\n");
    return 0;
}

void showResult(int, int, 
                unsigned long, unsigned long,
                unsigned long, unsigned long,
                const char *);
void showUsage(void);

int main(int argc, char **argv) {

    /* Initial random numbers */
    unsigned int g, p, a, b = 0;

    /* Alice's and Bob's public keys respectively */
    unsigned long aPK, bPK = 0;

    /* Alice's and Bob's generated secret key respectively */
    unsigned long aSK, bSK = 0;
    
    if (argc != 5) {
        showUsage();
        printf("Abort: Incorrect usage\n");
        return 1;
    }

    g = atoi(argv[1]);
    p = atoi(argv[2]);
    a = atoi(argv[3]);
    b = atoi(argv[4]);

    if (!isPrime(p)) {
        printf("Abort: p is not prime: %i\n", p);
        return 1;
    }
    if (g >= p) {
        printf("Abort: g must be less than p: %i, %i\n", g, p);
        return 1;
    }

    /* TODO: Student you need to calculate Alice's and Bob's
             public keys, then use those keys to generate
             Alice's and Bob's secret keys which, of course,
             should be the same value. Multiple calls to
             calculateDhKey() with the correct parameters is
             all you need here assuming your implementation
             of it is correct */

    /* Generate public key exchange here */

    /* Calculate secret key here */

    /* Check to ensure secret is same */
    if (aSK != bSK) {
        showResult(g, b, aPK, bPK, aSK, bSK, "mismatch");
        return 1;
    }
    showResult(g, b, aPK, bPK, aSK, bSK, "ok");
    return 0;
}

/* Displays results */
void showResult(int g, int p, 
                unsigned long aPK, unsigned long bPK,
                unsigned long aSK, unsigned long bSK,
                const char *score) {
    printf(
"{\"g\":%i,\"p\":%i,\"aPK\":%lu,\"bPK\":%lu,\
\"aSK\":%lu,\"bSK\":%lu,\"keys\":\"%s\"}\n",
g, p, aPK, bPK, aSK, bSK, score);
}

/* Displays usage message */
void showUsage() {
    printf("\nUsage: dh g p a b\n\n\
  g: base (must be relative root modulo to p)\n\
  p: modulus (must be prime)\n\
  a: Alice's secret key\n\
  b: Bob's secret key\n\n");
} 
