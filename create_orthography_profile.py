"""
Script for generating information to create an initial orthography profile.

"""

__author__ = "Steven Moran"
__date__ = "November, 2013"

import sys
import codecs
import regex as re
import operator
import collections
import unicodedata


characters = collections.defaultdict(int)

def get_characters(infile):
    # Generate Unicode character unigram model
    outfile = codecs.open("op_unigrams_characters.txt", "w")
    header = "character"+"\t"+"frequency"+"\t"+"Unicode category"+"\t"+"decimal code"+"\n"
    outfile.write(header)

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
        result = character+"\t"+str(frequency)+"\t"+unicodedata.category(character)+"\t"+str(ord(character))+"\n"
        outfile.write(result)

    outfile.close()

def get_graphemes(infile):
    # Generate Unicode grapheme cluster unigram model
    # get all unicode cluster graphemes
    outfile = codecs.open("op_grapheme_clusters.txt", "w")
    header = "grapheme cluster"+"\t"+"frequency"+"\n"
    outfile.write(header)

    # hash set of grapheme clusters
    graphemes_dict = collections.defaultdict(int)
    grapheme_pattern = re.compile("\X", re.UNICODE)

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
        result = grapheme+"\t"+str(frequency)+"\n"
        outfile.write(result)

    outfile.close()

def get_grapheme_cluster_environments(infile):
    # Generate Unicode grapheme cluster enivronments
    pass


environs = collections.defaultdict(int)
def get_character_environments(infile, target_char):
    # Generate Unicode character environments

    outfile = codecs.open("op_character_environments.txt", "a")
    header = "character"+"\t"+"environment"+"\t"+"frequency"+"\n"
    outfile.write(header)

    for word in infile:
        word = word.strip()
        word = unicodedata.normalize("NFD", word)
        word = "#"+word+"#"

        indices = [i for i, ltr in enumerate(word) if ltr == target_char]

        for i in indices:
            # print(word[1:-1], "\t", word[i-1]+"_"+word[i+1])
            environment = word[i-1]+"_"+word[i+1]
            environs[environment] += 1

    # evaluate every character in the document
    sorted_environs = sorted(environs.items(), key=operator.itemgetter(0))

    for environment, frequency in sorted_environs:
        result = target_char+"\t"+environment+"\t"+str(frequency)+"\n"
        outfile.write(result)
        # print(target_char, "\t", environment, "\t", frequency)

    outfile.close()

if __name__=="__main__":
    # input file - remove header if there is one
    infile = codecs.open(sys.argv[1], "r", "utf-8")
    header = infile.readline()
    get_characters(infile)
    infile.close()

    infile = codecs.open(sys.argv[1], "r", "utf-8")
    header = infile.readline()
    get_graphemes(infile)
    infile.close()

    infile = codecs.open(sys.argv[1], "r", "utf-8")
    header = infile.readline()
    for char in characters:
        get_character_environments(infile, char)
    infile.close()









