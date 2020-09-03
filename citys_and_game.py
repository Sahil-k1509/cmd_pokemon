from pokeworld import pokemonWorld, small_pokemons, legendary_pokemons
from pokemon import Pokemon
from npc import Gary, Zapdos, Articuno, Moltres, SelmonJongUn, Brock, Misty, Surge, Erika, Koga, Sabrina, Blaine, Giovanni

import os
import sys
import pickle
from time import sleep
from math import floor
from random import randint, random, choice
from os import system as OSsys, name as OSname

from colorama import init as initializeColor, Fore, Back, Style
from termcolor import colored
from pyfiglet import figlet_format

initializeColor()

routes = {
        'Pallet Town': ['Viridian City'],   
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
        'Cinnabar Island': ['Pallet Town', 'Volcano', 'Seafoam Island'],   
        'Volcano': ['Cinnabar Island'],
        'Indigo Plateau': [] 
}


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
    return player


def showMap(player):
    sleep(1)
    pprint()
    
    print(figlet_format("                M a p ")); sleep(0.7)

    pprint(r"                                                      Volcano      "); sleep(0.2)
    pprint(r"                                                         |         "); sleep(0.2)
    pprint(r"                                                         |         "); sleep(0.2)
    pprint(r"Indigo Plateau     Pallet Town . . . . . . . . .  Cinnabar Island  "); sleep(0.2)
    pprint(r"     |                  |                                .         "); sleep(0.2)
    pprint(r"     |                  |                                .         "); sleep(0.2)
    pprint(r"Victory Road ------ Viridian City                 Seafoam Island   "); sleep(0.2)
    pprint(r"     |                  |                                .         "); sleep(0.2)
    pprint(r"     |                  |                                .         "); sleep(0.2)
    pprint(r" Horizon           Viridian Forest                 Fuschia City    "); sleep(0.2)
    pprint(r"                        |                          /     |         "); sleep(0.2)
    pprint(r"                        |                         /      |         "); sleep(0.2)
    pprint(r"                    Pewter City       Celadon City       |         "); sleep(0.2)
    pprint(r"                        |               |                |         "); sleep(0.2)
    pprint(r"                        |               |                |         "); sleep(0.2)
    pprint(r"        Mt. Top ---  Mt. Moon     Saffron City           |         "); sleep(0.2)
    pprint(r"                        |        /      |     \          |         "); sleep(0.2)
    pprint(r"                        |       /       |      \         |         "); sleep(0.2)
    pprint(r"                   Cerulean City        |        Vermillion City   "); sleep(0.2)
    pprint(r"                                \       |       /                  "); sleep(0.2)
    pprint(r"                                 \      |      /                   "); sleep(0.2)
    pprint(r"                                  Lavender Town                    "); sleep(0.2)
    pprint(r"                                        |                          "); sleep(0.2)
    pprint(r"                                        |                          "); sleep(0.2)
    pprint(r"                                    Outskirts                      "); sleep(0.2)
    
    pprint()
    pprint()
        
    pprint(f"Current Location: {player.currentLocation}"); sleep(1)
    pprint("Go back? (press enter) ", end='')
    input()
    return

def openShop(player):
    shopitems = {1 :['thunderstone', 1000], 2: ['waterstone', 1000], 3: ['firestone', 1200], 4: ['pokeballs', 100]}
    pprint(f"Welcome to the shop {player.name}. What would you like to buy?"); sleep(1.2)
    
    pprint("+--------------------------------------------------+")
    pprint(); sleep(1.2)
    
    for index, item in shopitems.items():
        pprint(f"{index}) {item[0]} : $ {item[1]}"); sleep(0.5)
        
    pprint(); sleep(1.2)
    pprint("+--------------------------------------------------+")
    pprint()
    pprint(f"Money left: $ {player.money}")
    pprint("Enter the index of item you want: ", end='')
    try: 
        itemwantIndex = int(input())
    except Exception:
        return player
    
    sleep(1)
    if shopitems.get(itemwantIndex, -1) ==  -1:
        pprint("Sorry, we don't have that item. Please visit later..."); sleep(1.2)
        return player
    else:
        pprint("How much do you want? ", end='')
        try:
            count = int(input())
        except Exception:
            return player
        sleep(2)
        if shopitems[itemwantIndex][1]*count > player.money:
            pprint("You don't have enough money. Please come back later..."); sleep(1.2)
            return player
         
        pprint(f"You received {count} {shopitems[itemwantIndex][0]} for $ {shopitems[itemwantIndex][1]*count}")
        player.money -= shopitems[itemwantIndex][1]*count
        
        if shopitems[itemwantIndex][0] == 'pokeballs': player.pokeballs += count
        else: player.items[shopitems[itemwantIndex][0]] = player.items.get(shopitems[itemwantIndex][0], 0) + count
        
        return player

