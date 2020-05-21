import  Utility

class Accuracy:
    def __init__(self):
        self.correctedTheMisspell_file = open("\\2019S1-proj1-data(Window)\\correctTheMispell.txt", "r")
        self.correctedTheMisspellList = Utility.readFileToList( self.correctedTheMisspell_file)
        self.correct_file = open("\\2019S1-proj1-data(Window)\\correct.txt", "r")
        self.correct_list = Utility.readFileToList(self.correct_file)
        self.correct_answer_count = 0

        for i in range( 0, len( self.correctedTheMisspellList)):
            correctedTheMisspellWord = self.correctedTheMisspellList[i]
            correctWord = self.correctedTheMisspellList[i]

            if correctedTheMisspellWord == correctWord:
                print(correctedTheMisspellWord + " matched the answer " + correctWord)
                self.correct_answer_count = self.correct_answer_count + 1
            else:
                print(correctedTheMisspellWord + " not  matched the answer " + correctWord)

if __name__ == "__main__":
    a = Accuracy()