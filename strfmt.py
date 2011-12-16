import sys

def runFormat(fmt, args, rangeMode=False):
	if rangeMode:
		rangeFormat(fmt, args)
	else:
		normalFormat(fmt, args)

def normalFormat(fmt, args):
	print fmt % args

def rangeFormat(fmt, args):
	if '-' in args:
		#Assuming comma seperated list
		splitArgs = args.split('-')
		if len(splitArgs) != 2:
			print "Format arguments are in an invalid format for range use"
		for x in xrange(int(splitArgs[0]), int(splitArgs[1])+1):
			print fmt % x
	else:
		print "Format arguments are in an invalid format for range use"


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
