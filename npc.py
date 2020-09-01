from random import choice
from player import PokemonTrainer
from pokeworld import pokemonWorld, small_pokemons, legendary_pokemons
from pokemon import Pokemon


garyPokname = choice(['charmander', 'bulbasaur', 'squirtle'])
garyPok = pokemonWorld[garyPokname]
garyPok = Pokemon(garyPokname, garyPok, level=0)
Gary = PokemonTrainer('Gary', kind='npc', money=400, startingPokemons=[garyPok])
Gary.currentPokemon = Gary.pokemonInHand[0]