import pickle

from player import PokemonTrainer
from pokeworld import pokemonWorld
from pokemon import Pokemon


from time import sleep
from random import randint, random
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




all_small_poke = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']


def pprint(*args, **kwargs):
    print('\t', *args, **kwargs)



def clearScreen():
    if OSname == 'nt': OSsys('cls')
    else: OSsys('clear')
    pprint()
    pprint()


def main_menu():
    pprint(); sleep(0.5)
    pprint("(N)ew Game"); sleep(0.5)
    pprint("(L)oad Game"); sleep(0.5)
    pprint("(E)xit"); sleep(0.5)
    
    pprint("New Game will overwrite any previously loaded game...")
    pprint('What would you like to do?', end=' ')
    response = input()
    
    if response in ['e', 'E']:
        sys.exit(0)
    
    if response not in ['n', 'N']:
        try:
            pprint("Trying to load the game...\n")
            sleep(1.5)
            player = load_game()
            pprint("Game Loaded...")
            sleep(0.5)
            return player
        except Exception:
            pprint("No game found... Starting New Game...")
            sleep(1)
            return None
        
    pprint("Starting New Game...")
    sleep(1)
    return None


def save_game(player):
    with open('pokemon_progess.pkl', 'wb') as output:
        pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
        
        
def load_game():
    with open('pokemon_progress.pkl', 'rb') as inputf:
        player = pickle.load(inputf)
    return player


def gameloop():
    player = main_menu()
    clearScreen()
    
    if player is None:
        pprint("Welcome to the world of pokemon...\n"); sleep(0.6)
        pprint("Your Goal is to catch all pokemons in the world and \n\tbecome the greatest pokemon trainer of all times.\n"); sleep(1.3)
        pprint("But, for that, you need to become the champion of \n\tIndigo league which is an annual pokemon duel competition...\n"); sleep(1.3)
        pprint("You need to earn 8 badges by defeating 8 gym leaders\n\t to prove that you are worthy of participating in league.\n"); sleep(1.2)
        pprint("Start you journey and \"Catch'em All\""); sleep(1.5)
        clearScreen()
        
        pprint("What is your name Adventurer?", end=" ")
        name = input()
        player = PokemonTrainer(name)
        
        pprint()
        pprint("We would like you to choose a pokemon before starting your adventure\n"); sleep(0.5)
        pprint("(C)harmander"); sleep(0.5)
        pprint("(S)quirtle"); sleep(0.5)
        pprint("(B)ulbasaur"); sleep(0.5)
        
        pprint()
        pprint("Choose any one. By default, you get a pikachu. Press enter for pikachu : ", end='')
        choice = input()
        
        if choice in ['c', 'C']:    firstpoke = 'charmander'
        elif choice in ['s', 'S']:  firstpoke = 'squirtle'
        elif choice in ['b', 'B']:  firstpoke = 'bulbasaur'
        else:   firstpoke = 'pikachu'
        
        pokedata = pokemonWorld[firstpoke]
        playerPokemon = Pokemon(firstpoke, pokedata)
        player.pokemonInHand.append(playerPokemon)
        player.currentPokemon = playerPokemon
        
        pprint("Saving the Game...")
        save_game(player)
        sleep(0.6)
        clearScreen()
        pprint("Let's Start our adventure..."); sleep(0.8)
        clearScreen()
    else:
        pprint(f"Welcome Back {player.name}. Let's Continue our adventure..."); sleep(0.8)
        clearScreen()
    
    while True:
        break
    
    
    
if __name__ == '__main__':    
    gameloop()