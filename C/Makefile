CC = gcc
BINARY := hello-world
CFLAGS += -Wall -O0

.PHONY: all
all: $(BINARY)

$(BINARY): hello-world.o

.PHONE: clean
clean:
	-rm -f *.o $(BINARY)
