from random import random, randint
from time import sleep

def pprint(*args, **kwargs):
    print('\t', *args, **kwargs)
    

class PokemonTrainer(object):
    
    def __init__(self, name, currentCity='Veridian', kind='player', startingPokemons=[], pokemonLimit=7, pokeballs=2, money=300, *args, **kwargs):
        self.name = name
        self.kind = kind
        self.pokemonInHand = startingPokemons
        self.pokemonLimit = pokemonLimit
        self.archivePokemons = []
        self.currentPokemon = None
        self.pokeballs = pokeballs
        self.currentCity = currentCity
        self.pokemonAwake = len(self.pokemonInHand)
        self.items = []
        self.badges = []
        self.money = money
        
        
    def switchPokemon(self, trainer='player'):
        if trainer == 'player':
            pprint("Your Pokemons: ")
            sleep(0.5)
            for index, pokemon in enumerate(self.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                sleep(0.5)
            
            pprint(f"\nCurrent Pokemon:\t {self.currentPokemon.printPokemon()}\n")
            sleep(0.5)
            
            chosen = False
            while not chosen:
                newCurrentPoke = int(input("\tWhich pokemon would you like to choose? "))-1
                if 0 <= newCurrentPoke < len(self.pokemonInHand):
                    if self.pokemonInHand[newCurrentPoke].health > 0:
                        self.currentPokemon = self.pokemonInHand[newCurrentPoke]
                        pprint(f"You chose {self.currentPokemon.name}")
                        chosen = True
                    else:
                        pprint(f"{self.pokemonInHand[newCurrentPoke].name}'s health is zero. You can't chose it")
                else:
                    pprint(f"That is not a valid number. Please choose between 1 and {len(self.pokemonInHand)}")
            
            return True        
        else:
            indexOfCurrent = self.pokemonInHand.index(self.currentPokemon)
            if indexOfCurrent == self.pokemonLimit - 1: return None
            
            self.currentPokemon = self.pokemonInHand[(indexOfCurrent+1)%len(self.pokemonLimit)]
            if self.currentPokemon.health <= 0: return None
        
            return True    
                
            
    def catchPokemon(self, pokemonToCatch):
        if self.pokeballs > 0:
            pokemonHealth = pokemonToCatch.health
            pokemonMaxHealth = pokemonToCatch.maxHealth
            
            probabilityToCatch = 1 - (pokemonHealth/pokemonMaxHealth)
            requiredCut = 0.3 + 0.4*random()
            
            if probabilityToCatch >= requiredCut:
                pprint(f"{pokemonToCatch.name} was caught!\n")
                self.pokeballs -= 1
                if len(self.pokemonInHand) < self.pokemonLimit:
                    self.pokemonInHand.append(pokemonToCatch)
                else:
                    self.archivePokemons.append(pokemonToCatch)
            
            else:
                pprint(f"{pokemonToCatch.name} wasn't caught...")
                self.pokeballs -= 1
            
        else:
            pprint("You don't have pokeballs !!\n")
            
    
    def printTrainer(self):
        pprint("+-----------------------------------------------------+")
        pprint(f"Name: {self.name}")
        pprint(f"Current Pokemon: {self.currentPokemon.name}")
        pprint(f"Pokeballs left: {self.pokeballs}")
        pprint(f"Items: {self.items}")
        pprint(f"Gym Badges: {self.badges}")
        pprint(f"Money: {self.money}")
        pprint("+-----------------------------------------------------+")