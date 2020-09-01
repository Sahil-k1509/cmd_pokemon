from pokeworld import pokemonWorld, small_pokemons, legendary_pokemons
from pokemon import Pokemon

import os
import sys
import pickle
from time import sleep
from math import floor
from random import randint, random, choice
from os import system as OSsys, name as OSname

from colorama import init as initializeColor, Fore, Back, Style
from termcolor import colored

initializeColor()



def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)

def clearScreen():
    if OSname == 'nt': OSsys('cls')
    else: OSsys('clear')
    pprint()
    pprint()


def save_game(player):
    with open('pokemon_progress.pkl', 'wb') as output:
        pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
                
def load_game():
    with open('pokemon_progress.pkl', 'rb') as inputf:
        player = pickle.load(inputf)
    print(player)
    return player


def pokemon_duel(player, opponent, battle='wild'):
    battleOver = False
    
    
    if battle != 'wild': opp = opponent.name + "'s"
    else: opp = 'wild'
    
    while not battleOver:
        escapeProb = random()
        
        if battle != 'wild': opponent.currentPokemon.displayStats(trainer=opp)
        else: opponent.displayStats(trainer=opp)
        pprint()
        player.currentPokemon.displayStats()
        
        pprint('\n\n')
        pprint("(F)ight"); sleep(1)
        pprint("(S)witch pokemon"); sleep(1)
        if battle == 'wild':
            pprint("(T)hrow pokeball"); sleep(1)
            pprint("(E)scape"); sleep(1)

        pprint('\n\n')
        pprint("What would you like to do? (Wrong option will result in you skipping your turn.)", end=' ')
        whatTodo = input()
        
        if battle == 'wild':
            
            if whatTodo in ['e', 'E']:
                escapeLuck = random()
                if escapeLuck >= escapeProb:
                    clearScreen()
                    pprint("Escaped Successfully..."); sleep(1.8)
                    battleOver = True
                    return None
                else:
                    pprint("couldn't escape..\n\n"); sleep(1.8)
            
            if whatTodo in ['t', 'T']:
                if player.catchPokemon(opponent):
                    battleOver = True
                    clearScreen()
                    return None
            
            if whatTodo in ['s', 'S']:
                if not player.switchPokemon():
                    battleOver = True
                    return (opponent.name, player)
                
        
            i = 0
            attackInd = randint(0, len(opponent.attacks)-i-1)
            while opponent.attacks[attackInd] is None:
                attackInd = randint(0, len(opponent.attacks)-i-1)
                i+=1
            attackOpp = opponent.attacks[attackInd]
            
            if whatTodo not in ['f', 'F']:
                opponent.attack(player.currentPokemon, attackInd)
                if player.currentPokemon.health <= 0:
                    pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                    if not player.switchPokemon():
                        return (opponent.name, player)
                    
            else:
                pprint("Choose Your Attack: ", end=' '); sleep(1.8)
                attackpl = int(input()) - 1
                while True:
                    if attackpl not in [0, 1, 2, 3]:
                        sleep(1.2)
                        pprint("Invalid choice... Choose again : ", end='') 
                        attackpl = int(input())-1
                    elif player.currentPokemon.attacks[attackpl] is None:
                        sleep(1.2)
                        pprint("You haven't learnt any attack for that slot... Choose again: ", end='')
                        attackpl = int(input())-1
                    elif player.currentPokemon.attacks[attackpl].count == 0:
                        sleep(1.2)
                        pprint("You can't use that attack anymore... Choose again: ", end='')
                        attackpl = int(input())-1
                    else:
                        sleep(1.2)
                        break
                
                attackplayer = player.currentPokemon.attacks[attackpl]
                if attackplayer.name == 'quick attack' and attackOpp.name != 'quick attack':
                    player.currentPokemon.attack(opponent, attackpl)
                    sleep(1.2)
                    if opponent.health > 0: 
                        opponent.attack(player.currentPokemon, attackInd)
                    else:
                        if player.currentPokemon.health <= 0:
                            pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                            if not player.switchPokemon():
                                return (opponent.name, player)    
                        
                elif attackplayer.name != 'quick attack' and attackOpp.name == 'quick attack':
                    opponent.attack(player.currentPokemon, attackInd)
                    sleep(1.2)
                    
                    if player.currentPokemon.health > 0: 
                        player.currentPokemon.attack(opponent, attackpl)
                    
                    if player.currentPokemon.health <= 0:
                        pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                        if not player.switchPokemon():
                            return (opponent.name, player)
                        
                else:
                    if player.currentPokemon.speed >= opponent.speed:
                        player.currentPokemon.attack(opponent, attackpl)
                        sleep(1.2)
                        if opponent.health > 0: 
                            opponent.attack(player.currentPokemon, attackInd)
                        else:
                            if player.currentPokemon.health <= 0:
                                pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                                if not player.switchPokemon():
                                    return (opponent.name, player)  
                    else:
                        opponent.attack(player.currentPokemon, attackInd)
                        sleep(1.2)
                        if player.currentPokemon.health > 0: 
                            player.currentPokemon.attack(opponent, attackpl)
                        
                        if player.currentPokemon.health <= 0:
                            pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                            if not player.switchPokemon():
                                return (opponent.name, player)
            
            if opponent.health <= 0:
                sleep(1.2)
                pprint(f"wild {opponent.name} fainted"); sleep(1.2)
                pprint("You won the battle!!!\n"); sleep(1.2)
                battleOver = True            
                player.currentPokemon.gain_exp(opponent, battletype=battle); sleep(1.2)
                return (player.name, player)
        
        else:
            
            if whatTodo in ['s', 'S']:
                if not player.switchPokemon():
                    battleOver = True
                    pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(1.1)
                    player.money -= 0.15*player.money
                    player.money = max(0, player.money) 
                    return (opponent.name, player)
                
        
            i = 0
            attackInd = randint(0, len(opponent.currentPokemon.attacks)-i-1)
            while opponent.currentPokemon.attacks[attackInd] is None:
                attackInd = randint(0, len(opponent.currentPokemon.attacks)-i-1)
                i+=1
            attackOpp = opponent.currentPokemon.attacks[attackInd]
            
            if whatTodo not in ['f', 'F']:
                opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                if player.currentPokemon.health <= 0:
                    pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                    if not player.switchPokemon():
                        pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(2)
                        player.money -= 0.15*player.money
                        player.money = max(0, player.money) 
                        return (opponent.name, player)
                    
            else:
                pprint("Choose Your Attack: ", end=' '); sleep(1.8)
                attackpl = int(input()) - 1
                while True:
                    if attackpl not in [0, 1, 2, 3]:
                        sleep(1.2)
                        pprint("Invalid choice... Choose again : ", end='') 
                        attackpl = int(input())-1
                    elif player.currentPokemon.attacks[attackpl] is None:
                        sleep(1.2)
                        pprint("You haven't learnt any attack for that slot... Choose again: ", end='')
                        attackpl = int(input())-1
                    elif player.currentPokemon.attacks[attackpl].count == 0:
                        sleep(1.2)
                        pprint("You can't use that attack anymore... Choose again: ", end='')
                        attackpl = int(input())-1
                    else:
                        sleep(1.2)
                        break
                
                attackplayer = player.currentPokemon.attacks[attackpl]
                if attackplayer.name == 'quick attack' and attackOpp.name != 'quick attack':
                    player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                    sleep(1.2)
                    if opponent.currentPokemon.health > 0: 
                        opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                    else:
                        if player.currentPokemon.health <= 0:
                            pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                            if not player.switchPokemon():
                                pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(2)
                                player.money -= 0.15*player.money
                                player.money = max(0, player.money) 
                                return (opponent.name, player)    
                        
                elif attackplayer.name != 'quick attack' and attackOpp.name == 'quick attack':
                    opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                    sleep(1.2)
                    
                    if player.currentPokemon.health > 0: 
                        player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                    
                    if player.currentPokemon.health <= 0:
                        pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                        if not player.switchPokemon():
                            pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(2)
                            player.money -= 0.15*player.money
                            player.money = max(0, player.money) 
                            return (opponent.name, player)
                        
                else:
                    if player.currentPokemon.speed >= opponent.currentPokemon.speed:
                        player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                        sleep(1.2)
                        if opponent.currentPokemon.health > 0: 
                            opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                        else:
                            if player.currentPokemon.health <= 0:
                                pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                                if not player.switchPokemon():
                                    pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(2)
                                    player.money -= 0.15*player.money
                                    player.money = max(0, player.money) 
                                    return (opponent.name, player)  
                    else:
                        opponent.currentPokemon.attack(player.currentPokemon, attackInd)
                        sleep(1.2)
                        if player.currentPokemon.health > 0: 
                            player.currentPokemon.attack(opponent.currentPokemon, attackpl)
                        
                        if player.currentPokemon.health <= 0:
                            pprint(f"{player.currentPokemon.name} fainted..."); sleep(2)
                            if not player.switchPokemon():
                                pprint(f"{player.name} gave {opponent.name},  {floor(player.money*0.15)} as a reward for losing against him..."); sleep(2)
                                player.money -= 0.15*player.money
                                player.money = max(0, player.money) 
                                return (opponent.name, player)
            
            if opponent.currentPokemon.health <= 0:
                sleep(1.5)
                pprint(f"{opponent.name}'s {opponent.currentPokemon.name} fainted")
                if not opponent.switchPokemon():
                    sleep(1.5)
                    pprint("You won the battle!!!\n"); sleep(1.4)
                    battleOver = True            
                    player.currentPokemon.gain_exp(opponent.currentPokemon, battletype=battle); sleep(1.2)
                    player.money += 0.15*opponent.money
                    pprint(f"{opponent.name} gave {player.name}, {floor(opponent.money*0.15)} as a reward for losing against him..."); sleep(2)
                    return (player.name, player)
        sleep(3)
        clearScreen()    


