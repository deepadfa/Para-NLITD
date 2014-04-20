import Pmw
from Tkinter import *
import ttk
import tkMessageBox
import string
#import ply.lex as lex
#import lex
import re
import sys
#import cparse
#import ply.yacc as yacc
#import yacc

#from clex import tokens

import nltk
import Tkinter
import ScrolledText
from Tkconstants import *


from Tkinter import *
from tkFileDialog import askopenfilename
import re

from database_details import *
from adding_info import *
#import yacc

#import cparse, cvisitors, cx86

#import sys

#import re


root=Tk()


#mwww = Tkinter.Tk()
#mw=Toplevel()
#mw.withdraw()
root.withdraw()
root1=Toplevel()
root2=Toplevel()
root3=Toplevel()
root4=Toplevel()
root1.withdraw()
root2.withdraw()
root4.withdraw()



e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()
e12 = StringVar()
e13 = StringVar()
e14 = StringVar()
e15 = StringVar()
e16 = StringVar()

var = StringVar()
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
code={}
codes={}
regf={}
regl={}
grade=[]
grad=[]
graa=[]
gra=[]
sgpa=''	#require/not


import nltk
import re
import sys
import math
import MySQLdb as mdb
import re
conn=mdb.connect(host="localhost",user="root",passwd="aneesha123",db="transportation")
cursor=conn.cursor()

source=""
destination=""	
#tx=fc.readline()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#                              TO CAPITALIZE PLACE NAMES IF NOT ENTERED PROPERLY BY THE USER
#-----------------------------------------------------------------------------------------------------------------------------------------------

def capitalize():
	fc=open("prog.txt")# contains the question asked by the user
	gd=open("0oriplaces.txt")# contains the original set of places stored in the database
	tx=fc.readline()
	print tx
	
	while True:
		ty=gd.readline()
		if len(ty)<=1:
			break	
		print ty
		tz=ty.split()
		tz0=tz[0]	
		print tz[0]
		print tz0[1:]
		y=tz0[1:]
	#	if y in tx:
	#	res=re.findall(r""+y,tx)
	#		print "match found"
			
	#		u=tx.replace(y,tz0)
	#		print u
	#	print res
		tx = re.sub(r''' .'''+y," "+tz0,tx)
		print tx
		h=open("0orinput.txt","w")
		h.write(tx)
		h.close()
	fc.close()
	gd.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#					TO DO NAME ENTITY TAGGING IN THE QUESTION
#-----------------------------------------------------------------------------------------------------------------------------------------------

def netagging():
	#global tx
	#fc=open("0disinput.txt")
	#tx=fc.readline()
	#fc.close()
	
	
	
	b=open("0orinput.txt","r")
	v= b.readline()
	b.close()
	print "v=",v
	tok=nltk.word_tokenize(v)
	pos=nltk.pos_tag(tok)
	
	
	netag=nltk.ne_chunk(pos,binary=True)
	print netag
	
	d=open("0nextinput.txt","w")
	d.write(str(netag))
	d.close()


#-----------------------------------------------------------------------------------------------------------------------------------------------
#				TO CHECK WHETHER THE NAMED ENTITY IS A PLACE OR NAME
#				IF THE NE IS A PLACE, THEN WRITTEN TO FILE neplaces.txt
#				IF THE NE IS A NAME, THEN WRITTEN TO FILE nenames.txt
#-----------------------------------------------------------------------------------------------------------------------------------------------

def filecreation():
	uu=open("0nextinput.txt")
	xx=open("0neplaces.txt","w")
	yy=open("0nenames.txt","w")
	while True:
		gg=uu.readline()
		if len(gg)<=1:
			break
		gg=gg.replace("/"," ")
		print gg	
		if 'NE' in gg:
			print "NE found"
			list_of_words=nltk.word_tokenize(gg)
			print "list of words", list_of_words		
			next_word=list_of_words[list_of_words.index('NE')+1]
			print "next word",next_word
			ff=open("0oriplaces.txt","r")		
			while True:
				pp=ff.readline()
				if len(pp)<=1:
					break
				print "next word=",next_word
				print "pp=",pp
					
				if next_word in pp:
					print "matches"
					xx.write(next_word)
					xx.write('\n')
			ff.close()
			ff=open("0names.txt","r")		
			while True:
				pp=ff.readline()
				if len(pp)<=1:
					break
				print "next word=",next_word
				print "pp=",pp
				
				if next_word in pp:
					print "matches"
					yy.write(next_word)
					yy.write('\n')
			
	uu.close()
	xx.close()
	yy.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#						EXTRACT SOURCE AND DESTINATION
#-----------------------------------------------------------------------------------------------------------------------------------------------

