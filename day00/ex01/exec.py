import sys

def convert(s):
	return (s[::-1].swapcase())

args = sys.argv[-1:0:-1]

if len(args):
	print(*map(convert, args))
