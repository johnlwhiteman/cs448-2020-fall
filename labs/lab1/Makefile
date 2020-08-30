.PHONY: clean

all: vigenere

test: test.py
	python3 ./test.py

sign: signCode
	./signCode

verify: verifySign 
	./verifySign

vigenere: vigenere.c
	gcc -Wall -o $@ $<
 
clean:
	rm -f vigenere sign.* *.pem *.pub *.bin *.sig *.256
