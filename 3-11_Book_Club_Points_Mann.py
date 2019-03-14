#Paul Mann
#import stuff
import os;
import time;
import platform;
import math;

clear = 'tux';
opsys = 'notaOS';


books = '0.00';



#check what OS the computer is running so things work correctly# 
def osCheck():
#call the global variables#
	global clear;
	global opsys;
#get the Operating System#
	opsys = platform.system();
	#opsys = 'Free BSD'; #TEST LINE TO MAKE SURE THAT SLEEPING FOR 604800 SECONDS WILL NOT CAUSE OVERFLOW ERROR#
#check if the OS is windows#
	if opsys.lower() == 'win' or opsys.lower() == 'win32' or opsys.lower() == 'windows':
#set the command to clear the screen#
		clear = 'cls';
#set the command to change the text to green#
		os.system('color 0A');
#check if the OS is a linux device#
	elif opsys.lower() == 'linux' or opsys.lower == 'linux1' or opsys.lower == 'linux2' or opsys.lower == 'linux3':
#set the command to clear the screen#
		clear = 'clear';
#do this if not windows or linux#
	else:
#print a message saying to use windows or linux#
		print("Please use a Windows or Linux device to run this program");
#sleep indefinetly (for a week)#
		time.sleep(604800);
		
def userInput():
	global books;
	os.system(clear);
	print('How many books have you purchase');
	books = input('>>>');
	print(books);
	
	try:
		math();

	except ValueError:
		os.system(clear);
		print('Please inport a number.')
		time.sleep(5);
		userInput();
	
def math():

	global points;


	if int(books) <= 0:
		points = 0;
		
	elif int(books) >= 2 and int(books) < 4:
		points = 5;
		
	elif int(books) >= 4 and int(books) < 6:
		points = 15;
		
	elif int(books) >= 6 and int(books) < 8:
		points = 30;
		
	elif int(books) >= 8:
		points = 60;
		
	else:
		print('error');
		
		
	output();
	
	
def output():
	#print(books, points, clear);
	#time.sleep(5);
	#userInput();
	
	os.system(clear);
	print('You purchased', books, 'and have earned', points, 'points');
	time.sleep(10);
	userInput();
	
	
	
	
	
	
	
osCheck();
userInput();