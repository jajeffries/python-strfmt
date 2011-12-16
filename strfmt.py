import sys

def runFormat(fmt, args, rangeMode=False):
	for arg in args:
		print fmt % arg

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="A command line string formatter")
	parser.add_argument('-r',
	                    dest="rangeMode",
	                    action="store_true", 
			    default=False,
			    help="run in range mode")
	parser.add_argument('-f',
	                    dest="fmt",
	                    action="store",
			    help="string format")
	parser.add_argument('-a',
	                    dest="fmtArgs",
	                    action="store",
			    help="arguments for string format")
	parser.add_argument('-v', '--version', action='version')

	args = parser.parse_args(sys.argv[1:])

	runFormat(args.fmt, args.fmtArgs, args.rangeMode)
