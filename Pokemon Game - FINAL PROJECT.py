'''
CS 111: Intro to Computer Science
Final project by Andrew Qi and Hazel Que

This module runs a Pokemon game. Human player and computer player will each have
6 Pokemon. Each player chooses one Pokemon at a time and uses the Pokemon's attacks
on the opponent's Pokemon. When a Pokemon's health reaches zero, the Pokemon is defeated and the player will have to choose a new Pokemon.
The first player to defeat all the Pokemons of the other player wins.

*The computer player is so intelligent that we've lost many times*
'''

import supportModule
import graphics

class Attack:
	'''Constructs an Attack class, with instance variables name, type and damage and accessor
	methods for all the instance variables. Used for each Pokemon's attacks'''
	def __init__(self, iname, itype, idamage):
		self.name = iname
		self.type = itype
		self.damage = idamage

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getDamage(self):
		return self.damage

class Pokemon:
	'''Constructs a Pokemon class, with instance variables name, type, weakness, resistance,
	main attack, alternative attack, current health, original health and image.
	The Pokemon is capable of using attacks, receiving damage, as well as displaying an image that represents itself,
	as well as displaying the Pokemon's class object's other information.
	Thus, the class object includes accessor methods for all the instance variables as well as for the health bar,
	which is used for display purposes, and includes mutator methods for number of attacks and retreats used and health status.
	'''
	
	def __init__(self, iname, itype, iweakness, iresistance, imainAttack, ialtAttack, ihealth, ohealth, iimage):
		self.name = iname
		self.type = itype
		self.mainAttack = imainAttack
		self.altAttack = ialtAttack
		self.health = ihealth
		self.originalHealth = ohealth
		self.weakness = iweakness
		self.resistance = iresistance
		self.image = iimage
		self.display = None
		self.greenHealthBar = None
		self.redHealthBar = None
		self.healthText = None
		self.mainAttackUse = 0
		self.retreat = 0

	def getName(self):
		return self.name

	def getType(self):
		return self.type
	
	def getMainAttack(self):
		return self.mainAttack
		
	def getAltAttack(self):
		return self.altAttack

	def getMainAttackName(self):
		return self.mainAttack.getName()
	
	def getAltAttackName(self):
		return self.altAttack.getName()

	def getHealth(self):
		return self.health

	def getWeakness(self):
		return self.weakness

	def getResistance(self):
		return self.resistance
	
	def getImage(self):
		return self.image
	
	def getOriginalHealth(self):
		return self.originalHealth
	
	def getDisplay(self):
		return self.display
		
	def getGreenHealthBar(self):
		return self.greenHealthBar
	
	def getRedHealthBar(self):
		return self.redHealthBar
	
	def getMainAttackUse(self):
		return self.mainAttackUse
	
	def getRetreat(self):
		return self.retreat
	
	def getHealthText(self):
		return self.healthText
	
	def getRedHealthBar(self):
		return self.redHealthBar
		
	def getInfo(self):
		'''
		Retrieves all the important information of a Pokemon for the player and returns them a dictionary
		'''
		infoDict = {}
		infoDict["Name"] = self.getName()
		infoDict["Type"] = self.getType()
		infoDict["Health"] = self.getHealth()
		infoDict["Weakness"] = self.getWeakness()
		infoDict["Resistance"] = self.getResistance()
		infoDict["Main Attack"] = self.getMainAttackName()
		infoDict["Alternative Attack"] = self.getAltAttackName()
		return infoDict
	
	def setMainAttackUse(self):
		'''
		Increments the number of times the Pokemon has used its main attack
		'''
		self.mainAttackUse += 1
	
	def setRetreat(self):
		'''Increments the number of times the Pokemon has retreated'''
		self.retreat += 1
	
	def setDisplay(self, image):
		self.display = image
	
	def setGreenHealthBar(self, rectangle):
		self.greenHealthBar = rectangle
	
	def setHealthText(self, text):
		self.healthText = text
	
	def setRedHealthBar(self, text):
		self.redHealthBar = text        
	
	def useAttack(self, attackName):
		'''Returns an attack of a Pokemon, based on an attack name given. Return False if attack name is not valid'''
		if attackName == self.mainAttack.getName():
			if self.getMainAttackUse() < 2:   #main attack can only be used twice
				self.setMainAttackUse()       #increments the counter for the number of times main attack is used
				return self.mainAttack
			else:
				print("Oh no!", self.getName(), "is not able to use this attack!")
				return False
		elif attackName == self.altAttack.getName():
			return self.altAttack
		else:
			print("Oh no!", self.getName(), "is not able to use this attack!")
			return False

	def updateHealth(self, attack):
		'''Updates the Pokemon's own health based on an attack given and the attack's type'''
		attackType = attack.getType()
		if attackType == self.getWeakness():
			self.health -= attack.getDamage() * 2
			#if the Pokemon is weak against the attack's type, damage is doubled
		elif attackType == self.getResistance():
			self.health -= attack.getDamage() / 2
			#if the Pokemon has resistance against the attack's type, damage is halved
		else:
			self.health -= attack.getDamage()
			
		if self.health <= 0:
			#prevents a Pokemon's health from becoming negative, which is important for checking the conditions for the game to end
			self.health = 0

