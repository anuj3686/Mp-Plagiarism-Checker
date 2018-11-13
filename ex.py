import nltk
import re
import sys
sentence = [("the", "DT"), ("littles", "JJ"), ("yellow", "JJ")] 
grammar = "NP: {<DT>?<JJ>*<NN>}" 
cp = nltk.RegexpParser(grammar) 
result = cp.parse(sentence) 


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

sys.stdout = Logger("yourlogfilename.txt")
of = open("ex.txt",'w')
print(result,file = of)


#print "hello"
