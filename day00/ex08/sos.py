MORSE_CODE_DICT = {
	'A':'.-',
	'B':'-...',
	'C':'-.-.',
	'D':'-..',
	'E':'.',
	'F':'..-.',
	'G':'--.',
	'H':'....',
	'I':'..',
	'J':'.---',
	'K':'-.-',
	'L':'.-..',
	'M':'--',
	'N':'-.',
	'O':'---',
	'P':'.--.',
	'Q':'--.-',
	'R':'.-.',
	'S':'...',
	'T':'-',
	'U':'..-',
	'V':'...-',
	'W':'.--',
	'X':'-..-',
	'Y':'-.--',
	'Z':'--..',
	'1':'.----',
	'2':'..---',
	'3':'...--',
	'4':'....-',
	'5':'.....',
	'6':'-....',
	'7':'--...',
	'8':'---..',
	'9':'----.',
	'0':'-----'
	}

import sys

def encode(s):
	code = []
	for c in s:
		if c == ' ':
			code.append("/")
		elif c.isalpha():
			code.append(MORSE_CODE_DICT[c.upper()])
		elif c.isdigit():
			code.append(MORSE_CODE_DICT[c])
		else:
			return "ERROR"
	return " ".join(code)

if (len(sys.argv) > 1):
	codes = map(encode, sys.argv[1:])
	print(*codes, sep=" / ")
else:
	print("Usage: python sos.py \"SOS\"")	
