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
import nltk
import re
import sys
import math
import MySQLdb as mdb
import re
conn=mdb.connect(host="localhost",user="root",passwd="aneesha123",db="transportation")
cursor=conn.cursor()



def text_split():
	fr=open("addinfo.txt")
	tr=fr.readline()
	print tr
	#global source,destination
	tok=nltk.word_tokenize(tr)
	pos=nltk.pos_tag(tok)
	i=0
	for x,y in pos:
	
		print x,y
		if i!=0:
			if y =="NNP":
				if prevx=="from":
					source=x
					print "================source=",source
		if i!=0:
	
			if y =="NNP":
				if prevx=="to":
					destination=x
					print "================destination=",destination
	
		prevx=x
		prevy=y
		i=i+1
	find_table(tr,source,destination)

def find_table(tr,source,destination):
	matchObj=re.match(r'(.*) distance (.*)', tr, re.M|re.I ) or re.match(r'(.*) long (.*)', tr, re.M|re.I )
	if matchObj:	
		#distance_tab()
		print "distance table"	
	else:
		print "Type of question not defined"
	""" 
	matchObj=re.match(r'(.*)train(.*)', tr, re.M|re.I ) or re.match(r'(.*)railway(.*)', hh, re.M|re.I )
	if matchObj:	
		trainS()
	else:
		print "Type of question not defined" 
	matchObj=re.match(r'(.*)bus(.*)', tr, re.M|re.I )# or re.match(r'(.*)road(.*)', hh, re.M|re.I )
	if matchObj:	
		bus_tab()
	else:
		print "Type of question not defined" 
	"""	
	matchObj=re.match(r'(.*)route(.*)', tr, re.M|re.I ) or re.match(r'(.*)way(.*)', hh, re.M|re.I )
		
	if matchObj:	
		route_tab(source,destination,tr)
		print "route table"
	else:
		print "Type of question not defined" 
			
def route_tab(source,destination,tr):
	def add_entry():
		
		d= cursor.execute("""insert into route (source,destination,route) values(%s,%s,%s) """,(source,destination,route),)
		conn.commit()
		tkMessageBox.showinfo("Message Box!", "added sucessfully")			
			
	def edit_entry():
		d= cursor.execute("""update route set route=%s where source=%s and destination=%s""",(route,source,destination),)
		conn.commit()		
		tkMessageBox.showinfo("Message Box!", "updated sucessfully")			
		
	def interface():
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
		w = Label(master, text="An entry with the same source and destination already exists  !")
		w.pack()
		w = Label(master, text="Do you want to edit the existing entry or add as a new entry  ")
		w.pack()
		w = Label(master, text="                      ")
		w.pack()
		w = Label(master, text="                      ")
		w.pack()	
		b2=Button(master, text='EDIT ENTRY', command=edit_entry)
		b2.pack()	
		b3=Button(master, text='NEW ENTRY', command=add_entry)
		b3.pack()
		b1=Button(master, text='QUIT', command=master.destroy)
		b1.pack()				
		
	
	matchObj=re.match(r'(.*) is (.*).', tr, re.M|re.I ) 
	if matchObj:	
		route=matchObj.group(2)
		print "0000000000 route is 00000000000000",route
		d= cursor.execute("""select * from route where source=%s and destination=%s""",(source,destination),)		
		print "---------d-----------------",d		
		if d>0:
			print ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"			
			interface()
			
	




	
