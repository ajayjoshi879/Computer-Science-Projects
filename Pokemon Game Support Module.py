'''
Support Module for Pokemon Game
This module contains premade Attack and Pokemon objects that will be used by the finalProject module
to play Pokemon.

This module also contains functions to help create randomized lists of Pokemon to help make Pokeballs.

By Hazel Que and Andrew Qi
'''


import finalProject
from finalProject import *
import random

		
'''
List of all possible attackes usable for playPokemon
'''
flameThrower = Attack("Flame Thrower", "fire", 30)
fieryDance = Attack("Fiery Dance", "fire", 23)
seismicToss = Attack("Seismic Toss", "ground", 25)
dig = Attack("Dig", "ground", 27)
waterGun = Attack("Water Gun", "water", 20)
bubble = Attack("Bubble", "water", 29)
thunderBolt = Attack("Thunderbolt", "electric", 28)
charge = Attack("Charge", "electric", 26)
ironTail = Attack("Iron Tail", "normal", 24)
highSpeedMovement = Attack("High Speed Movement", "normal", 22)
tackle = Attack("Tackle", "normal", 18)
flyingLeaves = Attack("Flying Leaves", "grass", 24)
vineWhip = Attack("Vine Whip", "grass", 30)
sting = Attack("Sting", "grass", 24)
wingAttack = Attack("Wing Attack", "flying", 26)
flash = Attack("Flash", "normal", 30)
tornado = Attack("Tornado", "normal", 25)
poisonSting = Attack("Poison Sting", "poison", 27)
scare = Attack("Scare", "normal", 22)
hyperBeam = Attack("Hyper Beam", "fire", 38)
ram = Attack("Ram", "ground", 20)
bodySlam = Attack("Body Slam", "normal", 23)
anger = Attack("Anger", "psychic", 22)
bounce = Attack("Bounce", "normal", 18)
sonicBeam = Attack("Sonic Beam", "flying", 32)
stink = Attack("Stink", "poison", 30)
earthquake = Attack("Earthquake", "ground", 38)
scratch = Attack("Scratch", "fighting", 22)
bite = Attack("Bite", "fighting", 24)
hypnosis = Attack("Hypnosis", "psychic", 33)
punch = Attack("Punch", "fighting", 26)
psychicAttack = Attack("Psychic Attack", "psychic", 18)
roll = Attack("Roll", "normal", 23)
mudBullets = Attack("Mud Bullets", "poison", 20)
explode = Attack("Explode", "electric", 35)
poisonGas = Attack("Poison Gas", "poison", 24)
iceBeam = Attack("Ice Beam", "water", 37)
slice = Attack("Slice", "fighting", 27)
pinch = Attack("Pinch", "normal", 25)
dragonsRoar = Attack("Dragon's Roar", "normal", 36)
solarBeam = Attack("Solar Beam", "grass", 32)
flash = Attack("Flash", "normal", 21)

