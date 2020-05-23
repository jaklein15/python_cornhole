#this class hanldes the game logic and interactions between the controllers


from LightController import *
from PlayerController import *
import random

class GameController:
    def __init__(self):  
			
	#Game configuration:
	self.PLAYER_1 = PlayerController(color=Color(0, 255, 0), iplayer_num=1)
	self.PLAYER_2 = PlayerController(color=Color(255, 0, 0), iplayer_num=2)
	
	#create light controller object
	self.LIGHT_CONTROLLER = LightController()
	
	#RFID configuration:
	#TODO

    
    #Game Events
    
    #When someone gets the bag in the hole celebrate with lights
    def InTheHole(self):
	self.LIGHT_CONTROLLER.Celebrate()  
	self.RoundContinue()
	
    def ShowScore(self):
	self.LIGHT_CONTROLLER.ShowScore(self.PLAYER_1.iscore, self.PLAYER_1.iplayer_num, self.PLAYER_1.color)
	self.LIGHT_CONTROLLER.ShowScore(self.PLAYER_2.iscore, self.PLAYER_2.iplayer_num, self.PLAYER_2.color)
	
	
    #when the round starts set the lights for current score
    def RoundStart(self):
	self.ShowScore()
	
     #continue the round after an event
    def RoundContinue(self):
	self.LIGHT_CONTROLLER.Clear()
	self.ShowScore()
	
    #when the round is over figure out the scoring and update
    def RoundOver(self):
	
	#temporary for testing
	self.PLAYER_1.iround_score = random.randint(0,12)
	self.PLAYER_2.iround_score = random.randint(0,12)
	
	#calculate round score of both players
	iround_score = self.PLAYER_1.iround_score - self.PLAYER_2.iround_score
	
	#if round score is positive then player 1 won the round
	#if negative that means player 2 won the round
	if iround_score > 0:
		self.PLAYER_1.iscore += iround_score
	else:
		self.PLAYER_2.iscore += abs(iround_score)

	print ("Round Results.............%d : Player 1 = %d : Player 2 = %d" % (iround_score,self.PLAYER_1.iround_score,self.PLAYER_2.iround_score))
	
    #cleanup when the game is over
    def GameOver(self):
	self.LIGHT_CONTROLLER.Clear()
	
    #Main Game Loop
    def GameLoop(self):
	
	print("Starting Game")
	
	while self.PLAYER_1.iscore < 21 and self.PLAYER_2.iscore < 21:
	    
	    print ("Starting Round.........Player 1 = %d : Player 2 = %d" % (self.PLAYER_1.iscore,self.PLAYER_2.iscore))
	    self.RoundStart()
	    time.sleep(5.0)
	    print ("In the Hole............Player 1 = %d : Player 2 = %d" % (self.PLAYER_1.iscore,self.PLAYER_2.iscore))
	    #self.InTheHole()
	    self.RoundOver()
	    print ("Round Over.............Player 1 = %d : Player 2 = %d" % (self.PLAYER_1.iscore,self.PLAYER_2.iscore))
	    
	print ("Game Over")
	self.GameOver()







            