def useItem(player): 
    itemsUsableTemp = {}
    if len(player.items) == 0:
        pprint("You don't have any items to use..."); sleep(1)
        return player
    pprint("+----------------------------------------------+"); sleep(1.2); pprint()
    for index, item in enumerate(player.items.items(), 1):
        pprint(f"{index}) {item[0]} : {item[1]} left"); sleep(0.5)
        itemsUsableTemp[index] = item[0]
    sleep(1.2); pprint()
    pprint("+----------------------------------------------+")
    pprint()
    pprint("Choose index of item to use: ", end='')
    itemIndex = int(input())
     
    if itemsUsableTemp.get(itemIndex, -1) == -1:
        pprint("This is not a valid item..."); sleep(1)
        return player
    elif player.items[itemsUsableTemp[itemIndex]] <= 0:
        pprint("You don't have that item left anymore..."); sleep(1)
        return player
    
    if itemsUsableTemp[itemIndex] in ['thunderstone', 'waterstone', 'firestone']:
        
        pprint("Pokemon in Hand: ")
        for index, pokemon in enumerate(player.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                sleep(1)
                
        pprint()
        pprint("Select index of pokemon from hand: ", end=''); sleep(1.2)
        handIndex = int(input())-1
        
        if not (0 <= handIndex < len(player.pokemonInHand)):
            pprint("You don't have pokemon at that index in hand..."); sleep(1.2)
            return player
        
        player.pokemonInHand[handIndex].useStone(stonetype=itemsUsableTemp[itemIndex])
        player.items[itemsUsableTemp[itemIndex]] -= 1
        
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
                    return (None, player)
                else:
                    pprint("couldn't escape..\n\n"); sleep(1.8)
            
            if whatTodo in ['t', 'T']:
                if player.catchPokemon(opponent):
                    battleOver = True
                    clearScreen()
                    return (None, player)
            
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

def navigation_menu(player, hasGym=False, hasWild=False, hasShop=False, hasPokecenter=False):
    clearScreen()
    pprint("+--------------------------------------------------+") 
    sleep(1.2); pprint()
    
    pprint("(N)avigate to other city"); sleep(1.2)
    pprint("(M)ap"); sleep(1.2)
    pprint("(I)nfo of player"); sleep(1.2)
    pprint("(U)se item"); sleep(1.2)
    if hasWild:
        pprint("(W)ild pokemon catching"); sleep(1.2)
    if hasGym:
        pprint("(G)ym battle"); sleep(1.2)
    if hasShop:
        pprint("(B)uy Stuff"); sleep(1.2)
    if hasPokecenter:
        pprint("(P)okemon Centre"); sleep(1.2)
    pprint("(S)ave"); sleep(1.2)
    pprint("(E)xit"); sleep(1.2)
    
    pprint()
    pprint("+--------------------------------------------------+")
    
    pprint()
    sleep(1)
    pprint("What would you like to do? ", end='')
    navigate = input()
    sleep(1)
    
    clearScreen()
    
    if navigate in ['e', 'E']:
        save_game(player)
        sleep(1)
        pprint("Game Saved...."); sleep(1); clearScreen()
        pprint("We hope you would return soon...") 
        sys.exit(0)
    elif navigate in ['s', 'S']:
        save_game(player)
        sleep(1)
        pprint("Game Saved...."); sleep(1); clearScreen()
        return ('S', player)
    elif navigate in ['u', 'U']:
        player = useItem(player)
        return ('U', player)
    elif navigate in ['b', 'B'] and hasShop:    
        player = openShop(player)
        return ('B', player)
    elif navigate in ['p', 'P'] and hasPokecenter: 
        pprint("Welcome to pokemon centre..."); sleep(1.2)   
        player.healAllpoke()
        pprint("Do you want to exchange any pokemons from your current hand to any of your pokemon in archive? (y/n): ", end='')
        d = input()
        if d in ['y', 'Y']: player.archiveExchange()
        return ('P', player)
    elif navigate in ['m', 'M']:
        showMap(player)
        return ('M', player)
    elif navigate in ['i', 'I']:
        player.printTrainer(showAllpoke=True)
        pprint()
        pprint("Go back? (press any key and enter): ", end='')
        input()
        return ('I', player)
    elif navigate in ['w', 'W'] and hasWild:    return ('W', player)
    elif navigate in ['g', 'G'] and hasGym:     return ('G', player)
    else:
        currentCity = player.currentLocation
        if currentCity == 'Indigo Plateau':
            return ('N', player)
        
        pprint("|------------------------------------|")
        for index, neighbour in enumerate(routes[currentCity], 1):
            pprint(f"{index}) {neighbour}"); sleep(1.2)
        pprint("|------------------------------------|")
        pprint()
        sleep(1.2)
        pprint("Where would you like to Go? (Choose no. of city)", end='')
        cityToGo = int(input())-1
        if not (0<=cityToGo<=len(routes[currentCity])):
            pprint(f"Invalid city. You will stay in {currentCity} only..."); sleep(3)
            clearScreen()
            return ('N', player)
        else:
            player.currentLocation = routes[currentCity][cityToGo]
            pprint(f"Alright... Let's go to {player.currentLocation}"); sleep(3)
            clearScreen()
            return ('N', player)

def wildPokemonGenerator(player, listofpokemon, minlevel=0, maxlevel=100):
    clearScreen()
    pprint("Searching for pokemons...", end='')
    sleep(randint(3, 8))
    pprint()
    randpoke = choice(listofpokemon)
    randpokedata = pokemonWorld[randpoke]
    wildpokelvl = randint(minlevel, maxlevel)
    wildpokemon = Pokemon(randpoke, randpokedata, level=0)
    wildpokemon.npcPokemonReady(wildpokelvl)
    pprint(f"A wild {wildpokemon.name} of level {wildpokelvl} appeared..."); sleep(1.2)
    
    winner, player = pokemon_duel(player, wildpokemon)
    
    if winner == None or winner == player.name: return True
    else: return False


def palletTown(player):
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=False, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'E': sys.exit(0)


def viridianCity(player):
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=False, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G':
            if len(player.badges) < 6: 
                pprint(f"The gym is closed. Please Come back later!"); sleep(1)
            else:
                if 'Earth Badge' in player.badges:
                    pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
                else:
                    pprint(f"Welcome to Viridian Gym..."); sleep(1)
                    winner, player = pokemon_duel(player, Giovanni, battle='gym')
                    Giovanni.healAllpoke()
                    if winner == player.name: 
                        player.badges.append('Earth Badge')                    
                        pprint("Congratulations... You won Earth badge..."); sleep(1.2)
                    else:
                        pprint(f"All your pokemons have fainted..."); sleep(1.2)
                        pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                        player.healAllpoke()
                
        elif response == 'E': sys.exit(0)


def viridianForest(player):
    listofpokemons = ['caterpie', 'weedle', 'pidgey', 'eevee', 'oddish']
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=True, hasShop=False, hasPokecenter=False)
        if response == 'N': main_game(player)
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 0, 11)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Viridian City'
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def pewterCity(player):
    listofpokemons = ['meowth', 'pikachu', 'pidgey', 'nidoran']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Boulder Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Pewter Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Brock, battle='gym')
                Brock.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Boulder Badge')                    
                    pprint("Congratulations... You won Boulder badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()
       
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 12, 23)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def mtMoon(player):
    listofpokemons = ['jigglypuff']
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=True, hasShop=False, hasPokecenter=False)
        if response == 'N': main_game(player)
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 15, 30)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Pewter City'
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def mtTop(player):
    listofpokemons = ['diglett', 'sandshrew', 'nidoran', 'ekans', 'zubat']
    total = 0
    while True:
        pprint("What is 1 + 1 = ?", end=' ')
        answer = input()
        if answer == '1': total += 1
        else:
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 17, 50)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Pewter City'
                player.healAllpoke()
                main_game(player)
            else: total += 1
        
        if total >= 3:
            pprint("What is that ?!!!!"); sleep(2)
            pprint("It's a pokemon! But, pokedex doesn't have it in database..."); sleep(2)
            pprint()
            pprint("A Legendary Articuno appeared..."); sleep(2)
            clearScreen()
            didPlayerWin, player = pokemon_duel(player, Articuno, battle='wild')
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Pewter City'
                player.healAllpoke()
                main_game(player)
    