'''
List of all possible Pokemon a player can get allocated in playPokemon
'''
charizard = Pokemon("Charizard", "fire", "water", "grass", flameThrower, seismicToss, 120, 120, "charizard.gif")
squirtle = Pokemon("Squirtle", "water", "electric", "fire", bubble, waterGun, 65, 65, "squirtle.gif")
pikachu = Pokemon("Pikachu", "electric", "ground", "water", thunderBolt, ironTail, 55, 55, "pikachu.gif")
hitmonlee = Pokemon("Hitmonlee", "fighting", "poison", "flying", punch, highSpeedMovement, 50, 50, "hitmonlee.gif")
bulbasaur = Pokemon("Bulbasaur", "grass", "fire", "normal", vineWhip, flyingLeaves, 45, 45, "bulbasaur.gif")
butterfree = Pokemon("Butterfree", "flying", "fighting", "ground", wingAttack, tackle, 60, 60, "butterfree.gif") 
beedrill = Pokemon("Beedrill", "flying", "fighting", "ground", wingAttack, sting, 65, 65, "beedrill.gif") 
pidgeot = Pokemon("Pidgeot", "flying", "fighting", "ground", sonicBeam, tornado, 83, 83, "pidgeot.gif") 
rattata = Pokemon("Rattata", "normal", "grass", "psychic", dragonsRoar, bite, 30, 30, "rattata.gif") 
arbok = Pokemon("Arbok", "poison", "psychic", "fighting", poisonSting, scare, 60, 60, "arbok.gif") 
sandshrew = Pokemon("Sandshrew", "ground", "flying", "electric", dig, tackle, 50, 50, "sandshrew.gif") 
nidoqueen = Pokemon("Nidoqueen", "ground", "flying", "electric", earthquake, bodySlam, 90, 90, "nidoqueen.gif") 
nidoking = Pokemon("Nidoking", "ground", "flying", "electric", earthquake, ram, 81, 81, "nidoking.gif") 
vulpix = Pokemon("Vulpix", "fire", "water", "grass", flameThrower, ironTail, 38, 38, "vulpix.gif") 
jigglypuff = Pokemon("Jigglypuff", "normal", "grass", "psychic", pinch, bounce, 115, 115, "jigglypuff.gif") 
zubat = Pokemon("Zubat", "flying", "fighting", "ground", sonicBeam, wingAttack, 40, 40, "zubat.gif") 
gloom = Pokemon("Gloom", "grass", "fire", "normal", solarBeam, flyingLeaves, 60, 60, "gloom.gif") 
venomoth = Pokemon("Venomoth", "flying", "fighting", "ground", wingAttack, highSpeedMovement, 70, 70, "venomoth.gif") 
diglett = Pokemon("Diglett", "ground", "flying", "electric", earthquake, dig, 50, 50, "diglett.gif") 
meowth = Pokemon("Meowth", "normal", "grass", "psychic", pinch, scratch, 65, 65, "meowth.gif")
psyduck = Pokemon("Psyduck", "psychic", "normal", "poison", hypnosis, waterGun, 50, 50, "psyduck.gif") 
growlithe = Pokemon("Growlithe", "fire", "water", "grass", flameThrower, fieryDance, 55, 55, "growlithe.gif") 
primeape = Pokemon("Primeape", "fighting", "poison", "flying", punch, seismicToss, 65, 65, "primeape.gif") 
alakazam = Pokemon("Alakazam", "psychic", "normal", "poison", hypnosis, psychicAttack, 85, 85, "alakazam.gif") 
machop = Pokemon("Machop", "fighting", "poison", "flying", punch, seismicToss, 70, 70, "machop.gif") 
tentacruel = Pokemon("Tentacruel", "poison", "psychic", "fighting", poisonGas, waterGun, 80, 80, "tentacruel.gif") 
golem = Pokemon("Golem", "ground", "flying", "electric", earthquake, roll, 80, 80, "golem.gif") 
slowpoke = Pokemon("Slowpoke", "water", "electric", "fire", waterGun, tackle, 90, 90, "slowpoke.gif") 
magnemite = Pokemon("Magnemite", "electric", "ground", "water", thunderBolt, charge, 25, 25, "magnemite.gif")
dewgong = Pokemon("Dewgong", "water", "electric", "fire", iceBeam, waterGun, 90, 90, "dewgong.gif") 
muk = Pokemon("Muk", "poison", "psychic", "fighting", stink, mudBullets, 75, 75, "muk.gif") 
gastly = Pokemon("Gastly", "psychic", "normal", "poison", hypnosis, scare, 30, 30, "gastly.gif") 
onix = Pokemon("Onix", "ground", "flying", "electric", earthquake, ram, 35, 35, "onix.gif") 
electrode = Pokemon("Electrode", "electric", "ground", "water", explode, charge, 60, 60, "electrode.gif") 
exeggutor = Pokemon("Exeggutor", "grass", "fire", "normal", solarBeam, flyingLeaves, 75, 75, "exeggutor.gif") 
koffing = Pokemon("Koffing", "poison", "psychic", "fighting", poisonGas, tackle, 45, 45, "koffing.gif") 
seadra = Pokemon("Seadra", "water", "electric", "fire", iceBeam, waterGun, 55, 55, "seadra.gif") 
rhydon = Pokemon("Rhydon", "ground", "flying", "electric", earthquake, flash, 80, 80, "rhydon.gif") 
staryu = Pokemon("Staryu", "water", "electric", "fire", waterGun, tackle, 35, 35, "staryu.gif") 
scyther = Pokemon("Scyther", "grass", "fire", "normal", solarBeam, highSpeedMovement, 60, 60, "scyther.gif") 
electabuzz = Pokemon("Electabuzz", "electric", "ground", "water", thunderBolt, seismicToss, 65, 65, "electabuzz.gif") 
magmar = Pokemon("Magmar", "fire", "water", "grass", flameThrower, fieryDance, 65, 65, "magmar.gif") 
pinsir = Pokemon("Pinsir", "ground", "flying", "electric", seismicToss, anger, 65, 65, "pinsir.gif") 
tauros = Pokemon("Tauros", "normal", "grass", "psychic", dragonsRoar, tackle, 75, 75, "tauros.gif") 
gyarados = Pokemon("Gyarados", "water", "electric", "fire", bubble, waterGun, 95, 95, "gyarados.gif") 
ditto = Pokemon("Ditto", "normal", "grass", "psychic", pinch, tackle, 48, 48, "ditto.gif") 
kabuto = Pokemon("Kabuto", "fighting", "poison", "flying", slice, highSpeedMovement, 30, 30, "kabuto.gif") 
eevee = Pokemon("Eevee", "normal", "grass", "psychic", bodySlam, flash, 55, 55, "eevee.gif") 
vaporeon = Pokemon("Vaporean", "water", "electric", "fire", iceBeam, waterGun, 130, 130, "vaporeon.gif") 
jolteon = Pokemon("Jolteon", "electric", "ground", "water", thunderBolt, charge, 65, 65, "jolteon.gif") 
floette = Pokemon("Floette", "grass", "fire", "normal", solarBeam, flyingLeaves, 54, 54, "floette.gif") 
aerodactyl = Pokemon("Aerodactyl", "flying", "fighting", "ground", sonicBeam, wingAttack, 50, 50, "aerodactyl.gif") 
snorlax = Pokemon("Snorlax", "normal", "grass", "psychic", pinch, bodySlam, 160, 160, "snorlax.gif") 
articuno = Pokemon("Articuno", "water", "electric", "fire", iceBeam, charge, 80, 80, "articuno.gif") 
zapdos = Pokemon("Zapdos", "electric", "ground", "water", thunderBolt, charge, 80, 80, "zapdos.gif") 
moltres = Pokemon("Moltres", "fire", "water", "grass", flameThrower, flash, 95, 95, "moltres.gif") 
mew = Pokemon("Mew", "normal", "grass", "psychic", dragonsRoar, psychicAttack, 100, 100, "mew.gif") 

