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
import nltk
import re
import sys
import math
import MySQLdb as mdb
import re
conn=mdb.connect(host="localhost",user="root",passwd="aneesha123",db="transportation")
cursor=conn.cursor()




def show_distance():
	a="select * from distance "
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("distance.txt","w");
	g.write("--------------------------------------------------------------------------------------------------------------\n")
	g.write("                                 Table distance                                                      \n")
	g.write("------------------------------------------------------------------------------------------------------------\n")
	g.write("did \t\t source \t\t destination \t\t distance\n")
	g.write("------------------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")
		g.write(str(a[2]))
		g.write("\t\t")	
		g.write(str(a[3]))
		g.write("\t\t")
		g.write("\n")
	g.write("-----------------------------------------------------------------------------------------------------------------------------")	
	g.close()
	samplea()

def show_trains():
	a="select * from trains "
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("trains.txt","w");
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	g.write("                       Tabletrains                                                                         \n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	g.write("trid \t\t source \t\t destination \t\t train id \t\t train time\n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")
		g.write(str(a[2]))
		g.write("\t\t")	
		g.write(str(a[3]))
		g.write("\t\t")
		g.write(str(a[4]))
		g.write("\t\t")
		g.write("\n")
	g.write("------------------------------------------------------------------------------------------------------------")	
	g.close()
	samplet()
def show_traindata():	
	a="select * from traindetails "
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("traindata.txt","w");
	g.write("-------------------------------------------------------------------------------------------------------------------------\n")
	g.write("                                 Table train details                                                                     \n")
	g.write("-------------------------------------------------------------------------------------------------------------------------\n")
	g.write("trid \t\t  train name\n")
	g.write("-------------------------------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")		
		g.write("\n")
	g.write("--------------------------------------------------------------------------------------------------------------------")	
	g.close()
	sampletdata()

def show_buses():
	a="select * from buses "
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("buses.txt","w");
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	g.write("                                 Table buses                                                         \n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	g.write("tid \t\t source \t\t destination \t\t busid\t\t start_time\t\t reach_time\n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")
		g.write(str(a[2]))
		g.write("\t\t")	
		g.write(str(a[3]))
		g.write("\t\t")
		g.write(str(a[4]))
		g.write("\t\t")
		g.write(str(a[5]))
		g.write("\t\t")
		g.write("\n")
	g.write("-----------------------------------------------------------------------------------------------------------------------------")	
	g.close()
	sampleb()
def show_bus_data():
	a="select * from busdetails "
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("busdetails.txt","w");
	g.write("-----------------------------------------------------------------------------------------------------\n")
	g.write("                                 Table buses                                                         \n")
	g.write("-----------------------------------------------------------------------------------------------------\n")
	g.write("busid \t\t busname \n")
	g.write("-----------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")
		g.write("\n")
	g.write("-----------------------------------------------------------------------------------------------------")	
	g.close()
	samplebd()

def show_route():
	a="select * from route"
	cursor.execute(a)
	row=cursor.fetchall()
	g=open("route.txt","w");
	g.write("-------------------------------------------------------------------------------------------------------------------------\n")
	g.write("                                 Table route                                                         \n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	g.write("rid \t\t source \t\t destination \t\t route\n")
	g.write("--------------------------------------------------------------------------------------------------------------------------\n")
	for a in row :
       		print a
		
		g.write(str(a[0]))
		g.write("\t\t")
		g.write(str(a[1]))
		g.write("\t\t")
		g.write(str(a[2]))
		g.write("\t\t")	
		g.write(str(a[3]))
		g.write("\t\t")
		g.write("\n")
	g.write("----------------------------------------------------------------------------------------------------------------------------")	
	g.close()
	sampler()




def samplea():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Distance Table')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 80,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("distance.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()

def samplet():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Trains Table')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 120,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("trains.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()
def sampletdata():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Trains Table')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 120,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("traindata.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()

def sampleb():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Bus Table')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 120,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("buses.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()


def samplebd():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Bus Details')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 120,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("busdetails.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()
def sampler():
	mw = Tkinter.Tk()
	#tkMessageBox.showinfo("Message Box!", "sample3.....")
	mw.option_add("*font", ("Arial", 8, "normal"))
	mw.title('Route Table')
	mw.geometry("+373+262")
	txt = ScrolledText.ScrolledText(mw,
		                        background = 'white',
		                        width = 120,
		                        height =20,
		                        font = ("Arial", 12, "normal"))
	txt.pack()
	g = open("route.txt","r")
	grad=g.read()	
	g.close()
	
	txt.insert(END, grad)
	btn1 = Tkinter.Button(mw, text = "OK", command = mw.destroy)
	btn1.pack(side = RIGHT, padx = 10, pady = 10)
	mw.mainloop()
