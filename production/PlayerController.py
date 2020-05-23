#this class handles all the player stuff

class PlayerController:
	def __init__(self, color, iplayer_num):
	
		self.color = color
		self.iplayer_num = iplayer_num
		
		self.iscore = 0			#total score across all rounds
		self.iround_score = 0	#round score
	
