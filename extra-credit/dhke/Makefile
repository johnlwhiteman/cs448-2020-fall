CC=gcc
.PHONY: clean

all: dh

dh: dh.c
	gcc $< -o $@

test:
	python3 runLab.py

clean:
	rm -f dh results.json
