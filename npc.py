from random import choice
from player import PokemonTrainer
from pokeworld import pokemonWorld, small_pokemons, legendary_pokemons
from pokemon import Pokemon


# Legendary Pokemons
zapdosData = pokemonWorld['zapdos']
moltresData = pokemonWorld['moltres']
articunoData = pokemonWorld['articuno']
sjuData = pokemonWorld['selmon jong un']

Zapdos = Pokemon('zapdos', zapdosData, 0)
Moltres = Pokemon('moltres', moltresData, 0)
Articuno = Pokemon('articuno', articunoData, 0)
SelmonJongUn = Pokemon('selmon jong un', sjuData, 0)

Zapdos.npcPokemonReady(100)
Articuno.npcPokemonReady(100)
Moltres.npcPokemonReady(100)
SelmonJongUn.npcPokemonReady(100)


# Code Garry 
garyPokname = choice(['charmander', 'bulbasaur', 'squirtle'])
garyPok = pokemonWorld[garyPokname]
garyPok = Pokemon(garyPokname, garyPok, level=0)
Gary = PokemonTrainer('Gary', kind='npc', money=400, startingPokemons=[garyPok])
Gary.currentPokemon = Gary.pokemonInHand[0]


# Code Brock
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=5000, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Misty 
mistyp1 = pokemonWorld['staryu']
mistyp2 = pokemonWorld['staryu']

mistyp1 = Pokemon('staryu', mistyp1, level=0)
mistyp2 = Pokemon('staryu', mistyp2, level=0)

mistyp1.npcPokemonReady(maxlevel=12)
mistyp2.npcPokemonReady(maxlevel=19)

Misty = PokemonTrainer('Misty', kind='npc', money=16000, startingPokemons=[mistyp1, mistyp2])
Misty.currentPokemon = Misty.pokemonInHand[0]


# Code Lt. Surge 
surgep1 = pokemonWorld['pikachu']

surgep1 = Pokemon('pikachu', surgep1, level=0)

surgep1.npcPokemonReady(maxlevel=21)
surgep1.useStone('thunderstone', playertype='npc')

Surge = PokemonTrainer('Surge', kind='npc', money=20000, startingPokemons=[surgep1])
Surge.currentPokemon = Surge.pokemonInHand[0]


# Code Erika 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Koga 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Sabrina 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Blaine 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Giovanni 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Lorelei 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Bruno 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Agatha 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Lance 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Champion Indigo 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Jessie 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code James 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Josh 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Lee 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Mojo 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Joe 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Kira 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Sting 
brockp1 = pokemonWorld['geodude']
brockp2 = pokemonWorld['onix']

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]

