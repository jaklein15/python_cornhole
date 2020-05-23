#this class hanldes the game logic and interactions between the controllers


from LightController import *
from PlayerController import *
import random

class GameController:
    def __init__(self):  
			
	#Game configuration:
	self.PLAYER_1 = PlayerController(color=Color(0, 255, 0), iplayer_num=1, bmyturn=True)
	self.PLAYER_2 = PlayerController(color=Color(255, 0, 0), iplayer_num=2, bmyturn=False)
	
	#create light controller object
	self.LIGHT_CONTROLLER = LightController()
	
	#RFID configuration:
	#TODO


    #when the round starts flash color of player whose turn it is and then set the lights for current score
    def roundStart(self):
	self.PLAYER_1.iround_score = 0
	self.PLAYER_2.iround_score = 0
	
	if self.PLAYER_1.bmy_turn:
	    self.LIGHT_CONTROLLER.roundStart(self.PLAYER_1)
	else:
	    self.LIGHT_CONTROLLER.roundStart(self.PLAYER_2)
	    
	self.showScore()
	
    #when the round is over figure out the scoring and update
    def roundOver(self):
	
	#calculate round score of both players
	iround_score = self.PLAYER_1.iround_score - self.PLAYER_2.iround_score
	
	#if round score is positive then player 1 won the round
	#if negative that means player 2 won the round
	if iround_score > 0:
		self.PLAYER_1.iscore += iround_score
		self.PLAYER_1.bmy_turn = True
		self.PLAYER_2.bmy_turn = False
	else:
		self.PLAYER_2.iscore += abs(iround_score)
		self.PLAYER_1.bmy_turn = False
		self.PLAYER_2.bmy_turn = True

	print ("Round Results..........Player 1 = %d : Player 2 = %d" % (self.PLAYER_1.iround_score,self.PLAYER_2.iround_score))
	
    #cleanup when the game is over
    def gameOver(self):
	self.LIGHT_CONTROLLER.clear()
	
	
	
    #Game Helpers
    def inTheHole(self):
	self.LIGHT_CONTROLLER.celebrate()  
	self.roundContinue()
	
    #continue the round after an event
    def roundContinue(self):
	self.LIGHT_CONTROLLER.clear()
	self.showScore()
	
    def showScore(self):
	self.LIGHT_CONTROLLER.showScore(self.PLAYER_1)
	self.LIGHT_CONTROLLER.showScore(self.PLAYER_2)
    
	
    #Main Game Loop
    
    def gameLoop(self):
	
	print("Starting Game")
	
	
	while self.PLAYER_1.iscore < 21 and self.PLAYER_2.iscore < 21:
	    
	    print ("Starting Round.........Player 1 = %d : Player 2 = %d" % (self.PLAYER_1.iscore,self.PLAYER_2.iscore))
	    self.roundStart()
	    
	    #simulation code for testing------------------------------------------------
	   
	    for bag in range(8): 
		
		if self.PLAYER_1.bmy_turn:
		    iresult_of_throw = input("Player 1 Throw Bag...")
		    self.PLAYER_1.iround_score += iresult_of_throw
		    self.PLAYER_1.bmy_turn = False
		    self.PLAYER_2.bmy_turn = True
		else:
		    iresult_of_throw = input("Player 2 Throw Bag...")
		    self.PLAYER_2.iround_score += iresult_of_throw
		    self.PLAYER_1.bmy_turn = True
		    self.PLAYER_2.bmy_turn = False
		    
		
		if iresult_of_throw == 0:
		    print ("Missed...")
		elif iresult_of_throw == 1:
		    print ("On The Board...")
		elif iresult_of_throw == 3:
		    print ("In The Hole...")
		    self.inTheHole()
		else:	
		    print ("Unknown Event...")
		    
	    #----------------------------------------------------------------------------

	    self.roundOver()
	    
	print ("Game Over")
	self.gameOver()







            