class Check:
	def extract(self):
		flag1=0
		f=open("0orinput.txt");

		g=open("0myoutput.txt","w");
	
	
		while 1:
			stri=f.readline();
			list_of_words=nltk.word_tokenize(stri)
			e15=nltk.pos_tag(list_of_words)
			mystring=str(e15)
			g.write(mystring)
			if not stri:
				break
		g.close();
		h=open("0myoutput.txt","r")
	
		a=h.readline()
		print a
	
		print ('\n\n\n')
		result=a
		
		result=result.replace("[","")
		result=result.replace("]","")
		result=result.replace("(","")
		result=result.replace(")","")
		result=result.replace("'","")
		result=result.replace(",","")
		
		
		
		print result
		fla=0
		print ('\n\n\n')
		def fromreach():
			matchObj=re.match(r'(.*) from IN (.*) (.*) reach VB (.*) (.*) (.*)\?', result, re.M|re.I )
			blink=0
			if matchObj:
				fla=1
				print "matchObj.group() : ", matchObj.group()
				sourcetype=matchObj.group(3)
				print "source type found in the input : ", matchObj.group(3)
				destinationtype=matchObj.group(5)
				print "destination type found in the input : ", matchObj.group(5)
				blink=0
			else:
				print "No match found in the question format from **** to *****!!"
				matchObj=re.match(r'(.*) reach VB (.*) (.*) from IN (.*) (.*) (.*)\?', result, re.M|re.I )
		
				if matchObj:
					fla=1					
					print "Match found in the question format to **** from *****!!"
					print "matchObj1.group() : ", matchObj.group()
					sourcetype=matchObj.group(5)
					print "source type found in the input : ", matchObj.group(3)
					destinationtype=matchObj.group(3)
					print "destination type found in the input : ", matchObj.group(5)		
					#source=matchObj.group(4)
					#destination=matchObj.group(2)
					blink=1
				else:
					print "No match found in the question format from **** to *****!!"
		#------------------------------------------------------------------------------------------------------------------------------------------	
			if blink==0 : #The case when question is in from to format
	
				if sourcetype=='NNP':
					sourceguess=matchObj.group(2)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if sourceguess in mm:
							flag1=1
							print "flag1= 1 for source"
							self.source=sourceguess
					oo.close()
				else:	
					print "Source not found after from ";
			
				if destinationtype=='NNP':
					destinationguess=matchObj.group(4)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if destinationguess in mm:
							flag1=1
							print "flag1= 1 for destination"
							self.destination=destinationguess
					oo.close()
				else:	
					print "Destination not found after to ";
		
			if blink==1: #The case when question is in to from format
	
				if sourcetype=='NNP':
					sourceguess=matchObj.group(4)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if sourceguess in mm:
							flag1=1
							print "flag1= 1 for source"
							self.source=sourceguess
					oo.close()
				else:	
					print "Source not found after from ";
			
				if destinationtype=='NNP':
					destinationguess=matchObj.group(2)
					oo=open("0oriplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if destinationguess in mm:
							flag1=1
							print "flag1= 1 for destination"
							self.destination=destinationguess
					oo.close()
				else:	
					print "Destination not found after to ";
		def fromto():
			matchObj=re.match(r'(.*) from IN (.*) (.*) to TO (.*) (.*) (.*)\?', result, re.M|re.I )
		
			if matchObj:
				
				print "matchObj.group() : ", matchObj.group()
				sourcetype=matchObj.group(3)
				print "source type found in the input : ", matchObj.group(3)
				destinationtype=matchObj.group(5)
				print "destination type found in the input : ", matchObj.group(5)
				blink=0
			else:
				print "No match found in the question format from **** to *****!!"
				matchObj=re.match(r'(.*) to TO (.*) (.*) from IN (.*) (.*) (.*)\?', result, re.M|re.I )
		
				if matchObj:
					print "Match found in the question format to **** from *****!!"
					print "matchObj1.group() : ", matchObj.group()
					sourcetype=matchObj.group(5)
					print "source type found in the input : ", matchObj.group(3)
					destinationtype=matchObj.group(3)
					print "destination type found in the input : ", matchObj.group(5)		
					#source=matchObj.group(4)
					#destination=matchObj.group(2)
					blink=1
				else:
					print "No match found in the question format from **** to *****!!"
		#------------------------------------------------------------------------------------------------------------------------------------------	
			if blink==0: #The case when question is in from to format
	
				if sourcetype=='NNP':
					sourceguess=matchObj.group(2)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if sourceguess in mm:
							flag1=1
							print "flag1= 1 for source"
							self.source=sourceguess
					oo.close()
				else:	
					print "Source not found after from ";
			
				if destinationtype=='NNP':
					destinationguess=matchObj.group(4)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if destinationguess in mm:
							flag1=1
							print "flag1= 1 for destination"
							self.destination=destinationguess
					oo.close()
				else:	
					print "Destination not found after to ";
		
			if blink==1: #The case when question is in to from format
	
				if sourcetype=='NNP':
					sourceguess=matchObj.group(4)
					oo=open("0neplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if sourceguess in mm:
							flag1=1
							print "flag1= 1 for source"
							self.source=sourceguess
					oo.close()
				else:	
					print "Source not found after from ";
			
				if destinationtype=='NNP':
					destinationguess=matchObj.group(2)
					oo=open("0oriplaces.txt")
					while True:
						mm=oo.readline()
						if len(mm)<=1:
							break
						if destinationguess in mm:
							flag1=1
							print "flag1= 1 for destination"
							self.destination=destinationguess
					oo.close()
				else:	
					print "Destination not found after to ";
		#fromreach()
		#if fla==0:
		fromto()
		global source,destination
		source=self.source
		destination=self.destination
		print "The source is ",self.source
		print "The destination is ",self.destination
		dd=open("last.txt","w")
		dd.write("The source is : ")
		dd.write(self.source)
		dd.write("\nThe destination is : ")
		dd.write(self.destination)
		dd.close()


#----------------------------------------------------------------------------------------------------------------------------------------------
#                                        RETRIEVING DATA FROM THE DATABASE
#----------------------------------------------------------------------------------------------------------------------------------------------


	def retrieval(self):
		print ",,,,,,,,,,,,,,,,,,,,,,,koi,,,,,,,,,,,,,,,,,,,,,,,,,,,"
		def distancE():

			f=open("finaloutput.txt","w")
			f.write("The available distance is ")		
			a=cursor.execute("""select (distance) from distance where source=%s and destination=%s""",(self.source,self.destination))
			row=cursor.fetchall()			
			print "from retrieval a=",a
			if a!=0:	
				
				for a in row :
       					print a[0],"kilometers"
					z=str(a[0])
					f.write(z)
					f.write(" kilometers")
      			else:	
				v=cursor.execute("""select (distance) from distance where source=%s and destination=%s""",(self.destination,self.source))
				if v!=0:	
					row=cursor.fetchall()
					for v in row :
       						print v[0],"kilometers"
						z=str(v[0])
					f.write(z)
					f.write(" kilometers")
					f.close()
				else:
					f=open("finaloutput.txt","w")
					f.write("No entry found!! ")
					f.close()	
					
		
		def trainS():
		
			f=open("finaloutput.txt","w")
			f.write("The available train details: \n")		
			a=cursor.execute("""select E.trainname,E.trainid,B.traintime from traindetails as E, trains as B where E.trainid=B.trainid and  B.source=%s and B.destination=%s""",(self.source,self.destination))
			#a=cursor.execute("""select E.trainname,E.trainid,E.traintime from traindetails as E,trains as B where E.trainid=B.trainid and B.source='Ottapalam' and B.destination='Thrissur'""")
			row=cursor.fetchall()			
			#print "from retrieval a=",a
				
				
			for a in row :
				print "\n\nTrain id is",a[0]
				z=str(a[0])
				f.write("\n\n Train id =")
				f.write(z)
				y=str(a[1])
				f.write("\n Train name =")
				f.write(y)					
				x=str(a[2])
				f.write("\n Starting time from ")
				f.write(self.source)
				f.write(" ")
				f.write(x)
			f.close()					
				#f.write(" kilometers")
		
			if a==0:
				f=open("finaloutput.txt","w")
				f.write("No entry found!! ")
				f.close()
			sample3()				
		
		def buseS():
			
			def busfun1():			
				f=open("finaloutput.txt","w")
				f.write("The available bus details:\n ")		
				a=cursor.execute("""select E.busid,E.busname,B.start_time,B.reach_time from busdetails as E, buses as B where E.busid=B.busid and  B.source=%s and B.destination=%s""",(self.source,self.destination))
				#a=cursor.execute("""select E.trainname,E.trainid,E.traintime from traindetails as E,trains as B where E.trainid=B.trainid and B.source='Ottapalam' and B.destination='Thrissur'""")
				row=cursor.fetchall()			
				#print "from retrieval a=",a
	
	
				for a in row :
					print "Bus id is",a[0]
					z=str(a[0])
					f.write("\n\n Bus id =")
					f.write(z)
					y=str(a[1])
					f.write("\n Bus name =")
					f.write(y)					
					x=str(a[2])
					f.write("\n Starting time from ")
					f.write(self.source)
					f.write(" ")
					f.write(x)
				f.close()					
					#f.write(" kilometers")

				if a==0:
					f=open("finaloutput.txt","w")
					f.write("No entry found!! ")
					f.close()	

	
			
			
				
			f=open("0orinput.txt");
			strq=f.readline()
			f.close()
			tok=nltk.word_tokenize(strq)
			pos=nltk.pos_tag(tok)
			flag=0
			for x,y in pos:
				print "------------",x,y
				if x=="When":
					flag=1					
					a=cursor.execute("""select B.start_time from busdetails as E, buses as B where E.busid=B.busid and  B.source=%s and B.destination=%s""",(self.source,self.destination))
					row=cursor.fetchall()
					f=open("finaloutput.txt","w")
					f.write("The buses are avilable at:\n ")	
					for a in row :
						print "The buses are avilable at ",a[0]
						f.write(str(a[0]))
						f.write("\t")
					f.close()
			if flag==0:
				busfun1()
				sample3()
			else:
				sample33()
		def routE():
		
			f=open("finaloutput.txt","w")
			f.write("The available route is :\n")		
			a=cursor.execute("""select (route) from route where source=%s and destination=%s""",(self.source,self.destination))
			row=cursor.fetchall()			
			print "from retrieval a=",a
			if a!=0:	
				
				for a in row :
       					print a[0]
					z=str(a[0])
					f.write(z)
					#f.write(" kilometers")
      			else:	
				v=cursor.execute("""select (route) from route where source=%s and destination=%s""",(self.destination,self.source))
				if v!=0:	
					row=cursor.fetchall()
					for v in row :
       						print v[0]
						z=str(v[0])
						print "z=",z					
					matchObj=re.match(r'(.*)-->(.*)-->(.*)-->(.*)-->(.*)', z, re.M|re.I )
					
					if matchObj:
						f.write(matchObj.group(5)) 
						f.write('-->')

						f.write(matchObj.group(4)) 
						f.write('-->')

						f.write(matchObj.group(3)) 
						f.write('-->')

						f.write(matchObj.group(2)) 
						f.write('-->')

						f.write(matchObj.group(1)) 
						
					f.close()
				else:
					f=open("finaloutput.txt","w")
					f.write("No entry found!! ")
					f.close()	
					
			

		h=open("0orinput.txt","r")
		hh=h.readline()
		matchObj=re.match(r'(.*) distance (.*)', hh, re.M|re.I ) or re.match(r'(.*) long (.*)', hh, re.M|re.I )
		if matchObj:	
			distancE()
		else:
			print "Type of distance question not defined" 
		matchObj=re.match(r'(.*)train(.*)', hh, re.M|re.I ) or re.match(r'(.*)railway(.*)', hh, re.M|re.I )
		if matchObj:	
			trainS()
		else:
			print "Type of train question not defined" 
		matchObj=re.match(r'(.*)bus(.*)', hh, re.M|re.I )# or re.match(r'(.*)road(.*)', hh, re.M|re.I )
		if matchObj:	
			buseS()
		else:
			print "Type of bus question not defined" 
			
		matchObj=re.match(r'(.*)route(.*)', hh, re.M|re.I ) or re.match(r'(.*)way(.*)', hh, re.M|re.I )or re.match(r'(.*)reach(.*)', hh, re.M|re.I )
		if matchObj:
			print ",,,,,,,,,,,,,,,,,,,,, koiiiiiiiiiiiii 2,,,,,,,,,,,,,,,,,,,,"	
			routE()
		else:
			print "Type of route question not defined" 
				
	
		

def sample3():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Final Answer')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("finaloutput.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()
def sample33():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Final Answer')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("finaloutput.txt","r")
	grad=g.read()	
	g.close()
	def para1():
		para1gui()
		mw.destroy()
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = para1)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()
def para1gui():
	
	def fun():
		e4=e2.get()
		print "+++++++++++++++++++++++++++++  e4=",str(e4)
		if e4=="yes" or e4=="Yes":
			print "source is",source
			f=open("finaloutput.txt","w")
			f.write("The available bus details:\n ")		
			a=cursor.execute("""select E.busid,E.busname,B.start_time,B.reach_time from busdetails as E, buses as B where E.busid=B.busid and  B.source=%s and B.destination=%s""",(source,destination))
			#a=cursor.execute("""select E.trainname,E.trainid,E.traintime from traindetails as E,trains as B where E.trainid=B.trainid and B.source='Ottapalam' and B.destination='Thrissur'""")
			row=cursor.fetchall()			
			#print "from retrieval a=",a


			for a in row :
				print "Bus id is",a[0]
				z=str(a[0])
				f.write("\n\n Bus id =")
				f.write(z)
				y=str(a[1])
				f.write("\n Bus name =")
				f.write(y)					
				x=str(a[2])
				dd=str(a[3])
				f.write("\n Starting time from ")
				f.write(source)
				f.write(" ")
				f.write(x)
				f.write("\n Reaching time at ")
				f.write(destination)
				f.write(" ")
				f.write(dd)
			f.close()					
				#f.write(" kilometers")

			if a==0:
				f=open("finaloutput.txt","w")
				f.write("No entry found!! ")
				f.close()	

			sample3()
				
	master = Tk()
	master.title("Paraphrasing")
	master.geometry("600x300+10+10")
	master.option_add("*font", ("Arial", 15,  "normal"))	
	#w = Label(master, text="Welcome Administrator !")	
	Label(master, text="System :").grid(row=0)
	Label(master, text="Do you want details of the bus ?",bg="white").grid(row=0 ,column=3)
	Label(master, text="User   :").grid(row=2)
	global e1,e2
	#e1 = Entry(master)
	e2 = Entry(master)
	#e14=Entry(master)
	#e15=Entry(master)
	#e1="Do you want details of the bus ?"
	#e1.grid(row=0, column=1)
	e2.grid(row=2, column=3)
	print "e1=",e1 ,"e2=",e2
	#e3=e1.get()  
	
	e4=e2.get() 
	print "e3=",e3 ,"e4=",e4
	Button(master, text='OK', command=fun).grid(row=10, column=0, sticky=EW, pady=4)
	#Button(master, text='LOGIN', command=show_entry_fields).grid(row=10, column=1, sticky=EW, pady=4)
	#Button(master, text='CREATE NEW USER ACCOUNT', command=add_entry_fields).grid(row=8, column=2, sticky=EW, pady=4)

def tagging():

	tkMessageBox.showinfo("Message Box!", "Question Read")
	#e14 = StringVar()
	#e15 = StringVar()
	#grade=[]
	
	#grade=e14.get()	
	#f=open("0disinput.txt","w")
	#f.write(grade)	
	#print "grade=",grade
	#f.close()
	capitalize()
	netagging()
	filecreation()
	s= Check()
	s.extract()
	s.retrieval()
	#tex = nltk.word_tokenize(grade)
	#e15=nltk.pos_tag(tex)
	#mystring=str(e15)
	#f=open("try.txt","w")
	#f.write(mystring)
	#f.close()
	sample3()
	#tkMessageBox.showinfo("Message Box!", "question read.....")
	#mainloop()

def ffcapitalize():
	capitalize()
	sample4()

def ffnetagging():
	netagging()
	sample5()

def fffilecreation():
	filecreation()
	sample6()

def ffcheck():
	s=Check()
	s.extract()
	sample7()
	

def sample7():
	"""
	m = Tkinter.Tk()	
	tkMessageBox.showinfo("Message Box!", "sample7.....")
	m.option_add("*font", ("Arial", 8, "normal"))
	m.title('EXTRACTED SOURCE AND DESTINATION')
	m.geometry("+373+262")
	txt = ScrolledText.ScrolledText(m,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("last.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(m= "OK", command = m.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	m.mainloop()


	"""
	mwwwww = Tkinter.Tk()
	mwwwww.option_add("*font", ("Arial", 8, "normal"))
	mwwwww.title('EXTRACTED SOURCE AND DESTINATION')
	mwwwww.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mwwwww,
		                        background = 'white',
		                        width = 80,
		                        height = 20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	file = open("last.txt","r")
	grad=file.read()
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mwwwww, text = "Ok", command = mwwwww.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mwwwww.mainloop()


def sample6():
	
	mwwww = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample6.....")
	mwwww.option_add("*font", ("Arial", 8, "normal"))
	mwwww.title('NE Places Found')
	mwwww.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mwwww,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("0neplaces.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mwwww,text= "OK", command = mwwww.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mwwww.mainloop()
	"""
	mwwwww = Tkinter.Tk()
	mwwwww.option_add("*font", ("Arial", 8, "normal"))
	mwwwww.title('EXTRACTED SOURCE AND DESTINATION')
	mwwwww.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mwwwww,
		                        background = 'white',
		                        width = 150,
		                        height = 30,
		                        font = ("Arial", 8, "normal"))
	txt.pack()
	file = open("last.txt","r")
	grad=file.read()
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mwwwww, text = "Ok", command = mwwwww.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mwwwww.mainloop()
	"""
	
def sample4():
	mww = Tkinter.Tk()	
	#tkMessageBox.showinfo("Message Box!", "sample4.....")
	mww.option_add("*font", ("Arial", 8, "normal"))
	mww.title('Capitalize')
	mww.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mww,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("0orinput.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mww,text= "OK", command = mww.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mww.mainloop()

def sample5():
	mwww = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample5.....")
	mwww.option_add("*font", ("Arial", 8, "normal"))
	mwww.title('Named Entity Tag')
	mwww.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mwww,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("0nextinput.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mwww,text= "OK", command = mwww.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mwww.mainloop()

def show_entry_fields():
	
	e3=e1.get()  
	e4=e2.get() 

	print e3 
 	print e4
	print("user Name: %s\npassword: %s" % (e3, e4))
   	a="select * from userlogin "
	cursor.execute(a)
	#print "-----------a---------",a
	row=cursor.fetchall()
	for a in row :
       		print a
	
	d= cursor.execute("""select password from userlogin where username=%s """,(str(e3)),)
	
	if d==0:
		print "Invalid username"
		tkMessageBox.showinfo("Message Box!", "Invalid Username")
				
		#ch=raw_input('If you want to create new account press 1:')
		#if ch=='1':
		#	print"creating new user account"
		#	cursor.execute("""insert into userlogin (username,password) values(%s,%s) """,(e3,e4),)
		#	a="select * from userlogin "
		#	cursor.execute(a)
		#	row=cursor.fetchall()
		#	for a in row :
       		#		print a
		
	else:
		st=str(cursor.fetchone()[0])
		print st
		if e4==st:
			print "login successful"
			tkMessageBox.showinfo("Message Box!", "Successful Login!")
			main()
			#main_entry()
		else:
			print "password incorrect"	
			tkMessageBox.showinfo("Message Box!", "Incorrect Password!")






def show_entry_fieldad():
	
	e3=e1.get()  
	e4=e2.get() 

	print e3 
 	print e4
	print("Admin Name: %s\nPassword: %s" % (e3, e4))
   	a="select * from adminlogin "
	cursor.execute(a)
	row=cursor.fetchall()
	for a in row :
       		print a
	
	d= cursor.execute("""select adminpassword from adminlogin where adminname=%s """,(str(e3)),)
	
	if d==0:
		print "Invalid Admin Name"
		tkMessageBox.showinfo("Message Box!", "Invalid Admin Name")
				
		#ch=raw_input('If you want to create new account press 1:')
		#if ch=='1':
		#	print"creating new user account"
		#	cursor.execute("""insert into userlogin (username,password) values(%s,%s) """,(e3,e4),)
		#	a="select * from userlogin "
		#	cursor.execute(a)
		#	row=cursor.fetchall()
		#	for a in row :
       		#		print a
		
	else:
		st=str(cursor.fetchone()[0])
		print st
		if e4==st:
			print "login successful"
			tkMessageBox.showinfo("Message Box!", "Successful Login!")
			maiin()
			#main_entry()
		else:
			print "password incorrect"	
			tkMessageBox.showinfo("Message Box!", "Incorrect Password!")







def add_entry_fields():
			
			e3=e1.get()  
			e4=e2.get() 
			flag=0
			
			a="select * from userlogin "
			cursor.execute(a)
			row=cursor.fetchall()
			for a in row :
       				print a


			
			uname="select username from userlogin"
			cursor.execute(uname)

			row=cursor.fetchall()
			for uname in row :
					print uname[0]
					
					if e3==uname[0]:
						
						print "username already exist"
						tkMessageBox.showinfo("Message Box!", "Username Already Exist!")
			 			flag=1
						break

			
			if flag==0:#---------If the username not already present--------
		
					cursor.execute("""insert into userlogin (username,password) values(%s,%s) """,(e3,e4),)	
					conn.commit()					
					#print uname			
					print "New user added successfully"
					tkMessageBox.showinfo("Message Box!", "New User Added Succesfully!")
					a="select * from userlogin "
					cursor.execute(a)
					row=cursor.fetchall()
					for a in row :
       						print a
					#tkMessageBox.showinfo("Message Box!", "Successfully registered!")
							

#----------------------------------------------------------------------------------------------------------------------------------------------
#                                                     TKINTER DISPLAY FUNTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------

class mywidgets:
	root3.withdraw()
	#file = open("compileres.txt","w")
	#file.close()
	def __init__(self,root3):
		frame=Frame(root3)
		self.top(frame)
		#Entry(root3,bd=5,textvariable=e14).grid(ipadx=100,ipady=100, column=2,row=1)
		self.makeMenuBar(frame)
		
		self.Demo(frame)
		frame.pack()
		return
	
	def top(self,frame):
		frame.option_add("*font", ("Arial", 15,  "normal"))
#		frame.option_add("*fontcolor", ("blue"))
		Label(frame,text='Welcome to Para-NLITD',background='pink',pady=100,padx=525).pack(pady=0,padx=0)
		
		return
	#defines the text area
	title = 'Pmw.ScrolledText'
	import sys
	sys.path[:0] = ['../../..']



	import string
	import Tkinter
	import Pmw

	class Demo:
	    def __init__(self, frame):

		# Create the ScrolledText .
		fixedFont = Pmw.logicalfont('Fixed')
	       	self.st = Pmw.ScrolledText(frame,
			labelpos = 'nw',
			label_text='What to do?',


			usehullsize = 1,
			hull_width = 200,
			hull_height = 345,
			text_wrap='none',
#			text_font = fixedFont,
			text_font = "Arial",

			text_padx = 0,
			text_pady = 0,
		)
		self.st.importfile('whattodo.txt');
		self.st.pack(padx = 0, pady = 0, fill = 'both', expand = 1)

		# Prevent users' modifying text and headers
		self.st.configure(
		    text_state = 'disabled',

		)

	######################################################################

	# Create demo in root window for testing.
	if __name__ == '__main__':
#	    root = Tkinter.Tk()
#	    Pmw.initialise(root)
#	    root.title(title)

#	    exitButton = Tkinter.Button(root, text = 'Exit', command =
#	root.destroy)
#	    exitButton.pack(side = 'bottom')
	    widget = Demo(root)
#	    root.mainloop()


	def txtfr(self,frame):
		textfr = Frame(frame)
#		self.text = Text(textfr,height = 44,width = 185,background='white')
		self.text = Text(textfr,height = 30,width = 160,background='white')
		#Entry(root3,bd=5,textvariable=e14).grid(ipadx=100,ipady=100, column=2,row=1)
		scroll = Scrollbar(textfr)
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return
	
	def makeMenuBar(self,frame):
		frame.option_add("*font", ("Arial", 11,  "normal"))
		menubar = Frame(frame,relief = RAISED,borderwidth = 2)
		menubar.pack()
		
		mb_phases = Menubutton(menubar,text = 'STAGES')
		mb_phases.pack(side = LEFT)
		mb_phases.menu = Menu(mb_phases)
		mb_phases.menu.add_command(label = 'FINAL ANSWER',command = tagging)
		mb_phases.menu.add_command(label = 'CAPITALIZE',command = ffcapitalize)
		mb_phases.menu.add_command(label = 'NAMED ENTITY TAG',command = ffnetagging)
		mb_phases.menu.add_command(label = 'NE PLACES FOUND',command = fffilecreation)
		mb_phases.menu.add_command(label = 'EXTRACT SOURCE DESTINATION',command = ffcheck)
		"""
		mb_exit = Menubutton(menubar,text = 'EXIT')
		mb_exit.pack(side = LEFT)
		mb_exit.menu = Menu(mb_exit)
		"""
		global root3
		#mb_exit.menu.add_command(label = 'QUIT',command = usergui)
		#mb_file['menu'] = mb_file.menu
		mb_phases['menu'] = mb_phases.menu
 		#mb_exit['menu'] = mb_exit.menu
		return
	

class mywidget:
	root3.withdraw()
	#file = open("compileres.txt","w")
	#file.close()
	def __init__(self,root3):
		frame=Frame(root3)
		self.top(frame)
		#Entry(root3,bd=5,textvariable=e14).grid(ipadx=100,ipady=100, column=2,row=1)
		#self.makeMenuBar(frame)
		
		self.Demo(frame)
		#self.button(frame)		
		frame.pack()
		return
	
	def top(self,frame):
		frame.option_add("*font", ("Arial", 19,  "normal"))
#		frame.option_add("*fontcolor", ("blue"))
		Label(frame,text='Welcome to Para-NLITD',background='pink',pady=100,padx=525).pack(pady=0,padx=0)
		
		return
	#def button(self,frame):
		
	#defines the text area
	title = 'Pmw.ScrolledText'
	import sys
	sys.path[:0] = ['../../..']



	import string
	import Tkinter
	import Pmw

	class Demo:
	    def __init__(self, frame):

		# Create the ScrolledText .
		fixedFont = Pmw.logicalfont('Fixed')
	       	self.st = Pmw.ScrolledText(frame,
			labelpos = 'nw',
			label_text='Description of the System',


			usehullsize = 1,
			hull_width = 210,
			hull_height = 245,
			text_wrap='none',
#			text_font = fixedFont,
			text_font = "Arial",

			text_padx = 0,
			text_pady = 0,
		)
		self.st.importfile('description.txt');
		self.st.pack(padx = 0, pady = 0, fill = 'both', expand = 1)

		# Prevent users' modifying text and headers
		self.st.configure(
		    text_state = 'disabled',

		)

	######################################################################

	# Create demo in root window for testing.
	if __name__ == '__main__':
#	    root = Tkinter.Tk()
#	    Pmw.initialise(root)
#	    root.title(title)

#	    exitButton = Tkinter.Button(root, text = 'Exit', command =
#	root.destroy)
#	    exitButton.pack(side = 'bottom')
	    widget = Demo(root)
#	    root.mainloop()


	def txtfr(self,frame):
		textfr = Frame(frame)
#		self.text = Text(textfr,height = 44,width = 185,background='white')
		self.text = Text(textfr,height = 30,width = 160,background='white')
		#Entry(root3,bd=5,textvariable=e14).grid(ipadx=100,ipady=100, column=2,row=1)
		scroll = Scrollbar(textfr)
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return
	
	
	
	
def main():
	def callback():
		f=open("prog.txt","w")
		k=e.get()
		f.write(str(k))
		f.close()
		tagging()
	root3 = Tk()

	k = mywidgets(root3)
	e = Entry(root3,width=100,bd=25,textvariable=e14)
	#e.pack()

	b1 = Button(root3,text="OK",command=callback)
	b1.pack()
	e.pack()
	b2 = Button(root3,text="EXIT",command=root3.destroy)
	b2.pack()
	
	#Label(root3,text='Enter the question',background='pink',pady=100,padx=45).pack(pady=50,padx=10)
	root3.title('Para-NLITD')
	root3.mainloop()
#main()

def usergui():
	master = Tk()
	master.title("User_Login")
	master.geometry("600x500+10+10")	
	Label(master, text="user Name").grid(row=0)
	Label(master, text="password").grid(row=2)
	global e1,e2
	e1 = Entry(master)
	e2 = Entry(master,show ="*")
	#e14=Entry(master)
	#e15=Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=2, column=1)
	print "e1=",e1 ,"e2=",e2
	e3=e1.get()  
	e4=e2.get() 
	print "e3=",e3 ,"e4=",e4
	Button(master, text='QUIT', command=master.destroy).grid(row=10, column=0, sticky=EW, pady=4)
	Button(master, text='LOGIN', command=show_entry_fields).grid(row=10, column=1, sticky=EW, pady=4)
	#Button(master, text='CREATE NEW USER ACCOUNT', command=add_entry_fields).grid(row=8, column=2, sticky=EW, pady=4)

def maiin():
	master = Tk()
	master.title("Admin_Login")
	master.geometry("600x500+10+10")	
	#Label(master, text="user Name").grid(row=0)
	#Label(master, text="password").grid(row=2)
	#global e1,e2
	#e1 = Entry(master)
	#e2 = Entry(master,show ="*")
	#e14=Entry(master)
	#e15=Entry(master)
	#e1.grid(row=0, column=1)
	#e2.grid(row=2, column=1)
	#print "e1=",e1 ,"e2=",e2
	#e3=e1.get()  
	#e4=e2.get() 
	#print "e3=",e3 ,"e4=",e4
	master.option_add("*font", ("Arial", 15,  "normal"))	
	w = Label(master, text="Welcome Administrator !")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()	
	b2=Button(master, text=' ADD OR VIEW INFORMATION ', command=add_view_info_gui)
	b2.pack()	
	b3=Button(master, text='CREATE NEW USER ACCOUNT', command=postmaiin)
	b3.pack()
	b1=Button(master, text='QUIT', command=master.destroy)
	b1.pack()
def add_view_info_gui():
	master = Tk()
	master.title("Para-NLITD")
	master.geometry("600x500+10+10")	
	#Label(master, text="user Name").grid(row=0)
	#Label(master, text="password").grid(row=2)
	#global e1,e2
	#e1 = Entry(master)
	#e2 = Entry(master,show ="*")
	#e14=Entry(master)
	#e15=Entry(master)
	#e1.grid(row=0, column=1)
	#e2.grid(row=2, column=1)
	#print "e1=",e1 ,"e2=",e2
	#e3=e1.get()  
	#e4=e2.get() 
	#print "e3=",e3 ,"e4=",e4
	master.option_add("*font", ("Arial", 15,  "normal"))	
	w = Label(master, text="Select One Option !")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()	
	b2=Button(master, text='  VIEW DATABASE  ', command=view_info_gui)
	b2.pack()	
	b3=Button(master, text='ADD INFORMATION', command=add_info_gui)
	b3.pack()
	b1=Button(master, text='QUIT', command=master.destroy)
	b1.pack()
def add_info_gui():
	def addinfo():
			f=open("addinfo.txt","w")
			k=e.get()
			f.write(str(k))
			f.close()
			text_split()
	master = Tk()
	master.title("Para-NLITD")
	master.geometry("900x900+10+10")	
	
	master.option_add("*font", ("Arial", 15,  "normal"))	
	w = Label(master, text="Please enter the information you want to enter !")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()	
	e = Entry(master,width=100,bd=25,textvariable=e16)
	#e.pack()
	
	b1 = Button(master,text="OK",command=addinfo)
	b1.pack()
	e.pack()
	b2 = Button(master,text="EXIT",command=master.destroy)
	b2.pack()
	
	#Label(root3,text='Enter the question',background='pink',pady=100,padx=45).pack(pady=50,padx=10)
	master.title('Para-NLITD')

def addinfo():
		f=open("addinfo.txt","w")
		k=e.get()
		f.write(str(k))
		f.close()
		

def view_info_gui():
	master = Tk()
	master.title("Para-NLITD")
	master.geometry("900x900+10+10")	
	
	master.option_add("*font", ("Arial", 15,  "normal"))	
	w = Label(master, text="Database Tables !")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	w = Label(master, text="                      ")
	w.pack()
	"""
	b2=Button(master, text='    DISTANCE  ', command=show_distance)
	b2.pack()	
	b3=Button(master, text=' TRAINS ', command=show_trains)
	b3.pack()
	b6=Button(master, text='TRAINDETAILS', command=show_traindata)
	b6.pack()
	b4=Button(master, text=' BUSES ', command=show_buses)
	b4.pack()	
	b5=Button(master, text='ROUTES', command=show_routes)
	b5.pack()
	b1=Button(master, text='QUIT', command=master.destroy)
	b1.pack()
	"""
	b2=Button(master, text='   DISTANCE     ', command=show_distance)
	b2.pack()	
	b3=Button(master, text='      TRAINS       ', command=show_trains)
	b3.pack()
	b6=Button(master, text='TRAIN DETAILS', command=show_traindata)
	b6.pack()
	b4=Button(master, text='      BUSES        ', command=show_buses)
	b4.pack()
	b7=Button(master, text=' BUS DETAILS   ', command=show_bus_data)
	b7.pack()	
	b5=Button(master, text='     ROUTES      ', command=show_route)
	b5.pack()
	b1=Button(master, text='        QUIT         ', command=master.destroy)
	b1.pack()



def postmaiin():
	master = Tk()
	master.title("Para-NLITD")
	master.geometry("600x500+10+10")	
	Label(master, text="user Name").grid(row=0)
	Label(master, text="password").grid(row=2)
	global e1,e2
	e1 = Entry(master)
	e2 = Entry(master,show ="*")
	e14=Entry(master)
	e15=Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=2, column=1)
	print "e1=",e1 ,"e2=",e2
	e3=e1.get()  
	e4=e2.get() 
	print "e3=",e3 ,"e4=",e4
	Button(master, text='CREATE NEW USER ACCOUNT', command=add_entry_fields).grid(row=8, column=2, sticky=EW, pady=4)
	Button(master, text='QUIT', command=master.destroy).grid(row=10, column=2, sticky=EW, pady=4)

def admingui():


	master = Tk()
	master.title("Admin_Login")
	master.geometry("600x500+10+10")
	master.option_add("*font", ("Arial", 10,  "normal"))		
	Label(master, text="Admin Name").grid(row=0)
	Label(master, text="Password").grid(row=2)
	global e1,e2
	e1 = Entry(master)
	e2 = Entry(master,show ="*")
	#e14=Entry(master)
	#e15=Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=2, column=1)
	print "e1=",e1 ,"e2=",e2
	e3=e1.get()  
	e4=e2.get() 
	print "e3=",e3 ,"e4=",e4
	Button(master, text='QUIT', command=master.destroy).grid(row=6, column=0, sticky=W, pady=4)
	Button(master, text='LOGIN', command=show_entry_fieldad).grid(row=7, column=0, sticky=W, pady=4)
	#Button(master, text='CREATE NEW USER ACCOUNT', command=add_entry_fields).grid(row=8, column=2, sticky=W, pady=4)


def mainpage():
	master = Tk()
	master.title("Para-NLITD")
	master.geometry("1300x900+10+10")	

	#w = Label(master, text="Welcome !")
	#w.pack()
	#Label(master, text="Welcome !",bg="pink", fg="black",font=12).grid(row=0,column=10)
	#Label(master, text="password").grid(row=2)
	k = mywidget(master)

	b1=Button(master, text=' ADMIN LOGIN ', command=admingui)
	b1.pack()

	b2=Button(master, text='  USER LOGIN  ', command=usergui)
	b2.pack()
	#Button(master, text='CREATE NEW USER ACCOUNT', command=add_entry_fields).grid(row=6, column=5, sticky=W, pady=4)
	b2=Button(master, text='QUIT', command=master.destroy)
	b2.pack()


mainpage()
mainloop()
