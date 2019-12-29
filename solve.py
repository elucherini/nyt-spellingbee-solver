import sys
import argparse
import re

def find_words(words, letters, required):
	print(letters)
	print(required)
	string = "".join(letters) + str(required)
	print(string)
	regex = re.compile("^[" + string + "]+$", re.IGNORECASE)
	req = re.compile(str(required), re.IGNORECASE)
	results = list()
	for w in words:
		if regex.match(w) and required in w and len(w) >= 4:
			results.append(w)	
	return results

def print_word_list(l):
	print("Found %d solutions in the English dictionary:" % (len(l)))
	for word in l:
		print(word)

filename = 'english-words/words_alpha.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-l','--letters', nargs=6, action='append', help='Letters', required=True)
parser.add_argument('-r', '--required', action='store', help='Required letter', required=True)
args = parser.parse_args()

words = [line.rstrip('\n') for line in open(filename)]

result = find_words(words, args.letters[0], args.required)
print_word_list(result)
