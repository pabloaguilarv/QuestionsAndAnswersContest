import random
from players import Player

class Prize():
    def __init__(self):
        self.bottom = random.randint(100,1000)
        self.top = random.randint(5000,100000)
    
    def create_list(self):
        return list(range(self.bottom,self.top,(self.top-self.bottom)//5))

class Player_prize(Player):
    def current_prize(self):
        #How to assign current prize to current player
        pass
