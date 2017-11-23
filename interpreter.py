# -*- coding: utf-8 -*-
import err
from time import sleep
from os import system
class interpreter(object):
	def __init__(self, codeSource):
			#Variables
		self.codeFile = open(codeSource, 'r')
		self.tempCode = self.codeFile.read()
		self.codeFile.close()
		self.tempCode = self.tempCode.split('\n')
		self.code = []

	def mov(self, l, d):
		print l
		#Movement
		#If going south
		if d == 2:
			l[1] += 1
		#If going north
		elif d == 0:
			l[1] -= 1
		#If going east
		elif d == 1:
			l[0] += 1
		#If going west
		elif d == 3:
			l[0] -= 1
		print l
		return l

	def run(self):
			##############
			#CODE LOADING#
			##############

		#Transforms into array of arrays from just an array
		for i in range(0, len(self.tempCode)):
			tempLine = []
			for x in self.tempCode[i]:
				tempLine.append(x)
			self.code.append(tempLine)

		#Finds the length of the longest list (width of code)
		codeWidth = 1
		for i in self.code:
			if len(i) > codeWidth:
				codeWidth = len(i)

		#Fills in with spaces so everything is the same width
		for i in range(0, len(self.code)):
			if len(self.code[i]) < codeWidth:
				diff = codeWidth - len(self.code[i])
			for s in range(0, diff):
				self.code[i].extend(" ")

			#############
			#INTERPRETER#
			#############
		#Variables
			#Direction
			#0 north
			#1 east
			#2 south
			#3 west
			#			N/0
			#			 |
			#	W/3 	 	E/1
			#		 	 |
			#			S/2
		dir = 2
			#Location
		loc = [0, 0]
			#Buffer
		buf = {"print":[], "if":[], "loop":[]}
			#Goto
		goto = [0, 0]
			#Font
		regu = '\033[0m'
		bold = '\033[0;37;42m'

		print """###########\n#EXECUTING#\n###########"""
		while True:
				#Printing code
			system("clear")
			for i in buf:
				if buf[i] != []:
					print i + ": " + str(buf[i])
			for y in range(0, len(self.code)):
				for x in range(0, len(self.code[y])):
					if [x,y] == loc:
						print bold + self.code[y][x] + regu,
					else:
						print self.code[y][x],
				print ""
			print "\n",
			print "─"*(codeWidth*2),
			print	"\n"

			loc = self.mov(loc, dir)
			print loc

			block = self.code[loc[1]][loc[0]]
				#Interpretation
			if (dir == 1) and (block == "("):
				goto = loc
				while block != ")":
					self.mov()
					buf["loop"][0] += block
			elif block == "^":
				dir = 0
			elif block == ">":
				dir = 1
			elif block == "v":
				dir = 2
			elif block == "<":
				dir = 3
			elif block == " ":
				err.errRet(01.1)
				break
			sleep(0.05)

		print """##########\n#FINISHED#\n##########"""
