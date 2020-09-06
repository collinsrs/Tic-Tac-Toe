ilistName =[]

input ("What is your name?"

listName.append input
       


	game = ['1.1','1.2','1.3','2.1','2.2','2.3','3.1']


def print_board(game):
	print (game['1.1'] + '|' + game['1.2'] + '|' + game['1.3']) 
	print('-+-+-')
	print (game['2.1'] + '|' + game['2.2'] + '|' + game['2.3'])
	print('-+-+-')
	print (game['3.1'] + '|' + game['3.2'] + '|' + game['3.3'])


###print (print_board)

##Function enabling user to stop game
def end(go): 
	if go == "stop":
		raise SystemExit

##Function definig win conditions
	def check_gme(game, turn):
    	win_true =:
             ['1.1', '2.1', '3.1'],
             ['1.2', '2.2', '3.2'],
             ['1.3', '2.3', '3.3'],
             ['1.1', '1.2', '1.3'],
             ['2.1', '2.2', '2.3'],
             ['3.1', '3.2', '3.3'],
             ['1.1', '2.2', '3.3'],
             ['1.3', '2.2', '3.1']
		   for condition in win_true:
                print("You Win!")
                print("Would you like to play again? Type yes to play again.")
                playAgain = input()
                if playAgain == 'yes':
                    return playAgain
                else:
                    exit
	 player = 'X'
    move = ' '
    print('To stop the game at any point, type in STOP, or press Control (^)-C on your keyboard.')
  

  while gameMove !="STOP":
	  	print_board(game)
	  	print ("It's" + move + "'s turn. Where would you like to move to?")
	  	move = input ()
	  	if move != game:
		  print ("Invalid entry. Try again.")
		elif game[move] =:
			game[move]=player

		else:
			print ("Invald entry. Try again.")  
	
	  

		
