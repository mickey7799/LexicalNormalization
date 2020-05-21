import  Utility

class ParsedTweet:

    def __init__(self):
        self.misspell_list = []
        self.correct_list = []
        self.read()

    def read(self):
        self.misspell_file = open("C:\\Users\\TingYuehShih\Downloads\\2019S1-proj1-data(Window)\\misspell.txt","r")
        self.misspell_list = Utility.readFileToList(self.misspell_file)

        self.dict_file = open("C:\\Users\\TingYuehShih\Downloads\\2019S1-proj1-data(Window)\\dict.txt", "r")
        self.dict_list = Utility.readFileToList(self.dict_file)

if __name__ == "__main__":
    r = ParsedTweet()
