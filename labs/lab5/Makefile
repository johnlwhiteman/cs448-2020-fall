.PHONY: clean

all: ticket 

ticket: ticket.c lottery.o
	gcc -Wall -o $@ lottery.o $<

clean:
	rm -f ticket