class Pokeball:
	'''Constructs a Pokeball class, which consists of 6 Pokemon.
	Includes accessor methods for the list of Pokemons, their names and health.'''
	def __init__(self, ipokemon1, ipokemon2, ipokemon3, ipokemon4, ipokemon5, ipokemon6):
		self.pokemon1 = ipokemon1
		self.pokemon2 = ipokemon2
		self.pokemon3 = ipokemon3
		self.pokemon4 = ipokemon4
		self.pokemon5 = ipokemon5
		self.pokemon6 = ipokemon6
		self.pokeList = [self.pokemon1, self.pokemon2, self.pokemon3, self.pokemon4, self.pokemon5, self.pokemon6]
		self.nameList = [self.pokemon1.getName(), self.pokemon2.getName(),
		self.pokemon3.getName(), self.pokemon4.getName(), self.pokemon5.getName(), self.pokemon6.getName()]
		 
	def getNameList(self):
		return self.nameList
	
	def getPokeList(self):
		return self.pokeList
		
	def getPokemon(self, pokemonName):
		'''Returns a Pokemon from Pokeball based on a Pokemon's name'''
		pokemonList = self.getPokeList()
		for item in pokemonList:
			if pokemonName == item.getName():
				return item

	def getAllHealth(self):
		'''Returns all the health of the Pokemon in a Pokeball in a list'''
		healthList = []
		pokemonList = self.getPokeList()
		for pokemon in pokemonList:
			healthList.append(pokemon.getHealth())
		return healthList

def playPokemon():
	'''Allows player 1 and player 2 to play a game of Pokemon. When all the Pokemon of a player
	are defeated, the other player wins. Implemented with graphics.'''
	
	# Starts a new game and draws a pokemon battle arena on the window
	enter = input("The game is about to start! Press any key to begin")
	window = graphics.GraphWin("Pokemon Battle Arena", 700, 400)
	background = graphics.Image(graphics.Point(300, 200), "background2.gif")
	background.draw(window)
	
	# Draws 'player 1' and 'player 2' texts on the window
	player1Text = graphics.Text(graphics.Point(100, 280), "Player 1")
	player1Text.setSize(32)
	player1Text.setStyle("bold")
	player1Text.setTextColor("white")
	player2Text = graphics.Text(graphics.Point(560, 90), "Player 2")
	player2Text.setSize(32)
	player2Text.setStyle("bold")
	player2Text.setTextColor("white")
	player1Text.draw(window)
	player2Text.draw(window)
	
	# Randomly generates 2 pokeballs for the 2 players
	print("Each player will be randomly allocated 6 Pokemon.")
	print("The first player to defeat all of his/her opponent's Pokemons wins!")
	pokeball1 = generatePokeball([])
	pokeList1 = pokeball1.getPokeList()
	pokeball2 = generatePokeball(pokeList1)
	#passing pokeball1 into generatePokeball() in support module ensures that the two pokeballs will not share an identical Pokemon
	
	# Allows the two players to choose their pokemons at the start of the game
	turn = 1
	player1Pokemon = ""
	player2Pokemon = ""
	if player1Pokemon == "" and player2Pokemon == "":
		player1Pokemon = choosePokemon(pokeball1, "Player 1", window)
		player2Pokemon = computerChoosePokemon(pokeball2, pokeball1, player1Pokemon, window, "draw")
	
	# Tests whether the game has come to an end; acts as a prime for the while loop
	gameFinish = testGameFinish(pokeball1, pokeball2)

	# The game continues and the players alternate turns, until all of a player's Pokemon reach zero health
	while gameFinish[0] == False:
		if turn == 1:
			if player1Pokemon.getHealth() <= 0:   
			#if current Pokemon has been defeated, prompt player to choose a new Pokemon
				player1Pokemon = choosePokemon(pokeball1, "Player 1", window)
			elif player1Pokemon.getRetreat() < 1:  
			#if Pokemon is capable of retreating (each Pokemon can only retreat once), ask player whether they want to retreat the Pokemon
				change = input("Player 1, would you like " + player1Pokemon.getName() + " to retreat (Type 'retreat' if yes; retreat can only be used once by each Pokemon)? ")
				if change == "retreat" or change == "Retreat":
					player1Pokemon.getDisplay().undraw()   #undraw all the display features of the current Pokemon
					player1Pokemon.getRedHealthBar().undraw()
					player1Pokemon.getGreenHealthBar().undraw()
					player1Pokemon.getHealthText().undraw()
					player1Pokemon.setRetreat()
					player1Pokemon = choosePokemon(pokeball1, "Player 1", window)  #choose new Pokemon as current Pokemon
			playerTurn(player1Pokemon, player2Pokemon, "Player 1", "Player 2", window)  
			#player takes his/her turn by choosing what attack for the current Pokemon to use
			turn = 2  #switch turn over to Player 2 in the next iteration of the loop
			
		gameFinish = testGameFinish(pokeball1, pokeball2)
		if gameFinish[0] == True:
		#checks if game has finished by the end of each of Player 1's turns
			break
			
		if turn == 2:
			print("Computer's turn")
			#computer's turn follows exact same procedures as player 1's turn
			if player2Pokemon.getHealth() <= 0:
				player2Pokemon = computerChoosePokemon(pokeball2, pokeball1, player1Pokemon, window, "draw")
			elif player2Pokemon.getRetreat() < 1:
				response = computerRetreat(player2Pokemon, player1Pokemon, pokeball2, pokeball1, window)
				print("Computer chooses to", response)
				if response == "retreat":
					player2Pokemon.getDisplay().undraw()
					player2Pokemon.getRedHealthBar().undraw()
					player2Pokemon.getGreenHealthBar().undraw()
					player2Pokemon.getHealthText().undraw()
					player2Pokemon.setRetreat()
					player2Pokemon = computerChoosePokemon(pokeball2, pokeball1, player1Pokemon, window, "draw")
			computerTurn(player2Pokemon, player1Pokemon, "Player 2", "Player 1", window)
			turn = 1
		gameFinish = testGameFinish(pokeball1, pokeball2)
	
	print("The game has finished!", gameFinish[1], "is the winner!")
	