def ceruleanCity(player):
    listofpokemons = ['staryu', 'pidgey']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Cascade Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Cerulean Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Misty, battle='gym')
                Misty.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Cascade Badge')                    
                    pprint("Congratulations... You won Cascade badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()
            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 15, 38)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def vermilionCity(player):
    listofpokemons = ['sandshrew', 'growlithe']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G':
            if 'Thunder Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Vermillion Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Surge, battle='gym')
                Surge.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Thunder Badge')                    
                    pprint("Congratulations... You won Thunder badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()

            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 18, 40)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def fuschiaCity(player):
    listofpokemons = ['weedle', 'nidoran', 'zubat', 'koffing']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Ninja Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Fuschia Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Koga, battle='gym')
                Koga.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Ninja Badge')                    
                    pprint("Congratulations... You won Ninja badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()

            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 16, 35)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def saffronCity(player):
    listofpokemons = ['abra', 'psyduck', 'meowth']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Soul Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Saffron Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Sabrina, battle='gym')
                Sabrina.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Soul Badge')                    
                    pprint("Congratulations... You won Soul badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()
            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 15, 38)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def lavenderTown(player):
    listofpokemons = ['gastly']
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=True, hasShop=False, hasPokecenter=False)
        if response == 'N': main_game(player)
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 10, 45)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Cerulean City'
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def outskirts(player):
    listofpokemons = ['psyduck', 'gastly', 'vulpix', 'geodude', 'onix']
    total = 0
    while True:
        pprint("What is 1 + 1 = ?", end=' ')
        answer = input()
        if answer == '1': total += 1
        else:
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 30, 60)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Cerulean City'
                player.healAllpoke()
                main_game(player)
            else: total += 1
        
        if total >= 3:
            pprint("What is that ?!!!!"); sleep(2)
            pprint("It's a pokemon! But, pokedex doesn't have it in database..."); sleep(2)
            pprint()
            pprint("A Legendary Zapdos appeared..."); sleep(2)
            clearScreen()
            didPlayerWin, player = pokemon_duel(player, Zapdos, battle='wild')
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Cerulean City'
                player.healAllpoke()
                main_game(player)


