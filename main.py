import pickle

from player import PokemonTrainer
from pokeworld import pokemonWorld
from pokemon import Pokemon
from npc import Gary


from time import sleep
from math import floor
from random import randint, random, choice
import os
import sys
from os import system as OSsys, name as OSname

from colorama import init as initializeColor, Fore, Back, Style
from termcolor import colored

initializeColor()
# print(Fore.RED + 'some red')
# print(Back.GREEN + 'green background')
# print(Style.DIM + 'dim text')
# print(Style.RESET_ALL)

# print(colored('Hello', 'green', 'on_red'))

"""
Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.
"""


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)

def clearScreen():
    if OSname == 'nt': OSsys('cls')
    else: OSsys('clear')
    pprint()
    pprint()

def main_menu():
    pprint(); sleep(1.5)
    pprint("(N)ew Game"); sleep(1.5)
    pprint("(L)oad Game"); sleep(1.5)
    pprint("(E)xit"); sleep(1.5)
    
    pprint()
    pprint("New Game will overwrite any previously loaded game..."); sleep(1.5)
    pprint('What would you like to do?', end=' ')
    response = input()
    
    if response in ['e', 'E']:
        pprint()
        pprint("Exiting the game...."); sleep(1.8)
        sys.exit(0)
    
    if response not in ['n', 'N']:
        try:
            pprint("Trying to load the game...\n")
            sleep(1.5)
            player = load_game()
            pprint("Game Loaded...")
            sleep(1.5)
            return player
        except Exception as e:
            pprint(e)
            pprint("No game found... Starting New Game...")
            sleep(2.3)
            return None
        
    pprint("Starting New Game...")
    sleep(1.9)
    return None

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
        
def gameloop():
    player = main_menu()
    clearScreen()
    gameOver = False
    
    if player is None:
        pprint("Welcome to the world of pokemon...\n"); sleep(1)
        pprint("Your Goal is to catch all pokemons in the world and \n\t\tbecome the greatest pokemon trainer of all times.\n"); sleep(1.7)
        pprint("But, for that, you need to become the champion of \n\t\tIndigo league which is an annual pokemon duel competition...\n"); sleep(1.7)
        pprint("You need to earn 8 badges by defeating 8 gym leaders\n\t\t to prove that you are worthy of participating in league.\n"); sleep(1.9)
        pprint("Start you journey and \"Catch'em All\""); sleep(5)
        clearScreen()
        
        pprint("What is your name Adventurer?", end=" ")
        name = input()
        player = PokemonTrainer(name)
        
        pprint()
        pprint("We would like you to choose a pokemon before starting your adventure\n"); sleep(1.5)
        pprint("(C)harmander"); sleep(1.5)
        pprint("(S)quirtle"); sleep(1.5)
        pprint("(B)ulbasaur"); sleep(1.5)
        
        pprint()
        pprint("Choose any one. By default, you get a pikachu. Press enter for pikachu : ", end='')
        pokem = input()
        
        if pokem in ['c', 'C']:    firstpoke = 'charmander'
        elif pokem in ['s', 'S']:  firstpoke = 'squirtle'
        elif pokem in ['b', 'B']:  firstpoke = 'bulbasaur'
        else:   firstpoke = 'pikachu'
        
        pokedata = pokemonWorld[firstpoke]
        playerPokemon = Pokemon(firstpoke, pokedata)
        player.pokemonInHand.append(playerPokemon)
        player.currentPokemon = playerPokemon
        
        
        pprint("Let's Start our adventure..."); sleep(1.8)
        
        pprint()
        pprint(f"'Wait {player.name}!! I am Gary.. I think You remember me...'"); sleep(1.3)
        pprint(f"'Let's have a pokemon battle to test our pokemons. Shall We? If you are not chickened out..' - Gary"); sleep(2.8)
        clearScreen()
        
        winner, player = pokemon_duel(player, Gary, battle='duel')
        clearScreen()
        
        if winner != player.name: 
            gameOver = True
            pprint()
            pprint("Unfortunately, you lost your first battle against gary.\n"); sleep(1.4)
            clearScreen()
            pprint("Game Over...\n"); sleep(1.6)
            pprint("But you can start again... Load the game to start from last check point you saved at..."); sleep(1.8)
        else:
            pprint("Saving the Game...")
            save_game(player)
            sleep(1.6)
            
        clearScreen()
    else:
        pprint(f"Welcome Back {player.name}. Let's Continue our adventure..."); sleep(1)
        clearScreen()
    
    while not gameOver:
        break
    
    
    
if __name__ == '__main__':    
    gameloop()