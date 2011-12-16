import sys

def runFormat(fmt, args):
	for arg in args:
		print fmt % arg

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: strfmt <format> <args>"
		sys.exit(1)
	else:
		runFormat(sys.argv[1], sys.argv[2:])
