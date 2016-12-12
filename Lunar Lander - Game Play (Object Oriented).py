'''
This module is used to play the game lunar lander, using two types of classes:
a LunarLander class and a LanderGame class.

Main function is included to allow user to choose game difficulty and then automatically
play the lunar lander game.
'''

import interfaces
from interfaces import *

class LunarLander:
    '''
    Creates an object that resembles a real life lunar lander that will be used for the lander game.
    '''
    def __init__(self, ialtitude, ifuelAmount, ivelocity):
        '''
	    Creates a LunarLander class object
	    '''
        self.altitude = ialtitude
        self.fuel = ifuelAmount
        self.velocity = ivelocity

    def getAltitude(self):
	    '''
	    Returns the LunarLander's altitude
	    '''
	    return self.altitude

    def getFuel(self):
	    '''
	    Returns the LunarLander's amount of fuel remaining
	    '''
	    return self.fuel

    def getVelocity(self):
	    '''
	    Returns the LunarLander's velocity
	    '''
	    return self.velocity

    def update(self, thrustAmount):
	    '''
	    Updates the instance variables of the LunarLander based on the amount of thrust
	    a user chooses to use.
	    '''
	    if self.fuel >= thrustAmount:
	        self.velocity += 4 * thrustAmount - 2
	        self.altitude += self.velocity
	        self.fuel -= thrustAmount
	    else:
		    self.velocity += self.fuel * 4 - 2
		    self.altitude += self.velocity
		    self.fuel = 0

class LanderGame:
    '''
    Used to run the game of lander, through a TextLanderInterface object and LunarLander object.
    '''
    def __init__(self, difficulty):
	    '''
	    Constructs a LanderGame class object
	    '''
	    self.interface = GraphicLanderInterface()
	    if difficulty == 1:
	        self.lunarLander = LunarLander(200, 30, 0)
	    elif difficulty ==2:
	        self.lunarLander = LunarLander(250, 25, 0)
	    elif difficulty == 3:
	        self.lunarLander = LunarLander(350, 20, 0)
	    elif difficulty == 4:
	        self.lunarLander = LunarLander(500, 10, 0)
    
    def play(self):
	    '''
	    Runs the game of lunar lander, by constantly prompting user for amount of thrust
	    to use and then updating the lunar lander's values, until the lander lands.
	    '''
	    while self.lunarLander.getAltitude() > 0:  #keep running the game until lander is on the ground
	        self.interface.showInfo(self.lunarLander)
	        thrust = self.interface.getThrust()
	        self.lunarLander.update(thrust)
	    if self.lunarLander.getAltitude() <= 0: #test whether lander crashed or not once lander has landed
		    if self.lunarLander.getVelocity() < -10:
		        self.interface.showCrash(self.lunarLander)
		    else:
		        self.interface.showLanding(self.lunarLander)
			
def main():
    print("This lander game has four difficulty options, with difficulty 1 being the easiest and difficulty 4 being the hardest.")
    print("For each increasing difficulty level, the lander will start at a higher altitude and will start with less units of fuel.")
    difficulty = input("Which difficulty level would you like to play?")
    testString = "1234"
    while (difficulty not in testString or difficulty == ""):
        difficulty = input("Which difficulty level would you like to play?")
    game = LanderGame(int(difficulty))
    game.play()
	
if __name__ == "__main__":
    main()