def choosePokemon(pokeball, playerNumber, window):
	'''Allows a player to choose which pokemon he wants to use and displays
	the pokemon on the window.'''
	
	# Gives the player some information about pokemons in the terminal
	print("=============\nChoose a new Pokemon!")
	print("Each pokemon has two attacks: main attack and alternative attack.")
	print("The main attack will deal more damage, and the two attacks will be of different types.")
	print("However, each Pokemon's main attack can only be used twice, so choose your attacks wisely!")
	
	# Compiles a list of the player's Pokemon that have not been defeated yet
	pokemonList = pokeball.getPokeList()
	availableList = []
	for pokemon in pokemonList:
		if pokemon.getHealth() > 0:
		#ensures only undefeated Pokemon can be chosen
			availableList.append(pokemon.getName())
	print("======= \n", playerNumber, "\nYour available pokemon are: \n", availableList)
	choice = input("Which Pokemon would you like to use? ")
	currentPokemon = pokeball.getPokemon(choice)   #sets the player's current Pokemon to the one he/she chose
	while currentPokemon == None:
		choice = input("Sorry, this Pokemon name is invalid! Choose another Pokemon: ")
		currentPokemon = pokeball.getPokemon(choice)	
	print("Your current Pokemon is", currentPokemon.getName())
	
	# Draws the pokemon, all its relevant information, such as type, weakness, resitance, and its health bar in the window
	currentPokemonHealth = currentPokemon.getHealth()
	originalHealth = currentPokemon.getOriginalHealth()
	
	currentPokemonType = currentPokemon.getType()
	currentPokemonWeakness = currentPokemon.getWeakness()
	currentPokemonResistance = currentPokemon.getResistance()
	healthInfo = "Health: " + str(currentPokemonHealth) + "\n Type: " + str(currentPokemonType) + ", Weakness: " + str(currentPokemonWeakness) + ", Resistance: " + str(currentPokemonResistance)
	#Collates all the current Pokemon's information into one string to be drawn later
	pokeImage = graphics.Image(graphics.Point(390, 300), currentPokemon.getImage())
	greenHealthBar = graphics.Rectangle(graphics.Point(540, 360), graphics.Point(540 + currentPokemonHealth, 370))
	redHealthBar = graphics.Rectangle(graphics.Point(540 + currentPokemonHealth, 360), graphics.Point(540 + currentPokemonHealth + (originalHealth - currentPokemonHealth), 370))
	healthDisplay = graphics.Text(graphics.Point(560, 345), healthInfo)
	
	greenHealthBar.setFill("green")
	healthDisplay.setTextColor("white")
	redHealthBar.setFill("red")
	currentPokemon.setDisplay(pokeImage)
	currentPokemon.setGreenHealthBar(greenHealthBar)
	currentPokemon.setHealthText(healthDisplay)
	currentPokemon.setRedHealthBar(redHealthBar)
	currentPokemon.getDisplay().draw(window)
	currentPokemon.getGreenHealthBar().draw(window)
	currentPokemon.getHealthText().draw(window)
	currentPokemon.getRedHealthBar().draw(window)
	
	# Displays all the information about the current pokemon on the terminal
	pokedex = currentPokemon.getInfo()
	print("The pokedex for your current Pokemon is:", pokedex, "\n ==============")
	enter = input("Press any key to continue")
	return currentPokemon

