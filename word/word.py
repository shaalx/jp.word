#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Word():
	"""Word japanese"""
	def __init__(self):
		# self.jap = jap
		self.word=""

	def __str__(self):
		return self.jap+self.jch+self.chi+self.typ

	def settings(self,*arg):
		self.jch=arg[0]
		self.jap=arg[1]
		self.chi=arg[3]
		self.typ=arg[5]


		