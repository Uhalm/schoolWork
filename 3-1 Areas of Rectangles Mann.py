#Paul Mann
#3-2 Area of Rectangle
import os;
import time;

length1 = 0;
width1 = 0;
length2 = 0;
width2 = 0;
area1 = 0;
area2 = 0;


def mainMenu():
	global length1;
	global length2;
	global width1;
	global width2;
	
	os.system('cls');
	
	length1 = input('What is the length of the first rectangle? : ');
	width1 = input('What is the width of the first rectangle? : ');
	length2 = input('What is the length of the second rectangle? : ');
	width2 = input('What is the width of the secodn rectangle? : ');
	
	#print(length1);
	#print(width1);
	#print(length2);
	#print(width2);
	
	theMaths();
	
	time.sleep(2);


def theMaths():
	global length1;
	global length2;
	global width1;
	global width2;
	
	os.system('cls');
	
	area1 = float(length1) * float(width1);
	area2 = float(length2) * float (width2);
	
	print(area1);
	print(area2);
	
	check();
	
def check():
	global length1;
	global length2;
	global width1;
	global width2;	
	global area1;
	global area2;
	
	if area1 > area2:
		print("The area of rectangle 1 is", area1 + ". ");
		print("The area of rectangle 2 is", area2 + ".");
		print("Rectangle 1 is bigger.")
	
	if area2 > area1:
		print("The area of rectangle 1 is", area1 + ". ");
		print("The area of rectangle 2 is", area2 + ".");
		print("Rectangle 2 is bigger.");
	
	if area1 == area2:
		print("The area of rectangle 1 is", area1 + ". ");
		print("The area of rectangle 2 is", area2 + ".");
		print("Rectangle 2 is bigger.");
		
	else:
		print("ERROR ERROR ERROR ERROR YOUR GONNA DIE THE COMPUTER BROKE ANY RULE OF MATH POSIBLE");
	
	time.sleep(5);
	mainMenu();
	

mainMenu();