def playerTurn(ownPokemon, opponentPokemon, playerTurn, opponentTurn, window):
	''' Allows a player to choose an attack for his/her turn and shows the effect of the attack
	on opponent's pokemon.'''
	
	# Displays the available attacks and their damages for the current pokemon, and prompts
	# the player to choose a move for the round
	print("It is", playerTurn, "'s turn.\n", playerTurn, "'s Pokemon is", ownPokemon.getName())
	#collate all the information on the current Pokemon's attacks to display to the user
	mainAttack = ownPokemon.getMainAttackName()   
	mainDamage = ownPokemon.getMainAttack().getDamage()
	mainType = ownPokemon.getMainAttack().getType()
	altAttack = ownPokemon.getAltAttackName()
	altDamage = ownPokemon.getAltAttack().getDamage()
	altType = ownPokemon.getAltAttack().getType()
	print(ownPokemon.getName(), "'s main attack is", mainAttack, ". This attack deals", mainDamage, "damage and is of type", mainType)
	print(ownPokemon.getName(), "'s alternative attack is", altAttack, ". This attack deals", altDamage, "damage and is of type", altType)
	playerMove = input("What attack would you like " + ownPokemon.getName() + " to use? ")
	attack = ownPokemon.useAttack(playerMove)
	#Gets the attack that the player wishes to use
	while attack == False:
		playerMove = input("What other attack would you like " + ownPokemon.getName() + " to use? ")
		attack = ownPokemon.useAttack(playerMove)
	
	# Opponent's pokemon receives the attack
	originalHealth = opponentPokemon.getOriginalHealth()
	prevHealth = opponentPokemon.getHealth()
	opponentPokemon.updateHealth(attack)  #updating the opponent Pokemon's health based on the attack used
	opponentPokemonType = opponentPokemon.getType()
	opponentPokemonWeakness = opponentPokemon.getWeakness()
	opponentPokemonResistance = opponentPokemon.getResistance()
	newHealth = opponentPokemon.getHealth()
	healthInfo = "Health: " + str(newHealth) + "\n Type: " + str(opponentPokemonType) + ", Weakness: " + str(opponentPokemonWeakness) + ", Resistance: " + str(opponentPokemonResistance)
	lostHealth = originalHealth - newHealth
	
	opponentPokemon.getGreenHealthBar().undraw()   #undraw old health information displayed about opponent's Pokemon
	opponentPokemon.getRedHealthBar().undraw()
	opponentPokemon.getHealthText().undraw()
	
	# Opponent's pokemon's new health is updated on the window
	greenBlock = graphics.Rectangle(graphics.Point(100, 50), graphics.Point(100 + newHealth, 60))
	redBlock = graphics.Rectangle(graphics.Point(100 + newHealth, 50), graphics.Point(100 + newHealth + lostHealth, 60))
	healthDisplay = graphics.Text(graphics.Point(150, 30), healthInfo)
	
	greenBlock.setFill("green")
	redBlock.setFill("red")
	healthDisplay.setTextColor("white")
	opponentPokemon.setGreenHealthBar(greenBlock)
	opponentPokemon.setRedHealthBar(redBlock)
	opponentPokemon.setHealthText(healthDisplay)
	opponentPokemon.getGreenHealthBar().draw(window)
	opponentPokemon.getRedHealthBar().draw(window)
	opponentPokemon.getHealthText().draw(window)
	
	# Displays information about the attack and continues the game
	print(playerTurn, "'s", ownPokemon.getName(), "used", attack.getName(), "on", opponentTurn, "'s ", opponentPokemon.getName(), "!")
	print(opponentTurn, "'s ",opponentPokemon.getName(), "'s health has changed from", prevHealth, "to", newHealth)
	if newHealth <= 0:
	#checks if opponent's Pokemon has been defeated
		print(opponentTurn, "'s ", opponentPokemon.getName(), "has been defeated!")
		opponentPokemon.getDisplay().undraw()   #undraw all the relevant information about the opponent's Pokemon
		opponentPokemon.getGreenHealthBar().undraw()
		opponentPokemon.getRedHealthBar().undraw()
		opponentPokemon.getHealthText().undraw()
	enter = input("============== \n Press any key to continue")
	
def testGameFinish(pokeball1, pokeball2):
	''' Tests whether the game has come to an end.'''
	
	# Initializes the status of the game and the winner
	gameFinish = False
	winner = None
	
	# If player 1's pokemons have all been defeated, i.e. have zero health, game ends and player 2 is the winner
	player1HealthList = pokeball1.getAllHealth()
	player1HealthSum = 0
	for health in player1HealthList:
		player1HealthSum += health  #accumulates the health of all the Pokemon in player1's Pokeball
	if player1HealthSum <= 0:
	#if the sum of player1's Pokemon is zero, then all of his/her Pokemon must be defeated already
		gameFinish = True
		winner = "Player 2"
		
	# If player 2's pokemons have all been defeated, i.e. have zero health, game ends and player 1 is the winner
	player2HealthList = pokeball2.getAllHealth()
	player2HealthSum = 0
	for health in player2HealthList:
		player2HealthSum += health
	if player2HealthSum <= 0:
		gameFinish = True
		winner = "Player 1"

	return (gameFinish, winner)

