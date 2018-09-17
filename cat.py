import ubinascii, sys

def cat_base64(fn):
	f = open(fn, 'rb')
	while True:
		c = ubinascii.b2a_base64(f.read())
		sys.stdout.write(c)
		sys.stdout.write("\n")
		if not len(c) or c == b'\n':
			break
	f.close()

def cat(fn):
	f = open(fn,'r')
	print(f.read())
	f.close()
