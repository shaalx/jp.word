#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
class Word():
	"""Word japanese"""
	def __init__(self):
		# self.jap = jap
		self.word=""

	def __str__(self):
		return self.jap+"\t"+self.jch+"\t"+self.chi+"\t"+self.typ

	def settings(self,arg):
		if len(arg)<6:
			return False
		self.jch=arg[0]
		self.jap=arg[1]
		self.chi=arg[2]
		self.typ=arg[5]
		return True

	def cmp(self,word2):
		if self==word2:
			return False
		wj1=self.jap
		wj2=word2.jap		
		len1=len(wj1)
		len2=len(wj2)

		w1=[]
		w2=[]
		for i in wj1:
			w1.append(i)
		for i in wj2:
			w2.append(i)
		# print(w1,w2)
		s=0
		for i in w1:
			w1.remove(i)
			for j in w2:
				if i==j:
					s+=1
					w2.remove(j)
					break
					# print(w1[i],w2[j],sep='-',end='')
		if s>=3 or s>=1 and abs((len2+len1)/s)<=3.5:
			return True
		return False

	def show(self):
		print(self.jap,self.jch,self.chi,self.typ,sep='\t')

f=open("w.txt","r")
wordList=[]
for i in range(2805):
	line=f.readline()
	if len(line)<1:
		break
	splits=line.split('\t')
	w=Word()	
	if w.settings(splits):
		wordList.append(w)
	# print(len(splits),splits,end="\n")
f.close()

of=open("words.txt","a")
for x in wordList:
	wordList.remove(x)
	for y in wordList:
		if x.cmp(y)==True:
			# x.show()
			# y.show()
			# print()
			print(x,y,sep='\n',end='\n',file=of)
			print(sep='\n',end='\n',file=of)

