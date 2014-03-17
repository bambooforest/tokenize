"""
Create an initial orthography profile of Unicode grapheme clusters

Input should be UTF-8 plain text. 

Requires 3rd party module:

https://pypi.python.org/pypi/regex

"""

import sys
import codecs
import regex as re
import operator
import collections
import unicodedata

from tokenizer import Tokenizer

# input file
infile = codecs.open(sys.argv[1], "r", "utf-8")

# to remove a header uncomment
header = infile.readline()

# get all unicode cluster graphemes
grapheme_pattern = re.compile("\X", re.UNICODE)

# hash set of grapheme clusters
graphemes_dict = collections.defaultdict(int)

for line in infile:
    line = line.strip()
    # denormalize
    line = unicodedata.normalize("NFD", line)
    # match \X
    graphemes = grapheme_pattern.findall(line)
    # hash set em
    for grapheme in graphemes:
        graphemes_dict[grapheme] += 1

# evaluate every character in the document
sorted_graphemes = sorted(graphemes_dict.items(), key=operator.itemgetter(0))

for grapheme, frequency in sorted_graphemes:
    print(grapheme,"\t", frequency)

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
