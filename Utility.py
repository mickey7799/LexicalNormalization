import  simplejson

def readFileToList(file):
    word_list = file.readlines()
    word_list = [x.strip() for x in word_list]  # remove next line "\n"
    return word_list

def writeOutputFile(file, word):
    file.write(word + "\n")
    file.flush()

def writeBestmatchAndCandidatesToOutputFile(file, best, candidates, candidatesNgram):
    simplejson.dump(best, file)
    simplejson.dump(candidates, file)
    simplejson.dump(candidatesNgram, file)
    file.flush()
    file.write("\n")
    file.flush()