#water, resistance = fire, weakness = electric
#fire, resistance = grass, weakness = water
#electric, resistance = water, weakness = ground
#ground, resistance = electric, weakness = flying
#normal, resistance = psychic, weakness = grass
#fighting, resistance = flying, weakness = poison
#poison, resistance = fighting, weakness = psychic
#flying, resistance = ground, weakness = fighting
#psychic, resistance = poison, weakness = normal
#grass,  resistance = normal, weakness = fire

totalList = [charizard, squirtle, pikachu, hitmonlee, bulbasaur, butterfree, beedrill, pidgeot, rattata,
arbok, sandshrew, nidoqueen, nidoking, vulpix, jigglypuff, zubat, gloom, venomoth, diglett, meowth,
psyduck, growlithe, primeape, alakazam, machop, tentacruel, golem, slowpoke, magnemite, dewgong, muk,
gastly, onix, electrode, exeggutor, koffing, seadra, rhydon, staryu, scyther, electabuzz, magmar, pinsir,
tauros, gyarados, ditto, kabuto, eevee, vaporeon, jolteon, floette, aerodactyl, snorlax, articuno, zapdos,
moltres, mew]

def returnList():
    '''Returns totalList, which is a list that contains all the Pokemon in supportModule'''
    
    return totalList

def generateList(pokemonList, totalList, notAvailableList):
    '''Generates a random list of 6 Pokemon using the random module and recursion.
    This list helps the creation of a Pokeball for the Pokemon game.
    
    By passing Pokeball1's Pokemon list into this function as notAvailableList, this ensures that
    the new list generated for Pokeball2 will not contain the same Pokemon as in Pokeball1.'''
    
    if len(pokemonList) == 6:
        return pokemonList
    else:
        int = random.randint(0, len(totalList) - 1)
        pokemon = totalList[int]
        if pokemon not in notAvailableList:
            pokemonList.append(pokemon)
            totalList = totalList[:int] + totalList[int+1:]   #removes the chosen Pokemon from the list of available choices to avoid duplicates
        return generateList(pokemonList, totalList, notAvailableList)
