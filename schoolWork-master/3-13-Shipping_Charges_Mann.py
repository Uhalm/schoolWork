#Paul Mann
#import stuff
import os;
import time;
import platform;
import math;

#global values
#needed for osCheck
clear = 'tux';
opsys = 'notaOS';

#weight of the package as string and float
weightTxt = 'tux'
weightNum = 0;

#output prices
priceOut = 0;


#input prices
twoLess = 1.50;
twoSix = 3;
sixTen = 4;
tenPlus = 4.75;





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
	#clear the screen
	os.system(clear);
	#call needed global values
	global weightTxt;
	global weightNum;

	#get the user input
	print('Input the weight of the package in pounds.');
	weightTxt = input('>>>');

	#try setting weightNum to the float of weightTxt
	#if fail then print error and go back to userInput

	try:
		#weightNum = weightTxt
		weightNum = float(weightTxt);
		#TEST LINE SEE IF VARIABLES SET CORRECTLY
		#print(weightNum, weightTxt);
		#TEST LINE SLEEPING
		#time.sleep(5);
		#END OF TEST LINES
		#goto the calc function
		calc();


	#do this if the last chunck of code errors
	except ValueError:
		#clear the screen
		os.system(clear);
		#print a error
		print('Please input a number.');
		#TEST LINE TO SEE WHAT THE VARIABLES WILL DISPLAY
		#print(weightNum, weightTxt);
		#sleep for 3 seconds
		time.sleep(3);
		#go back to the begining of this function
		userInput();



def calc():
	#call global values
	global priceOut
	#clear the screen
	os.system(clear);
	#check what the weight of the packages are
	#2 lbs or less
	if weightNum <= 2:
		#calculate output price
		priceOut = weightNum * twoLess;
		#run printer function
		printer();
	#if between 2 and 6 lbs
	elif weightNum > 2 and weightNum <= 6:
		priceOut = weightNum * twoSix;
		printer();
	#if between 6 and 10 lbs
	elif weightNum > 6 and weightNum <= 10:
		priceOut = weightNum * sixTen;
		printer();
	#if over 10 lbs
	elif weightNum > 10:
		priceOut = weightNum * tenPlus;
		printer();
	#this should never show up its a error code if these statements before dont work
	else:
		print("""This error shouldn't print unless there is a problem
		Code: 001""");



#print results
def printer():
	#clear the screen
	os.system(clear);
	#print the price and weight
	#print(priceOut, weightNum, weightTxt); ###TEST LINE
	print("The package weighes", weightTxt, "pounds")
	print("The shipping price is", format(priceOut, '.2f'), "$");
	time.sleep(5);
	userInput();


osCheck();
userInput();
