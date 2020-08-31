from attacklist import *


small_pokemons = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'caterpie', 'weedle', 'pidgey', 'ekans', 
                  'sandshrew', 'nidoran',  'vulpix', 'jigglypuff', 'zubat',  'diglett', 'meowth', 'psyduck',  
                  'growlithe', 'abra', 'geodude', 'shellder', 'gastly', 'onix', 'koffing', 'horsea', 'staryu', 'scyther', 'magmar', 'magikarp', 
                  'eevee']

medium_pokemons = ['raichu', 'charmeleon', 'wartortle', 'ivysaur', 'metapod', 'kakuna', 'pidgeotto', 'arbok', 'sandslash', 
                   'nidorina', 'nidorino', 'ninetales',  'golbat',  'dugtrio', 
                   'persian', 'golduck',  'arcanine', 'kadabra', 'graveler', 'cloyster', 'haunter', 'weezing', 'seadra', 'starmie', 
                   'gyarados', 'vaporeon', 'jolteon', 'flareon']

large_pokemons = ['charizard', 'blastoise', 'venusaur', 'butterfree', 'beedrill', 'pidgeot', 'nidoqueen', 'nidoking', 'alakazam',  'gengar']

legendary_pokemons = ['zapdos', 'moltres', 'articuno', 'selmon jong un']