def celadonCity(player):
    listofpokemons = ['scyther', 'meowth', 'bulbasaur', 'caterpie']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Rainbow Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Celadon Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Erika, battle='gym')
                Erika.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Rainbow Badge')                    
                    pprint("Congratulations... You won Rainbow badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()

            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 10, 20)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def seafoamIsland(player):
    listofpokemons = ['shelldar', 'horsea', 'staryu', 'magikarp']
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=True, hasShop=False, hasPokecenter=False)
        if response == 'N': main_game(player)
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 8, 19)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Fuschia City'
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def cinnabarIsland(player):
    listofpokemons = ['growlithe', 'vulpix']
    while True:
        response, player = navigation_menu(player, hasGym=True, hasWild=True, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'G': 
            if 'Volcano Badge' in player.badges:
                pprint(f"You have already defeated this Gym Leader. You can't duel again..."); sleep(1)
            else:
                pprint(f"Welcome to Cinnabar Gym..."); sleep(1)
                winner, player = pokemon_duel(player, Blaine, battle='gym')
                Blaine.healAllpoke()
                if winner == player.name: 
                    player.badges.append('Volcano Badge')
                    pprint("Congratulations... You won Volcano badge..."); sleep(1.2)
                else:
                    pprint(f"All your pokemons have fainted..."); sleep(1.2)
                    pprint(f"You went to nearest pokecentre..."); sleep(1.2)
                    player.healAllpoke()

            
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 30, 60)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def volcano(player):
    listofpokemons = ['sandshrew', 'vulpix', 'charmander', 'diglett', 'geodude', 'magmar']
    total = 0
    while True:
        pprint("What is 1 + 1 = ?", end=' ')
        answer = input()
        if answer == '1': total += 1
        else:
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 50, 70)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Cinnabar Island'
                player.healAllpoke()
                main_game(player)
            else: total += 1
        
        if total >= 3:
            pprint("What is that ?!!!!"); sleep(2)
            pprint("It's a pokemon! But, pokedex doesn't have it in database..."); sleep(2)
            pprint()
            pprint("A Legendary Moltres appeared..."); sleep(2)
            clearScreen()
            didPlayerWin, player = pokemon_duel(player, Moltres, battle='wild')
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Cinnabar Island'
                player.healAllpoke()
                main_game(player)
    

