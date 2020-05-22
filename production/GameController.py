#this class hanldes the game logic and interactions between the controllers


from LightController import *

class GameController:
    def __init__(self):  
			
			
	#Game configuration:
	self.iPlayer_Score = 0
	
	#create light controller object
	self.LIGHT_CONTROLLER = LightController(color=Color(0, 255, 0))
	
	#RFID configuration:
	#TODO

    
    #Game Events
    
    #When someone gets the bag in the hole celebrate with lights
    def InTheHole(self):
	self.LIGHT_CONTROLLER.celebrate()  
	self.LIGHT_CONTROLLER.clear()
	self.LIGHT_CONTROLLER.showScore(self.iPlayer_Score)
	
    #when the round starts set the lights for current score
    def RoundStart(self):
	self.LIGHT_CONTROLLER.showScore(self.iPlayer_Score)
	
    #when the round is over figure out the scoring and update
    def RoundOver(self):
	self.iPlayer_Score += 3

	
    #cleanup when the game is over
    def GameOver(self):
	self.LIGHT_CONTROLLER.clear()
	
    #Main Game Loop
    def GameLoop(self):
	
	while self.iPlayer_Score < 21:
	    
	    print ("Starting Round.........Score = %d",self.iPlayer_Score)
	    self.RoundStart()
	    time.sleep(3.0)
	    print ("In the Hole............Score = %d",self.iPlayer_Score)
	    self.InTheHole()
	    self.RoundOver()
	    print ("Round Over.............Score = %d",self.iPlayer_Score)
	    
	print ("Game Over")
	self.GameOver()







            
