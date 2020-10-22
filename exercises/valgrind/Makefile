.PHONY: all clean

all: memleak

badmem: memleak.c
	gcc -g $< -o $@

clean:
	rm -f memleak
