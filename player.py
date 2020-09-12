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
        self.items = {}
        self.badges = []
        self.money = money
        
    def archiveExchange(self):
        sleep(0.2)
        if len(self.archivePokemons) == 0:
            pprint("You don't have any pokemon in archive..."); sleep(0)
            return
        pprint("Pokemons in archive: ")
        sleep(0.2)
        for index, pokemon in enumerate(self.archivePokemons):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                if pokemon.health > 0: nonzerohp+=1
                sleep(0.3)
        pprint()
        pprint("Pokemon in Hand: ")
        for index, pokemon in enumerate(self.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                sleep(0.3)
                
        pprint()
        pprint("Select index of pokemon from archive: ", end=''); sleep(0.4)
        archiveIndex = int(input())-1
                
        pprint()
        pprint("Select index of pokemon from hand: ", end=''); sleep(0.2)
        handIndex = int(input())-1
        
        if not (0 <= archiveIndex < len(self.archivePokemons)):
            pprint("You don't have pokemon at that index in archive..."); sleep(0.2)
            return 
        
        if not (0 <= handIndex < len(self.pokemonInHand)):
            pprint("You don't have pokemon at that index in hand..."); sleep(0.2)
            return 
        
        pprint("Pokemon Changed Succesfully..."); sleep(0.2)
        self.pokemonInHand[handIndex], self.archivePokemons[archiveIndex] = self.archivePokemons[archiveIndex], self.pokemonInHand[handIndex]
        
        self.switchPokemon()
        
        return        
        
        
    def switchPokemon(self):
        if self.kind == 'player':
            pprint("Your Pokemons: ")
            sleep(0.2)
            nonzerohp = 0
            for index, pokemon in enumerate(self.pokemonInHand):
                pprint(index+1, end=') ')
                pokemon.printPokemon()
                if pokemon.health > 0: nonzerohp+=1
                sleep(0.2)
                
            pprint(f"Current Pokemon:"); sleep(0.2)
            self.currentPokemon.printPokemon()
            sleep(1)
            
            if nonzerohp == 0: return False
            chosen = False
            while not chosen:
                newCurrentPoke = int(input("\t\tWhich pokemon would you like to choose as current Pokemon? "))-1
                if 0 <= newCurrentPoke < len(self.pokemonInHand):
                    if self.pokemonInHand[newCurrentPoke].health > 0:
                        self.currentPokemon = self.pokemonInHand[newCurrentPoke]
                        pprint(f"You chose {self.currentPokemon.name}"); sleep(0.2)
                        chosen = True
                    else:
                        pprint(f"{self.pokemonInHand[newCurrentPoke].name}'s health is zero. You can't chose it"); sleep(0.2)
                else:
                    pprint(f"That is not a valid number. Please choose between 1 and {len(self.pokemonInHand)}"); sleep(0.2)
            
            return True        
        else:
            indexOfCurrent = self.pokemonInHand.index(self.currentPokemon)
            if indexOfCurrent == self.pokemonLimit - 1: return False
            
            self.currentPokemon = self.pokemonInHand[(indexOfCurrent+1)%len(self.pokemonInHand)]
            if self.currentPokemon.health <= 0: return False
        
            pprint(f"{self.name} Chose {self.currentPokemon.name}"); sleep(0.1)
            return True    
                
            
    def catchPokemon(self, pokemonToCatch):
        if self.pokeballs > 0:
            pokemonHealth = pokemonToCatch.health
            pokemonMaxHealth = pokemonToCatch.maxHealth
            
            probabilityToCatch = 1 - (pokemonHealth/pokemonMaxHealth)
            requiredCut = 0.6 + 0.2*random()
            
            if probabilityToCatch >= requiredCut and pokemonHealth <= 40 + pokemonToCatch.level:
                pprint(f"{pokemonToCatch.name} was caught!\n"); sleep(0.3)
                self.pokeballs -= 1
                if len(self.pokemonInHand) < self.pokemonLimit:
                    self.pokemonInHand.append(pokemonToCatch)
                else:
                    self.archivePokemons.append(pokemonToCatch)
                pprint();   pprint("Press Enter to Continue", end=' ');     input()
                return True
            else:
                pprint(f"{pokemonToCatch.name} wasn't caught..."); sleep(0.3)
                self.pokeballs -= 1
                pprint();   pprint("Press Enter to Continue", end=' ');     input()
                return False
            
        else:
            pprint("You don't have pokeballs !!\n"); sleep(0.3)
            pprint();   pprint("Press Enter to Continue", end=' ');     input()
            return False
            
    
    def printTrainer(self, showAllpoke=False):
        if self.kind == 'player':
            pprint("+--------------------------------------------------------------------------+"); sleep(0.2) 
            pprint()
            pprint(f"Name: {self.name}"); sleep(0.2)
            pprint(f"Current Pokemon: {self.currentPokemon.name}"); sleep(0.2)
            pprint(f"Pokeballs left: {self.pokeballs}"); sleep(0.2)
            pprint(f"Items: {self.items}"); sleep(0.2)
            pprint(f"Gym Badges: {self.badges}"); sleep(0.2)
            pprint(f"Money: {self.money}"); sleep(0.2)
            pprint()
            
            if showAllpoke:
                for pokemon in self.pokemonInHand:
                    pokemon.displayStats(detailed=True); sleep(0)
            
            pprint()
            pprint("+--------------------------------------------------------------------------+")
        else:
            pprint("+-----------------------------------------------------+"); sleep(0.2) 
            pprint()
            pprint(f"Name: {self.name}"); sleep(0.2)
            pprint(f"Number of pokemons: {len(self.pokemonInHand)}"); sleep(0.2)
            pprint(f"Money: $ {self.money}"); sleep(0.2)
            pprint()
            pprint("+-----------------------------------------------------+")
            
    def healAllpoke(self):
        sleep(0.2)
        if self.kind == 'player':
            pprint("All your pokemons have been healed..."); sleep(1.2)
        for pokemon in self.pokemonInHand:
            pokemon.visitPokemonCentre()