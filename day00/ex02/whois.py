import sys

if len(sys.argv) > 1:
	if len(sys.argv) == 2:
		try:
			arg = int(sys.argv[1])
			if arg % 2:
				print("I'm Odd.")
			else:
				print("I'm Even.")
		except ValueError:
			print("ERROR")
	else:
		print("ERROR")

