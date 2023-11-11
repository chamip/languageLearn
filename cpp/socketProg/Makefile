all: server client
CFLAGS=-O2 -Wall -W -std=c99

server: server.c
	$(CC) server.c -g -o server $(CFLAGS)

client:
	$(CC) client.c -g -o client $(CFLAGS)

clean:
	rm -f server
	rm -f client
