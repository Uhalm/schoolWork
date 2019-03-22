#Paul Mann
#import needed stuff#
import time;
import os;
import platform;
import math;


#Define all the global variables with place holders
opsys = 'Tux';
clear = 'Tux';

people = 'Tux';
dogPer = 'Tux';
leftOverDog = 'Tux';
leftOverBun = 'Tux';
bunNeed = 'Tux';
dogNeed = 'Tux';
dogPacNeed = 'Tux';
bunPacNeed = 'Tux';

#define the constants
dogsPerPac = 10;
bunPerPac = 8;


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
		
		
#Function to get the user input
def userInput():
	#call all global variables
	global people;
	global dogPer;
	#clear the screen#
	os.system(clear);
	#ask for the number of attendants and how many hot dogs per person
	print('How many people will be attending?');
	people = input('>>>');
	#clear the screen#
	os.system(clear)
	print('There are', people, 'people attending how many Hot Dogs will be handed out per person?')
	dogPer = input('>>>');
	#Clear the screen##
	os.system(clear);
	#run the Calc function
	calc();
	

#Function for calculating the outputs needed
def calc():
#all global variables that will be needed
	global leftOverDog;
	global leftOverBun;
	global bunNeed;
	global dogNeed;
	global dogPacNeed;
	global bunPacNeed;
	
	#calculate the hotdogs needed
	dogNeed = int(people) * int(dogPer);

	#calulate the buns needed
	bunNeed = dogNeed;
	
	#calculate how many packs of hot dogs are needed
	#math.ceil() rounds the number calculated up
	dogPacNeed = math.ceil(int(dogNeed) / int(dogsPerPac));
	
	#calculate how many packs of buns are needed
	#math.ceil() rounds the number calculated up 
	bunPacNeed = math.ceil(int(bunNeed) / int(bunPerPac));
	
	#calculate how many hot dogs will be bought
	tempDogBuy = int(dogPacNeed) * int(dogsPerPac);
	#calculate how many hot dogs will be left
	leftOverDog = int(tempDogBuy) - int(dogNeed);
	
	#calculate buns that will be bought
	tempBunBuy = int(bunPacNeed) * int(bunPerPac);
	#lef over buns
	leftOverBun = int(tempBunBuy) - int(bunNeed);
	
	result();
	
	
#PRINT THE RESULTS
def result():
	#test line
	#print(leftOverBun, leftOverDog, bunNeed, dogNeed, dogPacNeed, bunPacNeed);
	#print how many hot dogs are needed and left over
	print('You will need', dogPacNeed, 'Hot Dog packs.');
	print('You will have', dogNeed, 'Hot Dogs with', leftOverDog, 'left.')
	#same as last two lines but buns
	print('You will need', bunPacNeed, 'packs of Buns.');
	print('You will have', bunNeed, 'Buns with', leftOverBun, 'left');
	#print what the user inputed
	print('There will be', people, 'people with', dogPer, 'Hot Dogs per person');
	time.sleep(25);
	userInput();
osCheck();
userInput();