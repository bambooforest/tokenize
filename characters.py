"""
Create an initial orthography profile of Unicode grapheme clusters

Input should be UTF-8 plain text. 

Requires 3rd party module:

https://pypi.python.org/pypi/regex

"""

import sys
import codecs
import operator
import collections
import unicodedata

# input file
infile = codecs.open(sys.argv[1], "r", "utf-8")

# to remove a header uncomment
header = infile.readline()

# hash set of grapheme clusters
characters = collections.defaultdict(int)

for line in infile:
    line = line.strip()
    # denormalize
    line = unicodedata.normalize("NFD", line)

    for char in line:
        if not char == " ":
            characters[char] += 1

# evaluate every character in the document
sorted_characters = sorted(characters.items(), key=operator.itemgetter(1), reverse=True)

for character, frequency in sorted_characters:
    print(character,"\t", frequency, "\t", unicodedata.category(character), "\t", ord(character))

"""
def get_character_environments(self, char, string):
environs = {}
string = "# "+string+" #"
chars = string.split()
environ_index = chars.index(char)
environ = chars[environ_index-1]+"_"+chars[environ]+"_"+chars[environ+1]
if not environ in environs:
environs[environ] = 1
else:
environs[environ] += 1
"""