def generatePokeball(notAvailableList):
	''' Generates a pokeball from the currently available Pokemon in supportModule.'''
	
	totalList = supportModule.returnList()
	pokemonList = supportModule.generateList([], totalList, notAvailableList)
	#Gets a list of 6 randomly chosen Pokemon to be initialized into a Pokeball. The parameter notAvailableList ensures the
	#second Pokeball that needs to be generated does not contain any Pokemon already in the first Pokeball generated.
	pokeball = Pokeball(pokemonList[0], pokemonList[1], pokemonList[2], pokemonList[3], pokemonList[4], pokemonList[5])
	return pokeball
	
'''
The following functions comprise of the artificial intelligence strategies that the computer will use

'''
def computerChoosePokemon(ownPokeball, oppPokeball, oppPokemon, window, drawOrNoDraw):
	''' Computer chooses the Pokemon that will maximize its chance of winning, according to
	the specific rules stated in #.

	The drawOrNoDraw parameter exists because in computerRetreat, where the computer chooses whether it wants to retreat its current Pokemon,
	the computer will call computerChoosePokemon to predict what Pokemon it will choose after retreating its current Pokemon. This choice is only a predict
	and not an actual move, so the display aspects of this function would have to be disabled.
	'''
	
	#generates computer's available list of Pokemon, i.e. Pokemon that have not been defeated
	pokemonList = ownPokeball.getPokeList()
	availableList = []
	nameList = []
	ownWeaknessList = []
	for pokemon in pokemonList:
		if pokemon.getHealth() > 0:
			availableList.append(pokemon)
			nameList.append(pokemon.getName())
			ownWeaknessList.append(pokemon.getWeakness())  #also compiles a list of the weaknesses of all the available Pokemon to the computer
	if drawOrNoDraw == "draw":
		print("Computer's available Pokemon are: \n", nameList)
	
	# compiles a list of opponent's undefeated Pokemon's weaknesses
	oppWeaknessList = []
	for pokemon in oppPokeball.getPokeList():
		if pokemon.getHealth() > 0:
			oppWeaknessList.append(pokemon.getWeakness())
	
	firstPriority = []
	secondPriority = []
	thirdPriority = []
	fourthPriority = []
	
	for pokemon in availableList:
		if pokemon.getType() == oppPokemon.getWeakness():
		# First priority list contains Pokemon whose types match the opponent's Pokemon's weaknesses
			firstPriority.append(pokemon)
		elif pokemon.getType() != oppPokemon.getWeakness() and pokemon.getType() in oppWeaknessList:
		#Third priority list contains Pokemon who are not effective against oppPokemon but will be effective against opponent's
		#other Pokemon(s), thus we want to save these Pokemon for later use
			thirdPriority.append(pokemon)
		elif pokemon.getWeakness() != oppPokemon.getType():
		# Second priority list contains Pokemon whose are not weak against opponent's Pokemon
			secondPriority.append(pokemon)
		else:
		# Fourth priority contains Pokemon who are weak against the opponent's current pokemon
			fourthPriority.append(pokemon)
	
	#choose out of first priority first, as those are the Pokemon that oppPokemon has weakness against
	if len(firstPriority) > 0:
		for pokemon in firstPriority:
		#Choose the Pokemon if it can finish off the opponent's Pokemon in one go
			if pokemon.getMainAttack().getDamage() * 2 > oppPokemon.getHealth():
				currentPokemon = pokemon
				if drawOrNoDraw == "draw":
					computerDrawPokemon(currentPokemon, window)
				return currentPokemon
			
		for pokemon in firstPriority:
		#Choose the Pokemon if it can survive at least 2 attacks by the opponent's Pokemon
			attackAndDamage = calculateAttackAndDamage(pokemon, oppPokemon)
			maxOppDamage = attackAndDamage[2] 
			#The most damage the opponent's Pokemon can deal to this Pokemon each turn, based on
			#opponent's attack types and this Pokemon's type
			if pokemon.getHealth() > maxOppDamage * 2:
				currentPokemon = pokemon
				if drawOrNoDraw == "draw":
					computerDrawPokemon(currentPokemon, window)
				return currentPokemon
	
		#Else, choose the Pokemon with the highest health in first priority list
		currentPokemon = highestHealthPokemon(firstPriority)
		if drawOrNoDraw == "draw":
		  computerDrawPokemon(currentPokemon, window)
		return currentPokemon
	
	elif len(secondPriority) > 0:		
		#If first priority is empty, choose out of second priority list next, which contains Pokemon
		#that does not have a weakness against the opponent's current Pokemon
		
		for pokemon in secondPriority:
		#Choose the Pokemon if it can survive at least 2 attacks by the opponent's Pokemon
			attackAndDamage = calculateAttackAndDamage(pokemon, oppPokemon)
			maxOppDamage = attackAndDamage[2]
			if pokemon.getHealth() > maxOppDamage * 2:
				currentPokemon = pokemon
				if drawOrNoDraw == "draw":
					computerDrawPokemon(currentPokemon, window)
				return currentPokemon
	
		for pokemon in secondPriority:
		#Choose the pokemon if it can defeat opponent's current pokemon in one attack
			attackAndDamage = calculateAttackAndDamage(pokemon, oppPokemon)
			ownMainAttackDamage = attackAndDamage[0]
			ownAltAttackDamage = attackAndDamage[1]
			#The amount of damage this Pokemon's attacks would deal to opponent's Pokemon, based on
			#this Pokemon's attack types and opponent Pokemon's type
			if ownMainAttackDamage > oppPokemon.getHealth() or ownAltAttackDamage > oppPokemon.getHealth():
				currentPokemon = pokemon
				if drawOrNoDraw == "draw":
					computerDrawPokemon(currentPokemon, window)
				return currentPokemon
	
		#Choose the pokemon with highest health in secondPriority list
		currentPokemon = highestHealthPokemon(secondPriority)
		if drawOrNoDraw == "draw":
			computerDrawPokemon(currentPokemon, window)
		return currentPokemon
	
	elif len(thirdPriority) > 0:
		#if secondPriority is also empty, choose out of third priority.
		for pokemon in thirdPriority:
		#If more than one Pokemon have the same weakness, choose one of these Pokemon,
		#as it is best to not save a lot of pokemon with same weakness
			if ownWeaknessList.count(pokemon.getWeakness()) > 1:
				currentPokemon = pokemon
				if drawOrNoDraw == "draw":
					computerDrawPokemon(currentPokemon, window)
				return currentPokemon
	
		#return pokemon with highest health from third priority
		currentPokemon = highestHealthPokemon(thirdPriority)
		if currentPokemon != None:
			if drawOrNoDraw == "draw":
				computerDrawPokemon(currentPokemon, window)
			return currentPokemon
	
	else:
		#if third priority is empty as well, choose pokemon with highest health out of fourth priority,
		#which is the least preferable as these Pokemon are weak against the opponent's Pokemon.
		currentPokemon = highestHealthPokemon(fourthPriority)
		if currentPokemon != None:
			if drawOrNoDraw == "draw":
				computerDrawPokemon(currentPokemon, window)
			return currentPokemon
		
