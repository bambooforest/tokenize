"""
Create (initial) orthography profiles. Input should be UTF-8 plain text. Use Py 3.
"""

import sys
import collections
import unicodedata
import regex as re
from tokenizer import Tokenizer

def create_profiles(path):
    infile = open(path, "r")
    characters = collections.Counter()
    graphemes = collections.Counter()
    grapheme_pattern = re.compile("\X", re.UNICODE)
    for line in infile:
        line = line.strip()
        line = unicodedata.normalize("NFD", line)
        # line = line.replace(" ", "") # todo: all white space
        characters.update(line)
        print(characters)
        graphs = grapheme_pattern.findall(line)
        graphemes.update(graphs)
        print(graphemes)

    with open("op_unicode_characters.tsv", "w") as f:
        for character, count in characters.most_common():
            f.write('%s\t%7d\n' % (character, count))
    f.close()

    with open("op_grapheme_clusters.tsv", "w") as f:
        for grapheme, count in graphemes.most_common():
            f.write('%s\t%7d\n' % (grapheme, count))
    f.close()

if __name__=="__main__":
    create_profiles(sys.argv[1])



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
