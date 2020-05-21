import  jellyfish
import  ParsedTweet
import  Utility

class ConvertUsingSoundex:
    def __init__(self):
        self.p = ParsedTweet.ParsedTweet()
        self.tweet_soundex_file = open("\\2019S1-proj1-data(Window)\\tweetConvertedToSoundex.txt", "r+")
        self.dict_soundex_file = open("\\2019S1-proj1-data(Window)\\dictConvertedToSoundex.txt", "r+")

if __name__ == "__main__":
    c = ConvertUsingSoundex()

    for i in range(0, len( c.p.misspell_list)):
        word_in_tweet = c.p.misspell_list[i]
        wordConvertedToSoundex = jellyfish.soundex(word_in_tweet)
        Utility.writeOutputFile(c.tweet_soundex_file, wordConvertedToSoundex)

    for i in range(0, len( c.p.dict_list)):
        word_in_dict = c.p.dict_list[i]
        wordConvertedToSoundex = jellyfish.soundex(word_in_dict)
        Utility.writeOutputFile(c.dict_soundex_file, wordConvertedToSoundex)
