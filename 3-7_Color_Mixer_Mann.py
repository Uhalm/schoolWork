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
	print('Color One');
	print('You can mix Red Blue or Yellow');
	#get the first color from the user
	color1 = input('>>>');
	#repeat last 4 lines for the second color
	os.system(clear);
	print('Color Two');
	print('You can mix Red Blue or Yellow');
	color2 = input('>>>');
	#run the function to find out what the colors make'
	colorMix();
	
	
#Mix the colors
def colorMix():
	#useing if elif statements to determin what colors are being mixed and what color it makes along with its HTML Hex Color Code
	if color1.lower() == 'red' and color2.lower() == 'red':
		os.system(clear);
		print('Red and Red mix to make Red');
		print('HTML Color Code is #FF0000');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'red' and color2.lower() == 'blue':
		os.system(clear);
		print('Red and Blue mix to make Purple');
		print('HTML Color Code is #800080');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'red' and color2.lower() == 'yellow':
		os.system(clear);
		print('Red and Yellow mix to make Orange');
		print('HTML Color Code is #FFA500');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'blue' and color2.lower() == 'red':
		os.system(clear);
		print('Blue and Red mix to make Purple');
		print('HTML Color Code is #800080');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'blue' and color2.lower() == 'blue':
		os.system(clear);
		print('Blue and Blue mix to make Blue');
		print('HTML Color Code is #0000FF');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'blue' and color2.lower() == 'yellow':
		os.system(clear);
		print('Blue and Yellow mix to make Green');
		print('HTML Color Code is #008000');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'yellow' and color2.lower() == 'red':
		os.system(clear);
		print('Yellow and Red mix to make Red Orange');
		print('HTML Color Code is #FFA500');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'yellow' and color2.lower() == 'blue':
		os.system(clear);
		print('Yellow and Blue mix to make Green');
		print('HTML Color Code is #008000');
		time.sleep(5);
		colorIn();
		
	elif color1.lower() == 'yellow' and color2.lower() == 'yellow':
		os.system(clear);
		print('Yellow and Yellow mix to make Yellow');
		print('HTML Color Code is #FFFF00');
		time.sleep(5);
		colorIn();
	
	#if input does not match any of the above statements
	else:
		os.system(clear);
		print('One of the colors you picked is not valid');
		time.sleep(3);
		colorIn();
		
		
osCheck();
colorIn();0