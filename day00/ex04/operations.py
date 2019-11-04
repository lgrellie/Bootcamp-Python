import sys

args = sys.argv[1::]

def operations(a, b):
	print("Sum:\t\t", a + b)
	print("Difference:\t", a - b)
	try:
		print("Quotient:\t", a / b)
	except ZeroDivisionError:
		print("Quotient:\tERROR (div by zero)")
	try:
	 	print("Remainder:\t", a % b)
	except ZeroDivisionError:
		 print("Remainder:\tERROR (modulo by zero)")

if len(args) == 0:
	print("Usage: operations.py\nExample:\n\tpython operations.py 10 3")
elif len(args) > 2:
	print("InputError: too many arguments\nUsage: python operations.py")
	print("Example:\n\tpython operations.py 10 3")
elif len(args) < 2:
	print("InputError: too few arguments\nUsage: python operations.py")
	print("Example:\n\tpython operations.py 10 3")
else:
	try:
		operations(*map(int, args))
	except ValueError:
		print("ValueError: Arguments should be integers")