def highestHealthPokemon(availableList):
	''' Chooses the Pokemon with the highest attack within available list.'''
	
	highestHealth = 0
	highestHealthPokemon = None
	for pokemon in availableList:
		if pokemon.getHealth() > highestHealth:
			highestHealth = pokemon.getHealth()  #update highest health
			highestHealthPokemon = pokemon  #keep track of the Pokemon who had the highest health
			
	return highestHealthPokemon
		
def computerDrawPokemon(currentPokemon, window):
	''' Draws the current Pokemon on the display window. '''
	print("Computer chooses", currentPokemon.getName(), "!")
	
	#Get all the relevant information about the Pokemon to display
	originalHealth = currentPokemon.getOriginalHealth()
	currentPokemonHealth = currentPokemon.getHealth()
	currentPokemonType = currentPokemon.getType()
	currentPokemonWeakness = currentPokemon.getWeakness()
	currentPokemonResistance = currentPokemon.getResistance()
	healthInfo = "Health: " + str(currentPokemonHealth) + "\n Type: " + str(currentPokemonType) + ", Weakness: " + str(currentPokemonWeakness) + ", Resistance: " + str(currentPokemonResistance)
	lostHealth = originalHealth - currentPokemonHealth
	
	pokeImage = graphics.Image(graphics.Point(335, 90), currentPokemon.getImage())
	greenHealthBar = graphics.Rectangle(graphics.Point(100, 50), graphics.Point(100 + currentPokemonHealth, 60))
	redHealthBar = graphics.Rectangle(graphics.Point(100 + currentPokemonHealth, 50), graphics.Point(100 + currentPokemonHealth + lostHealth, 60))
	healthDisplay = graphics.Text(graphics.Point(150, 30), healthInfo)
	
	greenHealthBar.setFill("green")
	healthDisplay.setTextColor("white")
	redHealthBar.setFill("red")
	currentPokemon.setDisplay(pokeImage)
	currentPokemon.setGreenHealthBar(greenHealthBar)
	currentPokemon.setHealthText(healthDisplay)
	currentPokemon.setRedHealthBar(redHealthBar)
	currentPokemon.getDisplay().draw(window)
	currentPokemon.getGreenHealthBar().draw(window)
	currentPokemon.getHealthText().draw(window)
	currentPokemon.getRedHealthBar().draw(window)
	
	pokedex = currentPokemon.getInfo()
	print("The pokedex for computer's current Pokemon is:", pokedex, "\n ==============")
	enter = input("Press enter to continue")

