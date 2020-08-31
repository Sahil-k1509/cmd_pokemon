from attacklist import *


small_pokemons = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'caterpie', 'weedle', 'pidgey', 'ekans', 
                  'sandshrew', 'nidoran',  'vulpix', 'jigglypuff', 'zubat',  'diglett', 'meowth', 'psyduck',  
                  'growlithe', 'abra', 'geodude', 'shellder', 'gastly', 'onix', 'koffing', 'horsea', 'staryu', 'scyther', 'magmar', 'magikarp', 
                  'eevee']

medium_pokemons = ['raichu', 'charmeleon', 'wartortle', 'ivysaur', 'metapod', 'kakuna', 'pidgeotto', 'arbok', 'sandslash', 
                   'nidorina', 'nidorino', 'nidoqueen', 'nidoking', 'ninetales',  'golbat',  'dugtrio', 
                   'persian', 'golduck',  'arcanine', 'kadabra', 'graveler', 'cloyster', 'haunter', 'weezing', 'seadra', 'starmie', 
                   'gyarados', 'vaporeon', 'jolteon', 'flareon']

large_pokemons = ['charizard', 'blastoise', 'venusaur', 'butterfree', 'beedrill', 'pidgeot',  'alakazam',  'gengar']

legendary_pokemons = ['zapdos', 'moltres', 'articuno', 'selmon jong un']



pokemonWorld = {
    
    'zapdos': {'type': 'electric', 'evolveAt': None, 'evolveTo': None, 'baseDef': 100, 'baseSpeed': 130, 'startAttacks': [thunderbolt, electroball, catastropika, hyperbeam, aeroblast, aerialace, heal, airslash], 'learnableAttacks': [] },           
    'moltres': {'type': 'fire', 'evolveAt': None, 'evolveTo': None, 'baseDef': 150, 'baseSpeed': 120, 'startAttacks': [firespin, flamethrower, sacredfire, fireblast, aeroblast, heal], 'learnableAttacks': [] },           
    'articuno': {'type': 'water', 'evolveAt': None, 'evolveTo': None, 'baseDef': 240, 'baseSpeed': 121, 'startAttacks': [watercannon, hydrovortex, waterspout, iceburn, icebeam, aurorabeam, hyperbeam, aerialace], 'learnableAttacks': [] },           
    'selmon jong un': {'type': 'dark', 'evolveAt': None, 'evolveTo': None, 'baseDef': 600, 'baseSpeed': 320, 'startAttacks': [crunch, hyperbeam, futuresight, shadowpunch, landwrath, catastropika, sacredfire, watercannon, gigadrain, heal], 'learnableAttacks': [] },           
    
    
    
    'pikachu': {'type': 'electric', 'evolveAt': 18, 'evolveTo': 'raichu', 'baseDef': 10, 'baseSpeed': 30, 'startAttacks': [thundershock, tackle, None, None], 'learnableAttacks': [quickattack, thunderbolt, agility, irontail, thunderpunch, discharge, bolttackle, electroball, catastropika][::-1] },           
    'charmander': {'type': 'fire', 'evolveAt': 18, 'evolveTo': 'charmeleon', 'baseDef': 15, 'baseSpeed': 20, 'startAttacks': [scratch, tackle, None, None], 'learnableAttacks': [ember, flamethrower, firepunch, firespin, shelltrap, fireblast, sacredfire][::-1] },           
    'squirtle': {'type': 'water', 'evolveAt': 18, 'evolveTo': 'wartortle', 'baseDef': 24, 'baseSpeed': 21, 'startAttacks': [headbutt, tackle, None, None], 'learnableAttacks': [watergun, bubblebeam, hydropump, watercannon, hydrovortex][::-1] },           
    'bulbasaur': {'type': 'grass', 'evolveAt': 18, 'evolveTo': 'ivysaur', 'baseDef': 15, 'baseSpeed': 20, 'startAttacks': [razorleaf, tackle, None, None], 'learnableAttacks': [vinewhip, stunspore, gigadrain, frenzy, leafblade, solarbeam][::-1] },           
    
    
    'raichu': {'type': 'electric', 'evolveAt': None, 'evolveTo': None},           
    'charmeleon': {'type': 'fire', 'evolveAt': 36, 'evolveTo': 'charizard'},           
    'wartortle': {'type': 'water', 'evolveAt': 38, 'evolveTo': 'blastoise'},           
    'ivysaur': {'type': 'grass', 'evolveAt': 36, 'evolveTo': 'venusaur'},           
    
    
    'charizard': {'type': 'fire', 'evolveAt': None, 'evolveTo': None},           
    'blastoise': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'venusaur': {'type': 'grass', 'evolveAt': None, 'evolveTo': None},           
}