pokemonWorld = {
    
    'zapdos': {'type': 'electric', 'evolveAt': None, 'evolveTo': None, 'baseDef': 100, 'baseSpeed': 130, 'startAttacks': [thunderbolt, electroball, catastropika, hyperbeam, aeroblast, aerialace, heal, airslash], 'learnableAttacks': [] },           
    'moltres': {'type': 'fire', 'evolveAt': None, 'evolveTo': None, 'baseDef': 150, 'baseSpeed': 120, 'startAttacks': [firespin, flamethrower, sacredfire, fireblast, aeroblast, heal], 'learnableAttacks': [] },           
    'articuno': {'type': 'water', 'evolveAt': None, 'evolveTo': None, 'baseDef': 240, 'baseSpeed': 121, 'startAttacks': [watercannon, hydrovortex, waterspout, iceburn, icebeam, blizzard, aurorabeam, hyperbeam, aerialace], 'learnableAttacks': [] },           
    'selmon jong un': {'type': 'dark', 'evolveAt': None, 'evolveTo': None, 'baseDef': 600, 'baseSpeed': 320, 'startAttacks': [crunch, hyperbeam, futuresight, shadowpunch, landwrath, catastropika, sacredfire, watercannon, gigadrain, heal], 'learnableAttacks': [] },           
    
    
    'pikachu': {'type': 'electric', 'evolveAt': 18, 'evolveTo': 'raichu', 'baseDef': 10, 'baseSpeed': 30, 'startAttacks': [thundershock, tackle, None, None], 'learnableAttacks': [quickattack, thunderbolt, agility, irontail, thunderpunch, discharge, bolttackle, electroball, catastropika][::-1] },           
    'charmander': {'type': 'fire', 'evolveAt': 18, 'evolveTo': 'charmeleon', 'baseDef': 15, 'baseSpeed': 20, 'startAttacks': [scratch, tackle, None, None], 'learnableAttacks': [ember, flamethrower, firepunch, firespin, shelltrap, fireblast, sacredfire][::-1] },           
    'squirtle': {'type': 'water', 'evolveAt': 18, 'evolveTo': 'wartortle', 'baseDef': 24, 'baseSpeed': 21, 'startAttacks': [headbutt, tackle, None, None], 'learnableAttacks': [watergun, bubblebeam, headbutt, mudslap, hydropump, watercannon, hydrovortex][::-1] },           
    'bulbasaur': {'type': 'grass', 'evolveAt': 18, 'evolveTo': 'ivysaur', 'baseDef': 15, 'baseSpeed': 20, 'startAttacks': [razorleaf, tackle, None, None], 'learnableAttacks': [vinewhip, quickattack, stunspore, gigadrain, frenzy, leafblade, solarbeam][::-1] },           
    'caterpie': {'type': 'bug', 'evolveAt': 7, 'evolveTo': 'metapod', 'baseDef': 5, 'baseSpeed': 13, 'startAttacks': [stringshot, bugbite, leechlife, None], 'learnableAttacks': [tackle, harden, gust, whirlwind, wingattack][::-1] },           
    'weedle': {'type': 'bug', 'evolveAt': 7, 'evolveTo': 'kakuna', 'baseDef': 5, 'baseSpeed': 13, 'startAttacks': [poisonsting, bugbite, stinger, None], 'learnableAttacks': [tackle, poisonpowder, gust, leechlife, wingattack][::-1] },           
    'pidgey': {'type': 'flying', 'evolveAt': 16, 'evolveTo': 'pidgeotto', 'baseDef': 12, 'baseSpeed': 23, 'startAttacks': [quickattack, gust, None, None], 'learnableAttacks': [whirlwind, agility, sandattack, wingattack, fly, aerialace, airslash, aeroblast][::-1] },           
    'ekans': {'type': 'poison', 'evolveAt': 14, 'evolveTo': 'arbok', 'baseDef': 14, 'baseSpeed': 21, 'startAttacks': [acid, poisonsting, None, None], 'learnableAttacks': [poisonpowder, quickattack, tailwhip, agility, leechlife, poisonfang, gunkshot][::-1] },           
    'sandshrew': {'type': 'ground', 'evolveAt': 18, 'evolveTo': 'sandslash', 'baseDef': 30, 'baseSpeed': 18, 'startAttacks': [sandattack, tackle, None, None], 'learnableAttacks': [dig, quickattack, scratch, mudslap][::-1] },           
    'nidoran': {'type': 'poison', 'evolveAt': 15, 'evolveTo': None, 'baseDef': 13, 'baseSpeed': 15, 'startAttacks': [tackle, poisonsting, None, None], 'learnableAttacks': [sandattack, quickattack, bite, agility, headbutt, megahorn, acid, hyperbeam, icebeam, thunderbolt, earthquake][::-1] },           
    'vulpix': {'type': 'fire', 'evolveAt': 18, 'evolveTo': 'ninetales', 'baseDef': 18, 'baseSpeed': 19, 'startAttacks': [tackle, ember, None, None], 'learnableAttacks': [flamethrower, quickattack, headbutt, firespin, scratch, bite, fireblast][::-1] },           
    'jigglypuff': {'type': 'psychic', 'evolveAt': None, 'evolveTo': None, 'baseDef': 13, 'baseSpeed': 20, 'startAttacks': [pound, sing, None, None], 'learnableAttacks': [tackle, heal, headbutt, cut, curse, ironpunch, hyperbeam][::-1] },           
    'zubat': {'type': 'flying', 'evolveAt': 14, 'evolveTo': 'golbat', 'baseDef': 14, 'baseSpeed': 23, 'startAttacks': [poisonsting, whirlwind, None, None], 'learnableAttacks': [wingattack, airslash, quickattack, poisonfang, stinger][::-1] },           
    'diglett': {'type': 'ground', 'evolveAt': 18, 'evolveTo': 'dugtrio', 'baseDef': 19, 'baseSpeed': 21, 'startAttacks': [sandattack, dig, None, None], 'learnableAttacks': [mudslap, cut, rockthrow, headsmash, stoneedge, earthquake, landwrath][::-1] },           
    'meowth': {'type': 'normal', 'evolveAt': 18, 'evolveTo': 'persian', 'baseDef': 18, 'baseSpeed': 21, 'startAttacks': [scratch, tackle, tailwhip, None], 'learnableAttacks': [agility, quickattack, sandattack, irontail, bite, feintattack, hyperbeam][::-1] },           
    'psyduck': {'type': 'water', 'evolveAt': 18, 'evolveTo': 'golduck', 'baseDef': 17, 'baseSpeed': 11, 'startAttacks': [watergun, tackle, None, None], 'learnableAttacks': [scratch, bubblebeam, agility, psybeam, confusion, heal, psyshock, hyperbeam][::-1] },           
    
    
    'raichu': {'type': 'electric', 'evolveAt': None, 'evolveTo': None},           
    'charmeleon': {'type': 'fire', 'evolveAt': 36, 'evolveTo': 'charizard'},           
    'wartortle': {'type': 'water', 'evolveAt': 38, 'evolveTo': 'blastoise'},           
    'ivysaur': {'type': 'grass', 'evolveAt': 36, 'evolveTo': 'venusaur'},           
    'metapod': {'type': 'bug', 'evolveAt': 10, 'evolveTo': 'butterfree'},           
    'kakuna': {'type': 'bug', 'evolveAt': 10, 'evolveTo': 'beedrill'},           
    'pidgeotto': {'type': 'flying', 'evolveAt': 32, 'evolveTo': 'pidgeot'},           
    'arbok': {'type': 'poison', 'evolveAt': None, 'evolveTo': None},           
    'sandslash': {'type': 'ground', 'evolveAt': None, 'evolveTo': None},           
    'nidorina': {'type': 'poison', 'evolveAt': 30, 'evolveTo': 'nidoqueen'},           
    'nidorino': {'type': 'poison', 'evolveAt': 30, 'evolveTo': 'nidoking'},           
    'ninetales': {'type': 'fire', 'evolveAt': None, 'evolveTo': None},           
    'golbat': {'type': 'flying', 'evolveAt': None, 'evolveTo': None},           
    'dugtrio': {'type': 'ground', 'evolveAt': None, 'evolveTo': None},           
    'persian': {'type': 'normal', 'evolveAt': None, 'evolveTo': None},           
    'golduck': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'arcanine': {'type': 'fire', 'evolveAt': None, 'evolveTo': None},           
    'kadabra': {'type': 'psychic', 'evolveAt': 32, 'evolveTo': 'alakazam'},           
    'graveler': {'type': 'rock', 'evolveAt': None, 'evolveTo': None},           
    'cloyster': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'haunter': {'type': 'ghost', 'evolveAt': 34, 'evolveTo': 'gengar'},           
    'weezing': {'type': 'poison', 'evolveAt': None, 'evolveTo': None},           
    'seadra': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'starmie': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'gyarados': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'vaporeon': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'jolteon': {'type': 'electric', 'evolveAt': None, 'evolveTo': None},           
    'flareon': {'type': 'fire', 'evolveAt': None, 'evolveTo': None},           
    
    
    'charizard': {'type': 'fire', 'evolveAt': None, 'evolveTo': None},           
    'blastoise': {'type': 'water', 'evolveAt': None, 'evolveTo': None},           
    'venusaur': {'type': 'grass', 'evolveAt': None, 'evolveTo': None},           
    'butterfree': {'type': 'bug', 'evolveAt': None, 'evolveTo': None},           
    'beedrill': {'type': 'bug', 'evolveAt': None, 'evolveTo': None},           
    'pidgeot': {'type': 'flying', 'evolveAt': None, 'evolveTo': None},           
    'nidoqueen': {'type': 'poison', 'evolveAt': None, 'evolveTo': None},           
    'nidoking': {'type': 'poison', 'evolveAt': None, 'evolveTo': None},           
    'alakazam': {'type': 'psychic', 'evolveAt': None, 'evolveTo': None},           
    'gengar': {'type': 'ghost', 'evolveAt': None, 'evolveTo': None}           
}
