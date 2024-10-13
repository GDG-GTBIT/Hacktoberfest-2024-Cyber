opt=-O3 -Wall -std=c2x

all: clean altermac

altermac: altermac.o
	gcc ${opt} $^ -o $@

altermac.o:	altermac.c
	gcc ${opt} -c $^

clean:
	rm -f altermac *.o