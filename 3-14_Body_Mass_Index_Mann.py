#Paul Mann
#import things

import os;
import time;
import platform;

#Needed variables
clear = 'tux';
opsys = 'tux';

#what the user will input
height = 'tux';
weight = 'tux';

#what the program will output
BMI = 0;
bmiStat = 'tux';

#the variables that wont change
LOW = 18.5;
HIG = 25.0;


#check the OS
def osCheck():
#call the global variables#
	global clear;
	global opsys;
#get the Operating System#
	opsys = platform.system();
#	opsys = 'Free BSD'; #TEST LINE TO MAKE SURE THAT SLEEPING FOR 604800 SECONDS WILL NOT CAUSE OVERFLOW ERROR#
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




def main():
	#clear the screen
	os.system(clear);

	#call the global variables needed
	global weight;
	global height;

	#get the users hight and weight
	print('What is your height?');
	height = input('>>>');

	#clear the screen
	os.system(clear);

	#get user weight
	print('What is your weight?');
	weight = input('>>>');

	#try bmiCalc
	try:
		bmiCalc();

	#if last block has value error then try this
	except ValueError:
		#clear the screen
		os.system(clear);


		#print the error
		print('One of your inputs was not a number.');
		print('Plase input a number.');


		#sleep for 3 seconds
		time.sleep(3);
		#rerun the main function
		main();




#calculate the BMI
def bmiCalc():
	#call global variables
	global BMI;
	#the equasion
	BMI = float(weight) * 703 / float(height) ** 2;



	#bmiCheck to see if the BMI is a healthy one or not
	bmiCheck();




#function to check what your BMI is
def bmiCheck():
	#call the global variables
	global bmiStat;

	#clear the screen
	os.system(clear);


	#check if BMI is bellow 18.5
	if BMI < LOW:
		bmiStat = 'underweight';
		printer();

	#check if BMI is normal
	elif BMI <= LOW and BMI >= HIG:
		bmiStat = 'optimal';
		printer();

	elif BMI > HIG:
		bmiStat = 'overweight';
		printer();

	else:
		print('This is a imposible error.');
		main();



#print the results
def printer():
	#clear the screen
	os.system(clear);


	#print the results
#	print(BMI); #TEST LINE TO SEE IF THE BMI WILL PRINT
#	print(bmiStat); #TEST LINE TO SEE IF THE bmiStat VARIABLE WORKS
	print('Your BMI is', format(BMI, '.3f'));
	print('Your BMI is', bmiStat);


	#sleep for 3 seconds and return to the main
	time.sleep(3);
	main();



osCheck();
main();
