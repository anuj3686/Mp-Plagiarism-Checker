from __future__ import division
from operator import itemgetter
import nltk, re, pprint , time
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from itertools import product
import string
from nltk.stem import PorterStemmer

from nltk.util import ngrams
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def simi(word1,word2):
	wordx, wordy = word1,word2
	sem1, sem2 = wn.synsets(wordx), wn.synsets(wordy)

	maxscore = 0
	for i,j in list(product(*[sem1,sem2])):
	  score = i.wup_similarity(j) # Wu-Palmer Similarity
	  maxscore = score if maxscore < score else maxscore
	return maxscore


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
#print list_pos1
#print list_pos2
#print (pos)
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#cp = nltk.RegexpParser(grammar)
#result = cp.parse(pos)
#print (result)
#result.draw()
list1 = []
list2 = []
noun1=[]
noun2=[]
vb1=[]
vb2=[]
ad1=[]
ad2=[]
aj1=[]
aj2=[]
for j in range(len(list_pos1)):
        list1 = []
        for i in range(len(list_pos1[j])):
            if list_pos1[j][i][1] == 'NN':
                list1.append(list_pos1[j][i][0])
		noun1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJ':
                list1.append(list_pos1[j][i][0])
		aj1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJR':
                list1.append(list_pos1[j][i][0])
		aj1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'JJS':
                list1.append(list_pos1[j][i][0])
		aj1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNS' :
                list1.append(list_pos1[j][i][0])
		noun1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNP':
                list1.append(list_pos1[j][i][0])
		noun1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'NNPS' :
                list1.append(list_pos1[j][i][0])
		noun1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'POS':
                list1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RB':
                list1.append(list_pos1[j][i][0])
		ad1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBR':
                list1.append(list_pos1[j][i][0])
		ad1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'RBS':
                list1.append(list_pos1[j][i][0])
		ad1.append(list_pos1[j][i][0])
            if list_pos1[j][i][1] == 'VB':
                list1.append(st.stem(list_pos1[j][i][0]))
		vb1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos1[j][i][0]))
		vb1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos1[j][i][0]))
		vb1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos1[j][i][0]))
		vb1.append(st.stem(list_pos1[j][i][0]))
        #    if list_pos1[j][i][1] == 'VBP':
         #       list1.append(st.stem(list_pos1[j][i][0]))
            if list_pos1[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos1[j][i][0]))
		vb1.append(st.stem(list_pos1[j][i][0]))
        list2.append(list1)

list3 = []

for j in range(len(list_pos2)):
        list1 = []
        for i in range(len(list_pos2[j])):
            if list_pos2[j][i][1] == 'NN':
                list1.append(list_pos2[j][i][0])
		noun2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJ':
                list1.append(list_pos2[j][i][0])
		aj2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJR':
                list1.append(list_pos2[j][i][0])
		aj2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'JJS':
                list1.append(list_pos2[j][i][0])
		aj2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNS' :
                list1.append(list_pos2[j][i][0])
		noun2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNP':
               list1.append(list_pos2[j][i][0])
	       noun2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'NNPS' :
                list1.append(list_pos2[j][i][0])
		noun2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'POS':
               list1.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RB':
                list1.append(list_pos2[j][i][0])
		ad2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBR':
                list1.append(list_pos2[j][i][0])
		ad2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'RBS':
                list1.append(list_pos2[j][i][0])
		ad2.append(list_pos2[j][i][0])
            if list_pos2[j][i][1] == 'VB':
                list1.append(st.stem(list_pos2[j][i][0]))
		vb2.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBD':
                list1.append(st.stem(list_pos2[j][i][0]))
		vb2.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBG':
                list1.append(st.stem(list_pos2[j][i][0]))
		vb2.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBN':
                list1.append(st.stem(list_pos2[j][i][0]))
		vb2.append(st.stem(list_pos2[j][i][0]))
            #if list_pos2[j][i][1] == 'VBP':
             #   list1.append(st.stem(list_pos2[j][i][0]))
            if list_pos2[j][i][1] == 'VBZ':
                list1.append(st.stem(list_pos2[j][i][0]))
		vb2.append(st.stem(list_pos2[j][i][0]))
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
#print(count1)
#print(count)

noun1=set(noun1)
noun2=set(noun2)
vb1=set(vb1)
vb2=set(vb2)
for i in noun1:
	for j in noun2:
		if i!=j and simi(i,j)>0.9:
 			print i,j,simi(i,j)
			count+=1
			noun2.remove(j)
			break
for i in vb1:
	for j in vb2:
		if i!=j and simi(i,j)>0.9:
			print i,j,simi(i,j)
			count+=1
			vb2.remove(j)
			break
for i in ad1:
	for j in ad2:
		if i!=j and simi(i,j)>0.9:
			print i,j,simi(i,j)
			count+=1
			ad2.remove(j)
			break
for i in aj1:
	for j in aj2:
		if i!=j and simi(i,j)>0.9:
			print i,j,simi(i,j)
			count+=1
			aj2.remove(j)
			break			

			


a = count / count1
#b = count /count2
b = a 
x = ((a+b)/2)*100

print ("Percentage of plagiarsm :\n\t\t",x) 







    
            
    
text1=raw1
text1=text1.lower()
text2=raw2
text2=text2.lower()

def pre_processing(text):
	sent_tokenize_list = sent_tokenize(text)
	#print sent_tokenize_list
	#print len(sent_tokenize_list)
	#tokenise words
	#print stop_words
	words=word_tokenize(text)
	stop_words = str(stopwords.words('english'))
	alpha=stop_words.replace("u'", "")
    #print words
        result = []
    #print alpha
    #remove stop words
        for item in words:
            if item not in alpha:
                result.append(item)
    #print "Filtered",result
        fil=str(result)
    #remove punctuation
        repstr=" " * 32
        table=string.maketrans(string.punctuation,repstr)
        s=fil.translate(table)
    #return s


    #lemmatizing
        lemmatizer=WordNetLemmatizer()
        h=lemmatizer.lemmatize(s)
    #print "Lemma",lemmatizer.lemmatize(s)
    #stemming
        wordss=word_tokenize(h)
        ps=PorterStemmer()
        list1=[]
        for i in wordss:
            k=(ps.stem(i))
            list1.append(k)
    #print list1
        final= '  '.join(list1)
        finall=str(final)
        return finall

def plagcheck(text1,text2):
        tex1=pre_processing(text1)
        tex2=pre_processing(text2)
        n=3
        trigrams1 = list(ngrams(tex1.split(), n))
        trigrams2 = list(ngrams(tex2.split(), n))
    #print trigrams1
    #print trigrams2
        def compare(trigrams1, trigrams2):
            common=[]
            for gram in trigrams1:
                if gram in trigrams2:
                    common.append(gram)
            return common
        a=compare(trigrams1,trigrams2)
        print "SIMILARITY",a
        print "intersection",len(a)
        print "ref file",len(trigrams1)
	ratio = len(a)/len(trigrams1)
        print "Ratio",len(a)/len(trigrams1)
	print ("Plag : ",(x+(ratio*x)/2))

plagcheck(text1,text2)  