def computerTurn(ownPokemon, opponentPokemon, playerTurn, opponentTurn, window):
	''' Computer chooses what attack for its current Pokemon to use, based on what the opponent's current Pokemon is. '''
	
	ownHealth = ownPokemon.getHealth()
	opponentHealth = opponentPokemon.getHealth()
	attackAndDamage = calculateAttackAndDamage(ownPokemon, opponentPokemon)
	#Returns a tuple containing three values: the damage each of the Pokemon's two attacks would deal,
	#and how much maximum damage the opponent's Pokemon can cause to the current Pokemon in one turn, based
	#on current Pokemon's attack types and opponent's Pokemon's type.
	ownMainAttackDamage = attackAndDamage[0]
	ownAltAttackDamage = attackAndDamage[1]
	maxOppDamage = attackAndDamage[2]

	#if main attack unavailable, use alt attack
	if ownPokemon.getMainAttackUse() > 1:
		attack = ownPokemon.useAttack(ownPokemon.getAltAttack().getName())

	#if alt attack will defeat opponent, use alt attack and save main attack
	elif ownAltAttackDamage > opponentHealth:
		attack = ownPokemon.useAttack(ownPokemon.getAltAttack().getName())
	
	#if alt attack can't kill opponent in one go main attack can, use main attack
	elif ownMainAttackDamage > opponentHealth:
		attack = ownPokemon.useAttack(ownPokemon.getMainAttack().getName())
	
	#if ownPokemon will be defeated by the opponent's most damage inflicting attack next turn, use main attack, as ownPokemon will not
	#have chance to use main attack again
	elif ownHealth < maxOppDamage:
		attack = ownPokemon.useAttack(ownPokemon.getMainAttack().getName())
	
	#if opponent can be defeated either within two main attacks (but not one) and within 2 alt attacks,
	#use alt attack to save main attack, as defeating the opponent will need two of either attacks regardless
	elif ownMainAttackDamage * 2 > opponentHealth and ownAltAttackDamage * 2 > opponentHealth:
		attack = ownPokemon.useAttack(ownPokemon.getAltAttack().getName())
	
	#if alt attack damage > main attack damage, maybe for example if alt attack type is opponent's weakness, use alt attack
	elif ownMainAttackDamage <= ownAltAttackDamage:
		attack = ownPokemon.useAttack(ownPokemon.getAltAttack().getName())

	#else, if main attack causes more damage than alt attack, use main attack to deal more damage
	else:
		attack = ownPokemon.useAttack(ownPokemon.getMainAttack().getName())

	# displays opponent's Pokemon and its updated health, type, weakness and resistance on the window
	originalHealth = opponentPokemon.getOriginalHealth()
	opponentPokemon.updateHealth(attack)
	opponentPokemonType = opponentPokemon.getType()
	opponentPokemonWeakness = opponentPokemon.getWeakness()
	opponentPokemonResistance = opponentPokemon.getResistance()
	newHealth = opponentPokemon.getHealth()
	healthInfo = "Health: " + str(newHealth) + "\n Type: " + str(opponentPokemonType) + ", Weakness: " + str(opponentPokemonWeakness) + ", Resistance: " + str(opponentPokemonResistance)
	lostHealth = originalHealth - newHealth
	
	opponentPokemon.getGreenHealthBar().undraw()
	opponentPokemon.getRedHealthBar().undraw()
	opponentPokemon.getHealthText().undraw()
	
	greenBlock = graphics.Rectangle(graphics.Point(540, 360), graphics.Point(540 + newHealth, 370))
	redBlock = graphics.Rectangle(graphics.Point(540 + newHealth, 360), graphics.Point(540 + newHealth + lostHealth, 370))
	healthDisplay = graphics.Text(graphics.Point(560, 345), healthInfo)
	
	greenBlock.setFill("green")
	redBlock.setFill("red")
	healthDisplay.setTextColor("white")
	opponentPokemon.setGreenHealthBar(greenBlock)
	opponentPokemon.setRedHealthBar(redBlock)
	opponentPokemon.setHealthText(healthDisplay)
	opponentPokemon.getGreenHealthBar().draw(window)
	opponentPokemon.getRedHealthBar().draw(window)
	opponentPokemon.getHealthText().draw(window)
	
	print(playerTurn, "'s", ownPokemon.getName(), "used", attack.getName(), "on", opponentTurn, "'s ", opponentPokemon.getName(), "!")
	print(opponentTurn, "'s ",opponentPokemon.getName(), "'s health has changed from", opponentHealth, "to", newHealth)
	if newHealth <= 0:
	#if opponent's Pokemon is defeated as a result, undraw all visual aspects of opponent's Pokemon
		print(opponentTurn, "'s ", opponentPokemon.getName(), "has been defeated!")
		opponentPokemon.getDisplay().undraw()
		opponentPokemon.getGreenHealthBar().undraw()
		opponentPokemon.getRedHealthBar().undraw()
		opponentPokemon.getHealthText().undraw()
	
	print("=========")
	enter = input("Press any key to continue")

