import sys

def runFormat(fmt, args):
	for arg in args:
		print fmt % arg

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="A command line string formatter")
	parser.add_argument('-r', 
	                    action="store_true", 
			    default=False,
			    help="run in range mode")
	parser.add_argument('-f',
	                    action="store"
			    help="string format")
	parser.add_argument('-a',
	                    action="store"
			    help="arguments for string format")
	parser.add_argument('-v', '--version', action='version')

	args = parser.parse_args(sys.argv)

	if len(sys.argv) < 3:
		print "Usage: strfmt <format> <args>"
		sys.exit(1)
	else:
		runFormat(sys.argv[1], sys.argv[2:])
