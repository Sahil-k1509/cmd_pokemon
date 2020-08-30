from random import random, randint
from time import sleep

class PokemonTrainer(object):
    
    def __init__(self, name, kind='player', startingPokemons=[], pokemonLimit=7, pokeballs=2, money=300, *args, **kwargs):
        self.name = name
        self.kind = kind
        self.pokemonInHand = startingPokemons
        self.pokemonLimit = pokemonLimit
        self.archivePokemons = []
        self.currentPokemon = None
        self.pokeballs = pokeballs
        self.pokemonAwake = len(self.pokemonInHand)
        self.items = []
        self.money = money
        
        
    def switchPokemon(self):
        print("Your Pokemons: ")
        sleep(0.5)
        for index, pokemon in enumerate(self.pokemonInHand):
            print(index+1, end=') ')
            pokemon.printPokemon()
            sleep(0.5)
        
        print(f"\nCurrent Pokemon:\t {self.currentPokemon.printPokemon()}\n")
        sleep(0.5)
        
        chosen = False
        while not chosen:
            newCurrentPoke = int(input("Which pokemon would you like to choose?"))-1
            if 0 <= newCurrentPoke < len(self.pokemonInHand):
                if self.pokemonInHand[newCurrentPoke].health > 0:
                    self.currentPokemon = self.pokemonInHand[newCurrentPoke]
                    print(f"You chose {self.currentPokemon.name}")
                    chosen = True
                else:
                    print(f"{self.pokemonInHand[newCurrentPoke].name}'s health is zero. You can't chose it")
            else:
                print(f"That is not a valid number. Please choose between 1 and {len(self.pokemonInHand)}")
            
            
    def catchPokemon(self, pokemonToCatch):
        if self.pokeballs > 0:
            pokemonHealth = pokemonToCatch.health
            pokemonMaxHealth = pokemonToCatch.maxHealth
            
            probabilityToCatch = 1 - (pokemonHealth/pokemonMaxHealth)
            requiredCut = 0.3 + 0.4*random()
            
            if probabilityToCatch >= requiredCut:
                print(f"{pokemonToCatch.name} was caught!")
                self.pokeballs -= 1
                if len(self.pokemonInHand) < self.pokemonLimit:
                    self.pokemonInHand.append(pokemonToCatch)
                else:
                    self.archivePokemons.append(pokemonToCatch)
            
        else:
            print("You don't have pokeballs !!")            
            