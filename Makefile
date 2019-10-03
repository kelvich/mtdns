FUNCLIB := /Users/stas/code/ton/crypto/smartcont

mtdns.fif: mtdns.fc
	func -PS -o mtdns.fif $(FUNCLIB)/stdlib.fc mtdns.fc

test:
	./test.fif