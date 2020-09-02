.PHONY: clean all

all: prng snippet

prng: prng.c
	gcc $< -o $@ 

seed: prng
	./prng 

snippet: snippet.c 
	gcc $< -o $@ 

clean:
	rm -f prng snippet
