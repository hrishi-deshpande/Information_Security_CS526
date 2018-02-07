CC = gcc
CFLAGS = -ggdb
XS = -z execstack
NOXS = -z noexecstack
CANARY = -fstack-protector

xs_sources = vulnerable1 vulnerable2 vulnerable3
noxs_canary_sources = vulnerable4 exploit1 exploit2 exploit3 exploit4

all: xs noxs_canary

xs:
	$(foreach source,$(xs_sources),$(CC) $(CFLAGS) $(XS) $(source).c -o $(source);)

noxs_canary:
	$(foreach source,$(noxs_canary_sources),$(CC) $(CFLAGS) $(NOXS) $(CANARY) $(source).c -o $(source);)

cp:
	cp vulnerable? /tmp/

clean:
	rm -f vulnerable? core exploit?

setuid: cp
ifeq ($(shell id -u),0)
	chown root:root /tmp/vulnerable?
	chmod 4755 /tmp/vulnerable?
else
	@echo "'make setuid' must be run as root -- use su or a root login!"
endif

