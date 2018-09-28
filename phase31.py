from gensim import models
model = models.Word2Vec.load('./model3.dat')
from os import listdir
import os
import re

tp=['neuralnetwork','datamin','kmean','matrix','neighbor','crf','hmm','lda','svm','knn','decisiontreebas','backprop','spade','tfidf','mergesort','c45tree','search','plsa','machinelearn','cluster','randomforest','network','markov','reinforcementlearn','cart','regressiontre','naivebay','minmax','graph','algorithm','method']

fp=['associ','accept','accuraci','research','refer','vari','facebook','stream','task','target','addit','time','inform','uncertainti','factor','detect','online','system','group','distance','vector','part','type','express','imag','springer','world','busin','news','problem','concept','dataset','databas','approach','method','success','algorithm','analysi','acmsymposium','ieee','evalu','process','model']
with open('true_positives', 'r') as f:
    for word in f.readlines():
        tp.append(word.strip())

with open('false_positives', 'r') as f:
    for word in f.readlines():
        fp.append(word.strip())
import csv
ifile= open("finaltokens.csv","rb")
reader = csv.reader(ifile)
import numpy
ct=0
path = "./Output/"
if not os.path.exists(path):
    os.makedirs(path)

pr1=0
pr2=0
#print model.similarity("cat","cat")
for fle, row in zip(listdir('Text'),reader):
	ct+=1
	ple=0
	f1 = open(path+fle[:-5]+"_tp","wa")
	f2 = open(path+fle[:-5]+"_fp","wa")
	#f3 = open(path+fle[:-5]+"_mc","wa")
	tokens=set()
	false_tokens=set()
	misc=set()
        #print row
        #f1.write(str(ct)+"\n")
        #f2.write(str(ct)+"\n")
        #f3.write(str(ct)+"\n")
	for col in row:
		if col.isdigit():
			continue
		if re.match(".*cid[0-9].*",col):
			continue
		isadd=0
		isfalseadd=0
		for entry in fp:
				#print "adds"
				#print entry,col
				print col,entry
				print numpy.linalg.norm(model[col] - model[entry])
				#print model.similarity(str(col),str(entry)) 
				try:
					print model.similarity(entry,col) 
					if model.similarity(entry,col)>0.50:
						false_tokens.add(col)
						isfalseadd=1
						break
                    		except:
					false_tokens.add(col)
					isfalseadd=1
					pass
		"""for entry in fp:
				try:
					if col.find(entry)!=-1:
						false_tokens.add(col)
						isfalseadd=1
						break
				except:
					pass
		"""
		if not isfalseadd:	
		 for entry in tp:
			#print model.similarity(entry,col) 
                	try:
				if model.similarity(entry,col)> 0.50:
					tokens.add(col)
					isadd = 1
					ple=1
					break
			except:
				pass
		 for entry in tp:
			try:
				if col.find(entry)!=-1:
					tokens.add(col)
					isadd=1
					ple=1
					break
			except:
				pass
			
		if not isadd and not isfalseadd:
			misc.add(col)
	if ple==0:
                #f1.write(x[0]+"\n")
		print ct
	pr1+=len(tokens)
	pr2+=len(false_tokens)+len(misc)
	f1.write(str(tokens)+"\n")	
	f2.write(str(false_tokens)+"\n\n")
	f2.write(str(misc)+"\n")
print pr1,pr2
print pr1/(pr1+pr2)

	
		
