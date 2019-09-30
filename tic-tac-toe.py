    #PROJECT_1-TIC_TAC_TOE GAME
					          #CODE BY RIYAZ UL HAQUE
					
def main():	              #MAIN LOOP OF THE PROGRAM 									
	def Instruction():    #DISPLAYS THE GAME INSTRUCTIONS
		print(
    """

    **WELCOME TO THE**
         	
 
 ________   _   ______             _________   ______    ______             _________    _______    ________
/___  ___\ / \ /   ___/           /___   ___\ /  __  \  /  ____/           /___   ___\  /  ___  \  /   _____\  
   / \     | | |  /       _____       / \     |  __  | |  /        ______      / \     |  /   \  | |   \     
   | |     | | |  \___    \_____\     | |     | |  | | |  \____    \_____\     | |     |  \___/  | |   /____
   \_/     \_/ \______\               \_/     \_/  \_/  \______\               \_/      \_______/   \________\
   
   
    **GAME** CODED BY: RIYAZ-UL-HAQUE					 
    THIS WILL BE A BATTLE BETWEEN A HUMAN MIND AND A COMPUTER	
      
    INSTRUCTIONS:
	1: YOU CAN MAKE YOUR MOVE BY ENTERING A NUMBER IN BETWEEN 0-8. 
	2: THE NUMBER WILL CORRESPOND TO THE BOARD POSITION AS ILLUSTRATED.
    
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
	
	3: CONDITION OF WINNING THE GAME:
	   WINNER WILL BE DECIDED ON THE BASIS OF WHOEVER SO FIRST FILL THEIR RESPECTIVE SIGN ON THE BOARD'S POSITION
	   THREE CONSECUTIVE IN ROW OR COLUMN OR EITHER IN DIAGONAL.
	4: PLAY YOUR WITH YOUR BEST MOVES.
					
		   
    """
		)
	Instruction()



#DECLARATION OF VARIABLE GLOBALLY
	X="X"
	O="O"
			