def indigoPlateau(player):
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=False, hasShop=True, hasPokecenter=True)
        if response == 'N': main_game(player)
        elif response == 'E': sys.exit(0)


def victoryRoad(player):
    listofpokemons = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'onix', 'koffing', 'magikarp', 'shelldar', 'psyduck', 'magmar', 'nidoran', 'pidgey']
    while True:
        response, player = navigation_menu(player, hasGym=False, hasWild=True, hasShop=False, hasPokecenter=False)
        if response == 'N': main_game(player)
        elif response == 'W':   
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 60, 80)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Viridian City'
                player.healAllpoke()
        elif response == 'E': sys.exit(0)


def horizon(player):
    listofpokemons = ['gastly', 'psyduck', 'jigglypuff', 'abra']        
    total = 0
    while True:
        pprint("What is 1 + 1 = ?", end=' ')
        answer = input()
        if answer == '1': total += 1
        else:
            didPlayerWin = wildPokemonGenerator(player, listofpokemons, 70, 90)
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Viridian Island'
                player.healAllpoke()
                main_game(player)
            else: total += 1
        
        if total >= 3:
            pprint("What is that ?!!!!"); sleep(2)
            pprint("It's a pokemon! But, pokedex doesn't have it in database..."); sleep(2)
            pprint()
            pprint("A Mythical 'Selmon Jong Un' appeared..."); sleep(2)
            clearScreen()
            didPlayerWin, player = pokemon_duel(player, SelmonJongUn, battle='wild')
            if not didPlayerWin:
                pprint()
                pprint("All your pokemons have fainted..."); sleep(1.2)
                pprint("You went to nearest pokecentre..."); sleep(1.2)
                player.currentLocation = 'Viridian Island'
                player.healAllpoke()
                main_game(player)



def main_game(player):
    # pprint(player)
    # pprint(player.currentLocation)
    clearScreen()
    
    if player.currentLocation == 'Pallet Town': palletTown(player)
    elif player.currentLocation == 'Viridian City': viridianCity(player)
    elif player.currentLocation == 'Victory Road': victoryRoad(player)
    elif player.currentLocation == 'Horizon': horizon(player)
    elif player.currentLocation == 'Viridian Forest': viridianForest(player)
    elif player.currentLocation == 'Pewter City': pewterCity(player)
    elif player.currentLocation == 'Mt. Moon': mtMoon(player)
    elif player.currentLocation == 'Mt. Top': mtTop(player)
    elif player.currentLocation == 'Cerulean City': ceruleanCity(player)
    elif player.currentLocation == 'Lavender Town': lavenderTown(player)
    elif player.currentLocation == 'Outskirts': outskirts(player)
    elif player.currentLocation == 'Saffron City': saffronCity(player)
    elif player.currentLocation == 'Vermillion City': vermilionCity(player)
    elif player.currentLocation == 'Celadon City': celadonCity(player)
    elif player.currentLocation == 'Fuschia City': fuschiaCity(player)
    elif player.currentLocation == 'Seafoam Island': seafoamIsland(player)
    elif player.currentLocation == 'Cinnabar Island': cinnabarIsland(player)
    elif player.currentLocation == 'Volcano': volcano(player)
    elif player.currentLocation == 'Indigo Plateau': indigoPlateau(player)
    else: sys.exit(0)


