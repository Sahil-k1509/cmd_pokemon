from random import random, randint
from time import sleep

def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)
    

class PokemonTrainer(object):
    
    def __init__(self, name, currentLocation='Pallet Town', kind='player', startingPokemons=[], pokemonLimit=7, pokeballs=2, money=300, *args, **kwargs):
        self.name = name
        self.kind = kind
        self.pokemonInHand = startingPokemons
        self.pokemonLimit = pokemonLimit
        self.archivePokemons = []
        self.currentPokemon = None
        self.pokeballs = pokeballs
        self.currentLocation = currentLocation
        self.items = []
        self.badges = []
        self.money = money
        
        
    def switchPokemon(self):
        if self.kind == 'player':
            pprint("Your Pokemons: ")
            sleep(1.2)
            nonzerohp = 0
            for index, pokemon in enumerate(self.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                if pokemon.health > 0: nonzerohp+=1
                sleep(1.2)
                
            pprint(f"Current Pokemon:"); sleep(1.2)
            self.currentPokemon.printPokemon()
            sleep(2)
            
            if nonzerohp == 0: return False
            
            chosen = False
            while not chosen:
                newCurrentPoke = int(input("\t\tWhich pokemon would you like to choose? "))-1
                if 0 <= newCurrentPoke < len(self.pokemonInHand):
                    if self.pokemonInHand[newCurrentPoke].health > 0:
                        self.currentPokemon = self.pokemonInHand[newCurrentPoke]
                        pprint(f"You chose {self.currentPokemon.name}"); sleep(1.2)
                        chosen = True
                    else:
                        pprint(f"{self.pokemonInHand[newCurrentPoke].name}'s health is zero. You can't chose it"); sleep(1.2)
                else:
                    pprint(f"That is not a valid number. Please choose between 1 and {len(self.pokemonInHand)}"); sleep(1.2)
            
            return True        
        else:
            indexOfCurrent = self.pokemonInHand.index(self.currentPokemon)
            if indexOfCurrent == self.pokemonLimit - 1: return False
            
            self.currentPokemon = self.pokemonInHand[(indexOfCurrent+1)%len(self.pokemonInHand)]
            if self.currentPokemon.health <= 0: return False
        
            pprint(f"{self.name} Chose {self.currentPokemon.name}"); sleep(1.1)
            return True    
                
            
    def catchPokemon(self, pokemonToCatch):
        if self.pokeballs > 0:
            pokemonHealth = pokemonToCatch.health
            pokemonMaxHealth = pokemonToCatch.maxHealth
            
            probabilityToCatch = 1 - (pokemonHealth/pokemonMaxHealth)
            requiredCut = 0.3 + 0.4*random()
            
            if probabilityToCatch >= requiredCut:
                pprint(f"{pokemonToCatch.name} was caught!\n"); sleep(1.3)
                self.pokeballs -= 1
                if len(self.pokemonInHand) < self.pokemonLimit:
                    self.pokemonInHand.append(pokemonToCatch)
                else:
                    self.archivePokemons.append(pokemonToCatch)
                
                return True
            else:
                pprint(f"{pokemonToCatch.name} wasn't caught..."); sleep(1.3)
                self.pokeballs -= 1
                return False
            
        else:
            pprint("You don't have pokeballs !!\n"); sleep(1.3)
            return False
            
    
    def printTrainer(self):
        pprint("+-----------------------------------------------------+")
        pprint(f"Name: {self.name}"); sleep(1.2)
        pprint(f"Current Pokemon: {self.currentPokemon.name}"); sleep(1.2)
        pprint(f"Pokeballs left: {self.pokeballs}"); sleep(1.2)
        pprint(f"Items: {self.items}"); sleep(1.2)
        pprint(f"Gym Badges: {self.badges}"); sleep(1.2)
        pprint(f"Money: {self.money}"); sleep(1.2)
        pprint("+-----------------------------------------------------+")