#GAME BOARD
	Board=[0,1,2,
		   3,4,5,
	       6,7,8]
	   
	def show(Board):      #DISPLAY_GAME BOARD
		print  "-- -- -- -- -- -- "
		print '||' , Board[0] , '||' , Board[1] , '||' , Board[2] , '||'
		print  "-- -- -- -- -- -- "	
		print '||' , Board[3] , '||' , Board[4] , '||' , Board[5] , '||'
		print  "-- -- -- -- -- -- "
		print '||' , Board[6] , '||' , Board[7] , '||' , Board[8] , '||'
		print  "-- -- -- -- -- -- "
	   
	show(Board)
	
	def CHOOSE_PLAYER(Board):   #FUNCTION ALLOW THE PLAYER(HUMAN) TO CHOOSE THEIR SPOT ON THE BOARD
		valid_move=False
		try:
			while(not valid_move):
				select=int(raw_input("PLEASE SELECT YOUR CHOICE TO MAKE A MOVE BETWEEN 0 To 8 :\n>"))
				if (Board[select]!='X' and Board[select]!='O'):
					Board[select]='X'
					valid_move=True
				else:
					print("SORRY THE POSITION ON THE BOARD HAS ALREADY BEEN TAKEN!! TRY OTHER")
					
		except:
			if select!=(0,8):
				print"PLEASE ENTER THE VALID INPUT BETWEEN 0 TO 8"
				CHOOSE_PLAYER(Board)
		return WIN_CHECK(Board)


	import random	
	def CHOOSE_COMPUTER(Board):                  #FUNCTION ALLOW THE COMPUTER(AI) TO CHOOSE THEIR SPOT RANDOMLY
		valid_move=False
		while(not valid_move):
		
			random.seed()
			select=random.randint(0,8)
			if (Board[select]!="X" and Board[select]!="O"):
				Board[select]="O"
				print("COMPUTER MADE A MOVE:")
				valid_move=True
				
		return WIN_CHECK(Board)
        
	def WIN(Board):
        winner=False
		if (Board[0]==Board[1]==Board[2]):
			winner=True
		elif (Board[3]==Board[4]==Board[5]):
			winner=True
		elif (Board[6]==Board[7]==Board[8]):
			winner=True
        elif (Board[0]==Board[3]==Board[6]):
			winner=True
		elif (Board[1]==Board[4]==Board[7]):
			winner=True
		elif (Board[2]==Board[5]==Board[8]):
			winner=True
		elif (Board[0]==Board[4]==Board[8]):
			winner=True
		elif (Board[2]==Board[4]==Board[6]):
			winner=True
		return winner

	# def WIN_HORIZONTAL(Board):             #CHANCES WINNER IN HORIZONTAL MOVE
	# 	winner=False
	# 	if (Board[0]==Board[1]==Board[2]):
	# 		winner=True
	# 	elif (Board[3]==Board[4]==Board[5]):
	# 		winner=True
	# 	elif (Board[6]==Board[7]==Board[8]):
	# 		winner=True
	# 	return winner
	
	# def WIN_VERTICAL(Board):               #CHANCES WINNER IN VERTICAL MOVE 
	# 	winner=False
	# 	if (Board[0]==Board[3]==Board[6]):
	# 		winner=True
	# 	elif (Board[1]==Board[4]==Board[7]):
	# 		winner=True
	# 	elif (Board[2]==Board[5]==Board[8]):
	# 		winner=True
	# 	return winner
	
	# def WIN_DIAGONAL(Board):               #CHANCES WINNER IN DIAGONAL MOVE
	# 	winner=False
	# 	if (Board[0]==Board[4]==Board[8]):
	# 		winner=True
	# 	elif (Board[2]==Board[4]==Board[6]):
	# 		winner=True
	# 	return winner
	
	def WIN_CHECK(Board):                  #CHECKING WINNER 
		GAME_WINNER=False
		if (WIN(Board)==True):
			GAME_WINNER=True
		# elif (WIN_VERTICAL(Board)==True):
		# 	GAME_WINNER=True
		# elif (WIN_DIAGONAL(Board)==True):
		# 	GAME_WINNER=True
		return GAME_WINNER
	
	
	
	#MAIN BODY OF THE PROGRAM
	Board=[0,1,2,
	       3,4,5,
	       6,7,8]
	won=False
	turn=0
	FIRST=raw_input("DO YOU WANT TO START THE GAME FIRST:(Y/N) \n>")
	if FIRST=="Y":
		print "**GREAT YOU ARE THE FIRST PLAYER AND YOU ARE PLAYING WITH Xs**:"
	elif FIRST=="N":
		print "AS YOU CHOOSE COMPUTER WILL START FIRST AND GOING TO PLAY WITH Os:"
	

    #LOGIC OF DECIDING THE TURN OF THE PLAYER	
	while(not won and turn <9):
		if FIRST=="Y":
			if turn % 2==0:
				won=CHOOSE_PLAYER(Board)
			else:
				won=CHOOSE_COMPUTER(Board)
			turn= turn+1
			show(Board)
		elif FIRST=="N":
			if turn % 2==0:
				won=CHOOSE_COMPUTER(Board)
			else:
				won=CHOOSE_PLAYER(Board)
			turn= turn+1	
			show(Board)	
	show(Board)
    
	#LOGIC OF DECIDING THE WINNER OF THE GAME  
	turn=turn -1
	if (not won):
		print "WELL THATS A TIE"
	if FIRST=="Y" and (won):	
		if (turn%2==0):
			print "CONGRATULATIONS !!! ***YOU WON***"
		elif (won):
			print "WOW !! STILL COMPUTTER IS FASTER THAN YOU ***COMPUTER WON***"
	elif FIRST=="N":
		if (turn%2==0) and (won):
			print "WOW !! STILL COMPUTTER IS FASTER THAN YOU ***COMPUTER WON***"
		elif (won):
			print "CONGRATULATIONS !!! ***YOU WON***"
	

	#FUNCTION TO ASK FOR PLAYING AGAIN
	def ask():
		print"FOR PLAYING AGAIN PRESS Y OTHERWISE QUIT THE GAME BY PRESSING ENTER"
		QUESTION=raw_input("DO YOU WANT TO PLAY AGAIN IF YES PRESS 'Y' ELSE PRESS 'N': \n>")
		if QUESTION=="Y":
			main()             #CALL TO MAIN FUNCTION
		elif QUESTION=="N":
			input("QUIT BY PRESSING ENTER")
	ask()

main()	