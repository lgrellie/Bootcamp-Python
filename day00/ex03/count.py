import sys
import string

def text_analyzer(txt=""):
	if txt == "":
		txt = input("What is the text to analyze?\n")
	upper, lower, marks, spaces, total = 0, 0, 0, 0, 0
	for c in txt:
		upper += c.isupper()
		lower += c.islower()
		marks += c in string.punctuation
		spaces += c == ' '
		total += 1
	print("The text contains", total, "characters:")
	print("-", upper, "upper letters")
	print("-", lower, "lower letters")
	print("-", marks, "punctuation marks")
	print("-", spaces, "spaces")
