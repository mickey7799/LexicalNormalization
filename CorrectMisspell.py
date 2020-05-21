
import jellyfish
# 1. Levenshtein distance (LD)
# jellyfish.levenshtein_distance(u'jellyfish', u'smellyfish')
# 2. Damerau-Levenshtein distance (DLD)
# jellyfish.damerau_levenshtein_distance(u'jellyfish', u'jellyfihs')

import distance
# 3. Normalised Levenshtein Distance
# Levenshtein distance can be normalized,
# so that the results of several distance measures can be meaningfully compared.
# Two strategies are available for Levenshtein:
# either the length of the shortest alignment between the sequences is taken as factor,
# or the length of the longer one. Example uses:

import  ParsedTweet
import  Utility
import numpy as np
# from weighted_levenshtein import lev
import weighted_levenshtein

class CorrectMisspell:

    def __init__(self):
        self.p = ParsedTweet.ParsedTweet()
        self.correct_file = open("C:\\Users\\TingYuehShih\Downloads\\2019S1-proj1-data(Window)\\correctTheMispell.txt", "r+")

    def isWordInDict(self, word, words_in_dict):
        if word in words_in_dict:
            return True

    def writeWordHavinMinDistance(self, word, words_in_dict):
        min_dinstance = len(word)
        word_having_min_dinstance = ""
        for word_in_dict in words_in_dict:
            levenshtein_distance = jellyfish.levenshtein_distance(word, word_in_dict)
                # distance.levenshtein(word, word_in_dict)
            if levenshtein_distance < min_dinstance:
                word_having_min_dinstance = word_in_dict
                min_dinstance = levenshtein_distance
        # print(" correct " + word + " to " + word_having_min_dinstance)
        Utility.writeOutputFile(self.correct_file , word_having_min_dinstance)

if __name__ == "__main__":
    c = CorrectMisspell()

    for i in range(0, len( c.p.misspell_list)):
        word_in_tweet = c.p.misspell_list[i]

        if c.isWordInDict(word_in_tweet, c.p.dict_list):
            Utility.writeOutputFile(  c.correct_file, word_in_tweet)
        else:
            c.writeWordHavinMinDistance(word_in_tweet, c.p.dict_list)
