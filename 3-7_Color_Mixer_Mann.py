#import needed stuff#
import time;
import os;
import platform;

opsys = 'Tux'
clear = 'Tux'

color1 = 'Tux'
color2 = 'Tux'


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
		
		
"""		
osCheck();
print(opsys);
print(clear);
print('Return');
time.sleep(20);
"""

#Get the colors the user wants to input
def colorIn():
	#call the needed global variables
	global color1;
	global color2;
	#clear the screen
	os.system(clear);
	#print instructions
	print('Color One')
	print('You can mix Red Blue or Yellow').
	#get the first color from the user
	color1 = input('>>>')
	#repeat last 4 lines for the second color
	os.system(clear);
	print('Color Two');
	print('You can mix Red Blue or Yellow');
	color2 = input('>>>');
	#run the function to find out what the colors make'
	colorMix();
	
	
#Mix the colors
def colorMix():
	#useing if elif statements to determin what colors are being mixed and what color it makes
	if color1.lower() == 'red' and color2.lower() == 'red':
	
	elif color1.lower() == 'red' and color2.lower() == 'blue':
	
	elif color1.lower() == 'red' and color2.lower() == 'yellow':
	
	elif color1.lower() == 'blue' and color2.lower() == 'red':
	
	elif color1.lower() == 'blue' and color2.lower() == 'blue':
	
	elif color1.lower() == 'blue' and color2.lower() == 'yellow':
	