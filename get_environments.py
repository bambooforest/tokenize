"""
Get character environments given a list of words and a target character.

Input should be UTF-8 plain text, one word per line.

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

target_char = sys.argv[2]

# hash set of grapheme clusters
environs = collections.defaultdict(int)

for word in infile:
    word = word.strip()
    word = unicodedata.normalize("NFD", word)
    word = "#"+word+"#"
    indices = [i for i, ltr in enumerate(word) if ltr == target_char]

    for i in indices:
        print(word[1:-1], "\t", word[i-1]+"_"+word[i+1])
        environment = word[i-1]+"_"+word[i+1]
        environs[environment] += 1

# evaluate every character in the document
sorted_environs = sorted(environs.items(), key=operator.itemgetter(0))

for environment, frequency in sorted_environs:
    print(target_char, "\t", environment, "\t", frequency)
