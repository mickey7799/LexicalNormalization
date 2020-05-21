import ngram
import ParsedTweet
import Utility
import jellyfish


class MatchSoundex:

    def __init__(self):
        self.p = ParsedTweet.ParsedTweet()
        self.match_soundex_file = open("\\2019S1-proj1-data(Window)\\MatchSoundex.txt", "r+")

    def get_match(self, dictList ,token):
        candidates = []
        candidatesGram = []
        bestMatch = ""

        soundex_token = jellyfish.soundex(token)

        candidates = [match for match in dictList if jellyfish.soundex(match) == soundex_token]

        if len(candidates) > 1:
            GramSet = ngram.NGram(candidates)
            candidatesGram = GramSet.search(token)
            if len(candidatesGram) > 0:
                bestMatch = candidatesGram[0][0]
        elif len(candidates) == 1:
            bestMatch = candidates[0]

        return bestMatch, candidates, candidatesGram


if __name__ == "__main__":
    m = MatchSoundex()

    for i in range(0, len( m.p.misspell_list)):
        word_in_tweet = m.p.misspell_list[i]
        # print(word_in_tweet)
        bestMatch, candidates, candidatesGram = m.get_match( m.p.dict_list, word_in_tweet)
        # print(bestMatch)
        # print(candidates)

        Utility.writeBestmatchAndCandidatesToOutputFile(m.match_soundex_file , bestMatch, candidates, candidatesGram)