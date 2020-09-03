from player import PokemonTrainer
from pokeworld import pokemonWorld
from pokemon import Pokemon
from npc import Gary
from citys_and_game import pokemon_duel, main_game, pprint, save_game, load_game, clearScreen


from time import sleep
import sys

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

        
def gameloop():
    player = main_menu()
    clearScreen()
    gameOver = False
    
    if player is None:
        pprint("Welcome to the world of pokemon...\n"); sleep(1)
        pprint("Your Goal is to catch all pokemons in the world and\n\t\t become the greatest pokemon trainer of all times.\n"); sleep(1.2)
        pprint("But, for that, you need to become the champion of\n\t\t Indigo league which is an annual pokemon duel competition...\n"); sleep(1.2)
        pprint("You need to earn 8 badges by defeating 8 gym leaders\n\t\t to prove that you are worthy of participating in league.\n"); sleep(1.2)
        pprint("Start you journey and \"Catch'em All\""); sleep(1)
        
        pprint()
        pprint("Press Enter to continue"); input()
        clearScreen()
        
        pprint("What is your name Adventurer?", end=" ")
        name = input()
        player = PokemonTrainer(name)
        sleep(1.2)
        pprint()
        pprint("We would like you to choose a pokemon before starting your Journey\n"); sleep(1.5)
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
        playerPokemon = Pokemon(firstpoke, pokedata, 0)
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
            
        pprint()
        pprint("Press Enter to continue"); input()
        clearScreen()
    else:
        pprint(f"Welcome Back {player.name}. Let's Continue our adventure..."); sleep(1)
        clearScreen()
    
    while not gameOver:
        main_game(player)
    
    
if __name__ == '__main__':    
    gameloop()