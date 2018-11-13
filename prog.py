f=open('first.txt','r')
d=open('second.txt','r')

e=open('st.txt','r')
stop=fir=sec=list()

for a in e:
	temp=a.split()
	stop=temp+stop
	temp=list()

temp=list()

for a in f:
	temp=a.split()
	fir=temp+fir
	temp=list()
temp=list()

for a in d:
	temp=a.split()
	sec=temp+sec
	temp=list()

for a in fir:
	if a in stop:
		fir.remove(a)

for a in sec:
	if a in stop:
		sec.remove(a)

plag=0

for a in fir:
	for b in sec:
		if a==b:
			plag+=1

print (plag) #plag is number of common words
x=len(fir)+len(sec)
#print x
a=float(plag)/float(x)
print (a)

if a>0.5:
	print ('plagarism')
	


