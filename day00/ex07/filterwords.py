import sys
import re
import string

args = sys.argv

if len(args) != 3:
	print("Usage: python filterwords.py \"Hello, my friend\" 3")
else:
	try:
		s = str(args[1])
		n = int(args[2])
		words = re.split('[ ' + string.punctuation + ']+', s)
		print([word for word in words if len(word) > n])
	except:
		print("ERROR")
