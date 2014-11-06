"""
Get character environments given input and a target character. Input should be UTF-8 plain text, one word per line. Use Py 3.
"""
import sys
import collections
import unicodedata

infile = open(sys.argv[1], "r")
target_char = sys.argv[2]
results = []
for line in infile:
    line = line.strip()
    line = unicodedata.normalize("NFD", line)
    line = "#"+line+"#"
    indices = [i for i, ltr in enumerate(line) if ltr == target_char]
    for i in indices:
        environment = line[i-1]+"_"+line[i+1]
        results.append(environment)
environments = collections.Counter(results)
for environ, count in environments.most_common():
    print('%s\t%7d' % (environ, count))


