import pickle

from player import PokemonTrainer
from pokeworld import pokemonWorld
from pokemon import Pokemon


from time import sleep
from random import randint, random
import os
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

def clearScreen():
    if OSname == 'nt': OSsys('cls')
    else: OSsys('clear')


def main_menu():
    
    print("(N)ew Game")
    print("(L)oad Game")
    
    response = input('\nWhat would you like to do? ')
    
    if response not in ['n', 'N']:
        try:
            print("Trying to load the game...\n")
            sleep(1.5)
            player = load_game()
            print("Game Loaded...")
            sleep(0.5)
            return player
        except Exception:
            print("No game found... Starting New Game...")
            sleep(1)
            return None
        
    print("Starting New Game...")
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
        print("Welcome to the world of pokemon..."); sleep(0.6)
        print("Your Goal is to catch all pokemons in the world and become the greatest pokemon trainer of all times."); sleep(1.3)
        print("But, for that, you need to become the champion of Indigo league which is an annual pokemon duel competition..."); sleep(1.3)
        print("You need to earn 8 badges by defeating 8 gym leaders to prove that you are worthy of participating in league."); sleep(1.2)
        print("Start you journey and \"Catch'em All\""); sleep(1)
        clearScreen()
        
        name = input("What is your name Adventurer? ")
    
    while True:
        break
    
    
    
if __name__ == '__main__':    
    gameloop()