def computerRetreat(ownPokemon, opponentPokemon, ownPokeball, opponentPokeball, window):
	''' Allows the computer to choose whether to retreat a Pokemon.'''
	response = "not retreat"   #initiliazed default response
	
	attackAndDamage = calculateAttackAndDamage(ownPokemon, opponentPokemon)
	ownMainAttackDamage = attackAndDamage[0]
	ownAltAttackDamage = attackAndDamage[1]
	maxOppDamage = attackAndDamage[2]
	ownAttackDamages = [ownMainAttackDamage, ownAltAttackDamage]
	bestAttack = max(ownAttackDamages)  #find which attack out of main and alt attack causes more damage
	
	pokemonList = ownPokeball.getPokeList()
	if bestAttack < opponentPokemon.getHealth() and maxOppDamage >= ownPokemon.getHealth():
	#if best attack can't kill opponent in one go, and opponent will kill self in one turn, retreat
		response = "retreat"
	
	elif bestAttack < opponentPokemon.getHealth():
	# if current Pokemon cannot kill opponent's Pokemon in one go, and if computer has another Pokemon in its Pokeball that
	# has low health and can defeat opponent's Pokemon in one attack, retreat current Pokemon, assuming computerChoosePokemon
	# will choose that low health Pokemon subsequently.
	# i.e. the low health Pokemon will be able to have more impact before being defeated and also saves current Pokemon's main attack
		for pokemon in pokemonList:
			if pokemon.getHealth() < 15:  #arbitrary value for low health
				attackAndDamage = calculateAttackAndDamage(pokemon, opponentPokemon)
				ownMainAttackDamage = attackAndDamage[0]
				ownAltAttackDamage = attackAndDamage[1]
				if ownMainAttackDamage > opponentPokemon.getHealth() or ownAltAttackDamage > opponentPokemon.getHealth(): 
					response = "retreat"

	elif ownPokemon.getWeakness() == opponentPokemon.getType():
	#if the current Pokemon is weak against opponent's current Pokemon, then retreat
		response = "retreat" 
	
	if response == "retreat":
		#checks what the computer will choose if it chooses to retreat the current Pokemon. If the computer will
		#choose the current Pokemon again after retreating it, which is possible given the rules in
		#computerChoosePokemon, then change response to not retreat current Pokemon.
		chosenPokemon = computerChoosePokemon(ownPokeball, opponentPokeball, opponentPokemon, window, "noDraw")
		if chosenPokemon == ownPokemon:
			response = "not retreat"
	
	return response
	
def calculateAttackAndDamage(ownPokemon, opponentPokemon):
	''' Calculates the damage ownPokemon's main and alt attacks would deal to opponentPokemon, and the maximum
	 damage the opponentPokemon could deal to ownPokemon, based on each attack's type and each Pokemon's weaknesses / resistances.
	 Returns the three values in a tuple.'''
	
	opponentHealth = opponentPokemon.getHealth()
	ownHealth = ownPokemon.getHealth()
	ownMainAttackName = ownPokemon.getMainAttackName()
	ownAltAttackName = ownPokemon.getAltAttackName()
	ownMainAttackDamage = ownPokemon.getMainAttack().getDamage()
	ownAltAttackDamage = ownPokemon.getAltAttack().getDamage()
	ownMainAttackType = ownPokemon.getMainAttack().getType()
	ownAltAttackType = ownPokemon.getAltAttack().getType()
	oppMainAttackDamage = opponentPokemon.getMainAttack().getDamage()
	oppAltAttackDamage = opponentPokemon.getAltAttack().getDamage()
	oppMainAttackType = opponentPokemon.getMainAttack().getType()
	oppAltAttackType = opponentPokemon.getAltAttack().getType()

	if ownMainAttackType == opponentPokemon.getWeakness():
		ownMainAttackDamage *= 2
	elif ownMainAttackType == opponentPokemon.getResistance():
		ownMainAttackDamage /= 2
	if ownAltAttackType == opponentPokemon.getResistance():
		ownAltAttackDamage /= 2
	elif ownAltAttackType == opponentPokemon.getWeakness():
		ownAltAttackDamage *= 2
	
	# Calculates the opponent's Pokemon's maximum damage
	damageList = []
	if ownPokemon.getResistance() == oppMainAttackType:
		damageList.append(oppMainAttackDamage / 2)
	elif ownPokemon.getWeakness() == oppMainAttackType:
		damageList.append(oppMainAttackDamage * 2)
	else:
		damageList.append(oppMainAttackDamage)
	if ownPokemon.getResistance() == oppAltAttackType:
		damageList.append(oppAltAttackDamage / 2)
	elif ownPokemon.getWeakness() == oppAltAttackType:
		damageList.append(oppAltAttackDamage * 2)
	else:
		damageList.append(oppAltAttackDamage)
	maxOppDamage = max(damageList)
	
	return (ownMainAttackDamage, ownAltAttackDamage, maxOppDamage)
	
if __name__ == "__main__":
    playPokemon()
