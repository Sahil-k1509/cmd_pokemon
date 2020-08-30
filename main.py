import pickle

from player import PokemonTrainer
from pokeworld import pokemonWorld

all_small_poke = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']

def save_game(player):
    with open('pokemon_progess.pkl', 'wb') as output:
        pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
        
def load_game():
    with open('pokemon_progress.pkl', 'rb') as inputf:
        player = pickle.load(inputf)
    return player
    

def gameloop():
    while True:
        break
    
    
    
if __name__ == '__main__':    
    gameloop()