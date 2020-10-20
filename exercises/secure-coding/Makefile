.PHONY: all clean

all: buffy gets heartbleed memleak printf printfX

buffy: buffy.c
	gcc -g $< -o $@

gets: gets.c
	gcc -g $< -o $@

badmem: memleak.c
	gcc -g $< -o $@

heartbleed: heartbleed.c
	gcc -g $< -o $@

printf: printf.c
	gcc -g $< -o $@

printfX: printf.c
	gcc -Wno-format-extra-args -Wformat-security -g $< -o $@

clean:
	rm -f buffy gets heartbleed memleak printf printfX