routes = {
        'Pallet Town': ['Viridian City', 'Cinnabar Island'],   
        'Viridian City': ['Pallet Town', 'Victory Road', 'Viridian Forest'],   
        'Victory Road': ['Viridian City', 'Indigo Plateau', 'Horizon'],   
        'Horizon': ['Victory Road'],   
        'Viridian Forest': ['Viridian City', 'Pewter City'],   
        'Pewter City': ['Viridian Forest', 'Mt. Moon'],   
        'Mt. Moon': ['Pewter City', 'Mt. Top', 'Cerulean City'],   
        'Mt. Top': ['Mt. Moon'],   
        'Cerulean City': ['Saffron City', 'Mt. Moon', 'Lavender Town'],   
        'Lavender Town': ['Cerulean City', 'Vermillion City', 'Outskirts'],   
        'Outskirts': ['Lavender Town'],   
        'Saffron City': ['Lavender Town', 'Cerulean City', 'Vermillion City', 'Celadon City'],   
        'Vermillion City': ['Saffron City', 'Lavender Town', 'Fuschia City'],   
        'Celadon City': ['Saffron City', 'Fuschia City'],   
        'Fuschia City': ['Celadon City', 'Vermillion City', 'Seafoam Island'],   
        'Seafoam Island': ['Fuschia City', 'Cinnabar Island'],   
        'Cinnabar Island': ['Pallet Town', 'Volcano'],   
        'Volcano': ['Cinnabar Island'] 
}


def palletTown(player):
    return player


def viridianCity(player):
    return player


def viridianForest(player):
    return player


def pewterCity(player):
    return player


def mtMoon(player):
    return player


def mtTop(player):
    return player


def ceruleanCity(player):
    return player


def vermilionCity(player):
    return player


def fuschiaCity(player):
    return player


def saffronCity(player):
    return player


def lavenderTown(player):
    return player


def outskirts(player):
    return player


def celadonCity(player):
    return player


def seafoamIsland(player):
    return player


def cinnabarIsland(player):
    return player


def volcano(player):
    return player


def indigoPlateau(player):
    return player


def victoryRoad(player):
    return player


def horizon(player):
    return player



def main_game(player):
    return