def game (a,b):
 
 if(a==b):
  print('Try again')

 if(a=='rock' and b=='scissors') or (a=='scissors' and b=='paper') or (a=='paper' and b=='rock'):
  print('Player 1 wins')
  
   
 elif(a=='rock' and b=='paper') or (a=='scissors' and b=='rock') or (a=='papaer' and b=='scissors'):
  print('Player 2 wins')
 
 else:
 	print('wrong credentials')