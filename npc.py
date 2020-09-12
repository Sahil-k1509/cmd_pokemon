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

sabrinap1 = Pokemon('abra', sabrinap1, level=0)

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

giovannip1.npcPokemonReady(maxlevel=51)
giovannip2.npcPokemonReady(maxlevel=60)

Giovanni = PokemonTrainer('Giovanni', kind='npc', money=90000, startingPokemons=[giovannip1, giovannip2])
Giovanni.currentPokemon = Giovanni.pokemonInHand[0]



# Code Lorelei 
loreleip1 = deepcopy(pokemonWorld['squirtle'])
loreleip2 = deepcopy(pokemonWorld['shelldar'])
loreleip3 = deepcopy(pokemonWorld['horsea'])
loreleip4 = deepcopy(pokemonWorld['staryu'])
loreleip5 = deepcopy(pokemonWorld['magikarp'])

loreleip1 = Pokemon('squirtle', loreleip1, level=0)
loreleip2 = Pokemon('shelldar', loreleip2, level=0)
loreleip3 = Pokemon('horsea', loreleip3, level=0)
loreleip4 = Pokemon('staryu', loreleip4, level=0)
loreleip5 = Pokemon('magikarp', loreleip5, level=0)

loreleip1.npcPokemonReady(maxlevel=54)
loreleip2.npcPokemonReady(maxlevel=57)
loreleip3.npcPokemonReady(maxlevel=53)
loreleip4.npcPokemonReady(maxlevel=57)
loreleip5.npcPokemonReady(maxlevel=58)

Lorelei = PokemonTrainer('Lorelei', kind='npc', money=40000, startingPokemons=[loreleip1, loreleip2, loreleip3, loreleip4, loreleip5])
Lorelei.currentPokemon = Lorelei.pokemonInHand[0]


# Code Bruno 
brunop1 = deepcopy(pokemonWorld['ekans'])
brunop2 = deepcopy(pokemonWorld['zubat'])
brunop3 = deepcopy(pokemonWorld['koffing'])
brunop4 = deepcopy(pokemonWorld['nidoran'])

brunop1 = Pokemon('ekans', brunop1, level=0)
brunop2 = Pokemon('zubat', brunop2, level=0)
brunop3 = Pokemon('koffing', brunop3, level=0)
brunop4 = Pokemon('nidoran', brunop4, level=0)

brunop1.npcPokemonReady(maxlevel=58)
brunop2.npcPokemonReady(maxlevel=60)
brunop3.npcPokemonReady(maxlevel=61)
brunop4.npcPokemonReady(maxlevel=63)

Bruno = PokemonTrainer('Bruno', kind='npc', money=100000, startingPokemons=[brunop1, brunop2, brunop3, brunop4])
Bruno.currentPokemon = Bruno.pokemonInHand[0]


# Code Agatha 
agathap1 = deepcopy(pokemonWorld['sandshrew'])
agathap2 = deepcopy(pokemonWorld['diglett'])
agathap3 = deepcopy(pokemonWorld['geodude'])
agathap4 = deepcopy(pokemonWorld['onix'])
agathap5 = deepcopy(pokemonWorld['scyther'])

agathap1 = Pokemon('sandshrew', agathap1, level=0)
agathap2 = Pokemon('diglett', agathap2, level=0)
agathap3 = Pokemon('geodude', agathap3, level=0)
agathap4 = Pokemon('onix', agathap4, level=0)
agathap5 = Pokemon('scyther', agathap5, level=0)

agathap1.npcPokemonReady(maxlevel=64)
agathap2.npcPokemonReady(maxlevel=65)
agathap3.npcPokemonReady(maxlevel=65)
agathap4.npcPokemonReady(maxlevel=67)
agathap5.npcPokemonReady(maxlevel=68)

Agatha = PokemonTrainer('Agatha', kind='npc', money=400000, startingPokemons=[agathap1, agathap2, agathap3, agathap4, agathap5])
Agatha.currentPokemon = Agatha.pokemonInHand[0]


# Code Lance 
lancep1 = deepcopy(pokemonWorld['meowth'])
lancep2 = deepcopy(pokemonWorld['psyduck'])
lancep3 = deepcopy(pokemonWorld['jigglypuff'])
lancep4 = deepcopy(pokemonWorld['abra'])
lancep5 = deepcopy(pokemonWorld['gastly'])

lancep1 = Pokemon('meowth', lancep1, level=0)
lancep2 = Pokemon('psyduck', lancep2, level=0)
lancep3 = Pokemon('jigglypuff', lancep3, level=0)
lancep4 = Pokemon('abra', lancep4, level=0)
lancep5 = Pokemon('gastly', lancep5, level=0)

lancep1.npcPokemonReady(maxlevel=71)
lancep2.npcPokemonReady(maxlevel=72)
lancep3.npcPokemonReady(maxlevel=75)
lancep4.npcPokemonReady(maxlevel=77)
lancep5.npcPokemonReady(maxlevel=78)

Lance = PokemonTrainer('Lance', kind='npc', money=40000, startingPokemons=[lancep1, lancep2, lancep3, lancep4, lancep5])
Lance.currentPokemon = Lance.pokemonInHand[0]


# Code Champion Indigo 
chindigop1 = deepcopy(pokemonWorld['charmander'])
chindigop2 = deepcopy(pokemonWorld['bulbasaur'])
chindigop3 = deepcopy(pokemonWorld['pidgey'])
chindigop4 = deepcopy(pokemonWorld['nidoran'])
chindigop5 = deepcopy(pokemonWorld['onix'])
chindigop6 = deepcopy(pokemonWorld['magikarp'])

chindigop1 = Pokemon('charmander', chindigop1, level=0)
chindigop2 = Pokemon('bulbasaur', chindigop2, level=0)
chindigop3 = Pokemon('pidgey', chindigop3, level=0)
chindigop4 = Pokemon('nidoran', chindigop4, level=0)
chindigop5 = Pokemon('onix', chindigop5, level=0)
chindigop6 = Pokemon('magikarp', chindigop5, level=0)

chindigop1.npcPokemonReady(maxlevel=84)
chindigop2.npcPokemonReady(maxlevel=87)
chindigop3.npcPokemonReady(maxlevel=83)
chindigop4.npcPokemonReady(maxlevel=87)
chindigop5.npcPokemonReady(maxlevel=88)
chindigop6.npcPokemonReady(maxlevel=93)

Chindigo = PokemonTrainer('Champion Indigo League', kind='npc', money=40000, startingPokemons=[chindigop1, chindigop2, chindigop3, chindigop4, chindigop5, chindigop6])
Chindigo.currentPokemon = Chindigo.pokemonInHand[0]


# Code Jessie 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code James 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Trainer Josh 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Trainer Lee 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Trainer Mojo 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Pokemon master Joe 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Pokemon master Kira 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]


# # Code Pokemon master Sting 
# brockp1 = deepcopy(pokemonWorld['geodude'])
# brockp2 = deepcopy(pokemonWorld['onix'])

# brockp1 = Pokemon('geodude', brockp1, level=0)
# brockp2 = Pokemon('onix', brockp2, level=0)

# brockp1.npcPokemonReady(maxlevel=4)
# brockp2.npcPokemonReady(maxlevel=7)

# Brock = PokemonTrainer('Brock', kind='npc', money=400, startingPokemons=[brockp1, brockp2])
# Brock.currentPokemon = Brock.pokemonInHand[0]

