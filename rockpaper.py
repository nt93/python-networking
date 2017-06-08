from __future__ import print_function
#import func
abc = "yes"

while abc!="no":

	pl1 = raw_input('Player 1 turn (select from rock/ paper/ scissors): ')
	pl2 = raw_input('Player 2 turn (select from rock/ paper/ scissors): ')
			 
	if(pl1==pl2):
		print('Try again')
			 
	if(pl1=='rock' and pl2=='scissors') or (pl1=='scissors' and pl2=='paper') or (pl1=='paper' and pl2=='rock'): 
		print('Player 1 wins')
		break

	if(pl1=='rock' and pl2=='paper') or (pl1=='scissors' and pl2=='rock') or (pl1=='papaer' and pl2=='scissors'): 
		print('Player 2 wins')
		break
	else:
		print('Wrong credentials')
	abc= raw_input("Do you want to continiue:")