from random import choice
from player import PokemonTrainer
from pokeworld import pokemonWorld, small_pokemons, legendary_pokemons
from pokemon import Pokemon
from copy import deepcopy

# Legendary Pokemons
zapdosData =  deepcopy(pokemonWorld['zapdos'])
moltresData =  deepcopy(pokemonWorld['moltres'])
articunoData = deepcopy(pokemonWorld['articuno'])
sjuData = deepcopy(pokemonWorld['selmon jong un'])

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
garyPok = deepcopy(pokemonWorld[garyPokname])
garyPok = Pokemon(garyPokname, garyPok, level=0)
Gary = PokemonTrainer('Gary', kind='npc', money=400, startingPokemons=[garyPok])
Gary.currentPokemon = Gary.pokemonInHand[0]


# Code Brock
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=5000, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Misty 
mistyp1 = deepcopy(pokemonWorld['staryu'])
mistyp2 = deepcopy(pokemonWorld['staryu'])

mistyp1 = Pokemon('staryu', mistyp1, level=0)
mistyp2 = Pokemon('staryu', mistyp2, level=0)

mistyp1.npcPokemonReady(maxlevel=12)
mistyp2.npcPokemonReady(maxlevel=19)

Misty = PokemonTrainer('Misty', kind='npc', money=16000, startingPokemons=[mistyp1, mistyp2])
Misty.currentPokemon = Misty.pokemonInHand[0]


# Code Lt. Surge 
surgep1 = deepcopy(pokemonWorld['pikachu'])

surgep1 = Pokemon('pikachu', surgep1, level=0)

surgep1.npcPokemonReady(maxlevel=24)
surgep1.useStone('thunderstone', playertype='npc')

Surge = PokemonTrainer('Surge', kind='npc', money=20000, startingPokemons=[surgep1])
Surge.currentPokemon = Surge.pokemonInHand[0]
#surgep1.displayStats(trainer="player's")


# Code Erika 
erikap1 = deepcopy(pokemonWorld['bulbasaur'])
erikap2 = deepcopy(pokemonWorld['oddish'])

erikap1 = Pokemon('bulbasaur', erikap1, level=0)
erikap2 = Pokemon('oddish', erikap2, level=0)

erikap1.npcPokemonReady(maxlevel=29)
erikap2.npcPokemonReady(maxlevel=30)

Erika = PokemonTrainer('Erika', kind='npc', money=24000, startingPokemons=[erikap1, erikap2])
Erika.currentPokemon = Erika.pokemonInHand[0]


# Code Koga 
kogap1 = deepcopy(pokemonWorld['ekans'])
kogap2 = deepcopy(pokemonWorld['zubat'])

kogap1 = Pokemon('ekans', kogap1, level=0)
kogap2 = Pokemon('zubat', kogap2, level=0)

kogap1.npcPokemonReady(maxlevel=26)
kogap2.npcPokemonReady(maxlevel=32)

Koga = PokemonTrainer('Koga', kind='npc', money=40000, startingPokemons=[kogap1, kogap2])
Koga.currentPokemon = Koga.pokemonInHand[0]


# Code Sabrina 
sabrinap1 = deepcopy(pokemonWorld['abra'])

sabrinap1 = Pokemon('geodude', sabrinap1, level=0)

sabrinap1.npcPokemonReady(maxlevel=40)

Sabrina = PokemonTrainer('Sabrina', kind='npc', money=51000, startingPokemons=[sabrinap1])
Sabrina.currentPokemon = Sabrina.pokemonInHand[0]


# Code Blaine 
blainep1 = deepcopy(pokemonWorld['magmar'])

blainep1 = Pokemon('magmar', blainep1, level=0)

blainep1.npcPokemonReady(maxlevel=52)

Blaine = PokemonTrainer('Blaine', kind='npc', money=69000, startingPokemons=[blainep1])
Blaine.currentPokemon = Blaine.pokemonInHand[0]


# Code Giovanni 
giovannip1 = deepcopy(pokemonWorld['geodude'])
giovannip2 = deepcopy(pokemonWorld['nidoran'])

giovannip1 = Pokemon('geodude', giovannip1, level=0)
giovannip2 = Pokemon('nidoran', giovannip2, level=0)

giovannip1.npcPokemonReady(maxlevel=61)
giovannip2.npcPokemonReady(maxlevel=70)

Giovanni = PokemonTrainer('Giovanni', kind='npc', money=90000, startingPokemons=[giovannip1, giovannip2])
Giovanni.currentPokemon = Giovanni.pokemonInHand[0]


'''
# Code Lorelei 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Bruno 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Agatha 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Lance 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Champion Indigo 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Jessie 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code James 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Josh 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Lee 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Trainer Mojo 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Joe 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Kira 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]


# Code Pokemon master Sting 
brockp1 = deepcopy(pokemonWorld['geodude'])
brockp2 = deepcopy(pokemonWorld['onix'])

brockp1 = Pokemon('geodude', brockp1, level=0)
brockp2 = Pokemon('onix', brockp2, level=0)

brockp1.npcPokemonReady(maxlevel=4)
brockp2.npcPokemonReady(maxlevel=7)

Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
Brock.currentPokemon = Brock.pokemonInHand[0]
'''
