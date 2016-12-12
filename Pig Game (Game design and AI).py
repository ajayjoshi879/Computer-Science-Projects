"""
   Simulates a game of pig between two players: a computer which rolls
   6 dice each turn, and a human player who can choose the number of
   dice to roll each turn. 
"""

import random

turn = 0
totalScoreP0 = 0
totalScoreP1 = 0

"""
Simulates rolling a certain amount of dice with 6 sides and sums the
results. If a 1 is rolled, then the turn total is automatically
set to 1 and no more dice will be rolled.
"""
def rollDice(numDice):
    turnScore = 0
    for i in range(numDice): #Rolls dice numDice number of times.
        roll = random.randrange(1,7)   #Limits result of dice roll to 1-6.
        if roll == 1: #Check to see if a 1 was rolled.
            print("Rolled a 1, score for this round is 1.")
            turnScore = 1 #Sets score to 1 if a 1 was rolled.
            break #Stops rolling if a 1 was rolled.
        else:
            turnScore += roll #Sums the result of each roll.
    return turnScore

"""
Takes the result from rollDice and returns an overall turnScore.
If 0 dice are rolled then turnScore is based off the largest individual
digit of the opponent's total score.
"""
def takeTurn(opponentScore, numDice):
    #Calls rollDice to return the sum of the dice rolled.
    turnScore = rollDice(numDice)
    if numDice == 0: #checks to see if a player chose to roll no dice.
        singlesDigit = opponentScore % 10  #Finds singles digit of
                                           #opponent's score.
        doublesDigit = opponentScore // 10 #Finds tens digit of
                                           #opponent's score.
        if singlesDigit >= doublesDigit:   #Compares singles to tens digit
            turnScore = singlesDigit + 1   #Adding 1 to the larger digit.
        else:
            turnScore = doublesDigit + 1
        print("Total score for this turn is", turnScore)
        return turnScore
    else:
        print("Total score for this turn is", turnScore)
        return turnScore


#Strategy for the computer, which always chooses to roll 6 dice.
def alwaysRoll6Player(score, opponentScore, goalScore):
    turnScore = rollDice(6)
    print("Total score for this turn is", turnScore)
    return turnScore

"""
Allows for human input to choose how many dice they want to roll.
Returns an overall turnScore.
"""
def humanPlayer(score, opponentScore, goalScore):
    turnScore = 0
    print("Your score is", score, "and your opponent's score is", opponentScore)
    #Asks user for input of how many dice to roll.
    userInput = input("How many dice would you like to roll: ")
    numChoice = int(userInput)
    while numChoice > 10 or numChoice < 0: #Makes sure user enters valid
                                           #number of dice.
        secondTry = input("Input a number between 0 and 10: ")
        numChoice = int(secondTry)
    #Calls takeTurn using the human input to return overall turnScore.
    turnScore = takeTurn(opponentScore, numChoice)
    return turnScore

"""
Overall simulation which combines previous functions to simulate a game
of pig. Keeps track of total score and turn sequence. Checks after each
turn to see if player has reached goalScore, and terminates the game if
maxRounds is reached.
"""
def playPig (goalScore, maxRounds, strategy0, strategy1):
    turn = 0    #Initializes first turn to player0
    totalScoreP0 = 0
    totalScoreP1 = 0
    
    #Deciding whose turn it is within the range of maxRounds.
    for i in range(maxRounds):
        print("****\nTurn", i)
        if turn == 0:
            print("It is player0's turn")
            #Calls strategy0 to return a turnScore.
            turnScore = strategy0(totalScoreP0, totalScoreP1, goalScore)
            turn = 1      #Switches the turn for the next loop.
            totalScoreP0 += turnScore   #Keeping track of totalScoreP0.
            print("P0's total score is", totalScoreP0, "and P1's total score is", totalScoreP1)
            if totalScoreP0 >= goalScore:
                print ("****\nP0 wins!")
                return True    #Used for counting P0's wins in runExperiment
                break
        elif turn == 1:
            print("It is player1's turn")
            #Calls strategy1 to return a turnScore.
            turnScore = strategy1(totalScoreP1, totalScoreP0, goalScore)
            turn = 0      #Switches the turn for the next loop.
            totalScoreP1 += turnScore #Keeping track of totalScoreP1.
            print("P0's total score is", totalScoreP0, "and P1's total score is", totalScoreP1)
            if totalScoreP1 >= goalScore:
                print("****\nP1 wins!")
                return False
                break
        if i == maxRounds - 1: #Draws the game if maxRounds reached.
            print("****\nMaximum number of rounds reached. Game is a draw.")
            
"""            
Automatically runs playPig with predetermined parameters, with strategy0
being humanPlayer function, and strategy1 being alwaysRoll6Player function.
"""
def main():
	playPig(100, 20, humanPlayer, alwaysRoll6Player)

