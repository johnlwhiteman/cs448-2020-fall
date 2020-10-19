CC=afl-gcc
CFLAGS=-I.
LIBS=-lm
.PHONY: clean

all: vigenere

vigenere: vigenere.c
	$(CC) -o vigenere $(CFLAGS) $^ $(LIBS)

encrypt: vigenere
	afl-fuzz -i in/encrypt -o ./out/encrypt ./vigenere -E -k ./in/key.txt -i @@ -o ./out/encrypt.txt

decrypt: vigenere
	afl-fuzz -i in/decrypt -o ./out/decrypt ./vigenere -D -k ./in/key.txt -i @@ -o ./out/decrypt.txt

clean:
	rm -f vigenere rm -fr ./out/encrypt/* ./out/decrypt/* 
