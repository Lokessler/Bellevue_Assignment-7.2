#!/usr/bin/python3

# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Logan Kessler
# Creation Date: 09-23-2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors).
# You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#print('''You are in a land full of dragons. In front of you,
	#you see two caves. In one cave, the dragon is friendly
	#and will share his treasure with you. The other dragon
	#is greedy and hungry, and will eat you on sight.''')
        str1 = 'You are in a land full of dragons. In front of you,\n'
        str2 = 'you see two caves. In one cave, the dragon is friendly\n'
        str3 = 'and will share his treasure with you. The other dragon\n'
        str4 = 'is greedy and hungry, and will eat you on sight.'
        print(str1 + str2 + str3 + str4 + '\n')
        # LogicError: multi-line string includes ALL whitespace to be printed
        #print()
        # LogicError: unnecessary empty 'print()' call following 'print()' call to create newline
        # Appended '\n' character to preceding 'print()' function

def chooseCave():
    cave = ''
	#while cave != '1' and cave != '2':
	#	print('Which cave will you go into? (1 or 2)')
	#	cave = input()
        #
	#return caves
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
        
    return cave
    # NameError: name 'caves' is not defined, changed to 'cave' variable
    # TabError: inconsistent use of tabs and spaces in indentation

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
        # LogicError: Comment says 'sleep for 2 seconds' not 3
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
		# SyntaxError: Missing parentheses in call to 'print'

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
# SyntaxError: invalid syntax, use '==' for equality operation
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	# NameError: name 'choosecave' is not defined, changed to use 'chooseCave' function
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#print("Thanks for planing")
                print("Thanks for playing")
                # LogicError: We're not 'planing' in this program, should be 'playing' instead

