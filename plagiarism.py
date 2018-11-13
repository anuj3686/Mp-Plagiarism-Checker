from __future__ import division
import nltk, re, pprint , time
from nltk.stem.lancaster import LancasterStemmer
f1 = open('sample1.txt')
f2 = open('sample2.txt')
raw1 = f1.read()
raw2 = f2.read()

list_raw1 = raw1.split('.')
list_raw2 = raw2.split('.')
print(list_raw1)
list_tok1 = []
list_tok2 = []

for i in range(len(list_raw1)):
    list_tok1.append(nltk.word_tokenize(list_raw1[i].lower()))

for i in range(len(list_raw2)):
    list_tok2.append(nltk.word_tokenize(list_raw2[i].lower()))

list_pos1 = []
list_pos2 = []

for i in range(len(list_raw1)):
    list_pos1.append(nltk.pos_tag(list_tok1[i]))

for i in range(len(list_raw2)):
    list_pos2.append(nltk.pos_tag(list_tok2[i]))

st = LancasterStemmer()
print list_pos1
print list_pos2
#print (pos)
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#cp = nltk.RegexpParser(grammar)
#result = cp.parse(pos)
#print (result)
#result.draw()
list1 = []
list2 = []
for j in range(len(list_pos1)):
        list1 = []
        for i in range(len(list_pos1[j])):
            if list_pos1[j][i][1] == 'NN':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJ':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJR':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNS' :
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNP':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNPS' :
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'POS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RB':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBR':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'VB':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos1[j][i][0]))
        #    if list_pos1[j][i][1] == 'VBP':
         #       list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos1[j][i][0]))
        list2.append(list1)

list3 = []

for j in range(len(list_pos2)):
        list1 = []
        for i in range(len(list_pos2[j])):
            if list_pos2[j][i][1] == 'NN':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJ':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJR':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJS':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNS' :
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNP':
               list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNPS' :
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'POS':
               list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RB':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBR':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBS':
                list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'VB':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos2[j][i][0]))
            #if list_pos2[j][i][1] == 'VBP':
             #   list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos2[j][i][0]))
        list3.append(list1)


#print ("The words from document 1\n" ,list2)
#print ("The words from document 2\n" ,list3)


list4 = []
count = 0
count1 = 0
count2 = 0
for i in range(len(list2)):
    list4 = set(list2[i])
    count1 += len(list4)
    list5 = []
    list6 = []
    length = 0
    mlength = 0
    for j in range(len(list3)):
        list5 = set(list3[j])
        list6 = list4 & list5
        length = len(list6)
        if length > mlength:
            mlength = length
    count+=mlength
print(count1)
print(count)
a = count / count1
#b = count /count2
b = a 
x = ((a+b)/2)*100

print ("Percentage of plagiarsm :\n\t\t",x)