if __name__ == "__main__":
	main()

"""
Part II Question 1
Finds the average score obtained by rolling n dice (0 <= n <= 10). Rolls n dice by
a certain amount of simulations, sums the total from each simulation, and finds the average
by dividing total by the number of simulations
"""
def averageScoreForDice(numDice, numSimulations):
    total = 0    #initializing the total
    for i in range(numSimulations):
        turnScore = 0    #initializing the turnScore at start of each simulation
        for j in range(numDice):
            roll = random.randrange(1,7)   #Limits result of dice roll to 1-6.
            if roll != 1:
                turnScore += roll  #summing the result of each roll
            else:
                turnScore = 1   #If player rolls a 1, player only gets a score of 1 for entire simulation round
                break
        total += turnScore   #summing the result of each simulation
    average = total / numSimulations
    return average

#compares the average turn score of rolling 1 die, 2 dice...up to 10 dice, and finds the number of dice
#that gives largest average turn score
def maximumAverageScoreAction(numSimulations):
    optimalDiceNum = 0   #tracker of how many number of dice give highest average score
    prevResult = 0   #initiates a counter to keep track of the result returned
    for i in range(1, 11):
        result = averageScoreForDice(i, numSimulations)   #finds the average turn score of rolling i number of 
                                                          #dice based on numSimulations
        if result >= prevResult:   
            optimalDiceNum = i     #if new result is larger than old result, tracker updates
                                   #to store the number of dice that produced
                                   #the new highest average
        prevResult = result   #stores current result to compare to the new result
                              #from the next loop iteration
        print("Rolling", i,"dice", numSimulations, "times gives an average score of", result)
    return optimalDiceNum
        

"""
Part II Question 2
Simulates n number of games between two players, one of whom uses the alwaysRoll6Player strategy.
Keeps track of how many games Player 0 wins, and calculates the win percentage of Player 0.
"""

def runExperiment(n, strategy1):
    winsP0 = 0   #initializing win count for P0 and P1
    winsP1 = 0
    for i in range(n):
        outcome = playPig(100, 20, strategy1, alwaysRoll6Player)
        if outcome == True:    #situation where P0 wins
            winsP0 += 1
        elif outcome == False: #situation where P1 wins
            winsP1 += 1
    percP0Win = winsP0 / n *100    #finding P0's win percentage
    print("Player 0 won", winsP0, "games out of", n, "games. P0's win percentage is", percP0Win, "%")
    

"""
Part II Question 3
An optimization of the alwaysRoll6Player strategy. Player 0 will roll 0 dice if the result
will immediately allow him / her to reach the goalScore, or if the result will give him / her
at least 8 points
"""

def roll0strategy(score, opponentScore, goalScore):
    singlesDigit = opponentScore % 10      #Finds singles digit of opponent's score.
    doublesDigit = opponentScore // 10     #Finds tens digit of opponent's score.
    
    #determining if rolling 0 will immediately give P0 victory                                       
    if (singlesDigit + 1) >= (goalScore - score) or (doublesDigit + 1) >= (goalScore - score):
        turnScore = takeTurn(opponentScore, 0)
        
    elif singlesDigit >= 7 or doublesDigit >= 7:  #determining if rolling 0 will give at least 8 points
        turnScore = takeTurn(opponentScore, 0)
    else:
        turnScore = alwaysRoll6Player(score, opponentScore, goalScore)
    return turnScore
    
"""
Part II Question 4
A further optimized strategy by Andrew and Will. This strategy improves on all the previous
strategies and yields the highest win percentage that we have discovered.

The strategy entails: roll 0 dice if the turn score would give immediate victory, else
only roll 0 if the turn score will be 10. Additionally, P0 should take larger gambles
by rolling more dice if he is far behind P1 and P1 is close to winning. Lastly, the default
setting if above conditions are not met is to roll 7 dice each turn
"""
    
def bestStrategy(score, opponentScore, goalScore):

    singlesDigit = opponentScore % 10      #Finds singles digit of opponent's score.
    doublesDigit = opponentScore // 10     #Finds tens digit of opponent's score.

    #determining if rolling 1 will immediately give P0 victory                                       
    if (singlesDigit + 1) >= (goalScore - score) or (doublesDigit + 1) >= (goalScore - score):
        turnScore = takeTurn(opponentScore, 0)
        
    elif singlesDigit == 9 or doublesDigit == 9: #else only roll 0 if it will yield 10 points
        turnScore = takeTurn(opponentScore, 0)
    
    elif opponentScore > 90 and score < 40:   #take larger gamble by rolling more dice if
                                              #if very far behind in the game
        turnScore = takeTurn(opponentScore, 10)
    
    else:   #default setting of rolling 7 yields higher win percentage than alwaysRoll6Player
        turnScore = takeTurn(opponentScore, 7)
        
    return turnScore
