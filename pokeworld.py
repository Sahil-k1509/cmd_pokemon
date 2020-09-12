from attacklist import *
# from copy import deepcopy

def deepcopy(actualAttack):
    newattack = Attack(actualAttack.name, actualAttack.attCategory, actualAttack.baseDamage, actualAttack.pLevel, actualAttack.maxcount, heal=actualAttack.heal, accuracy=actualAttack.accuracy, recoil=actualAttack.recoil)
    return newattack

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
    
    'zapdos':          {'type': 'electric', 'evolveAt': None,   'evolveTo': None,          'baseDef': 100, 'baseSpeed': 130, 'startAttacks': [deepcopy(thunderbolt), deepcopy(electroball), deepcopy(catastropika), deepcopy(hyperbeam), deepcopy(aeroblast), deepcopy(aerialace), deepcopy(heal), deepcopy(airslash)], 'learnableAttacks': []         },           
    'moltres':         {'type': 'fire',     'evolveAt': None,   'evolveTo': None,          'baseDef': 150, 'baseSpeed': 120, 'startAttacks': [deepcopy(firespin), deepcopy(flamethrower), deepcopy(sacredfire), deepcopy(fireblast), deepcopy(aeroblast), deepcopy(heal)], 'learnableAttacks': []      },           
    'articuno':        {'type': 'water',    'evolveAt': None,   'evolveTo': None,          'baseDef': 240, 'baseSpeed': 121, 'startAttacks': [deepcopy(watercannon), deepcopy(hydrovortex), deepcopy(waterspout), deepcopy(iceburn), deepcopy(icebeam), deepcopy(blizzard), deepcopy(aurorabeam), deepcopy(hyperbeam), deepcopy(aerialace)], 'learnableAttacks': []        },           
    'selmon jong un':  {'type': 'dark',     'evolveAt': None,   'evolveTo': None,          'baseDef': 600, 'baseSpeed': 320, 'startAttacks': [deepcopy(crunch), deepcopy(hyperbeam), deepcopy(futuresight), deepcopy(shadowpunch), deepcopy(landwrath), deepcopy(catastropika), deepcopy(sacredfire), deepcopy(watercannon), deepcopy(gigadrain), deepcopy(heal)], 'learnableAttacks': []      },           
    

    'pikachu':      {'type': 'electric',    'evolveAt': None,   'evolveTo': 'raichu',       'baseDef': 10,  'baseSpeed': 30, 'startAttacks': [deepcopy(thundershock), deepcopy(tackle), None, None],                'learnableAttacks': [deepcopy(quickattack), deepcopy(thunderbolt), deepcopy(agility), deepcopy(irontail), deepcopy(thunderpunch), deepcopy(discharge), deepcopy(bolttackle), deepcopy(electroball), deepcopy(catastropika)][::-1]       },           
    'charmander':   {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'charmeleon',   'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [deepcopy(scratch), deepcopy(tackle), None, None],                     'learnableAttacks': [deepcopy(ember), deepcopy(flamethrower), deepcopy(firepunch), deepcopy(firespin), deepcopy(shelltrap), deepcopy(fireblast), deepcopy(sacredfire)][::-1]       },           
    'squirtle':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'wartortle',    'baseDef': 24,  'baseSpeed': 21, 'startAttacks': [deepcopy(headbutt), deepcopy(tackle), None, None],                    'learnableAttacks': [deepcopy(watergun), deepcopy(bubblebeam), deepcopy(mudslap), deepcopy(hydropump), deepcopy(watercannon), deepcopy(hydrovortex)][::-1]         },           
    'bulbasaur':    {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'ivysaur',      'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [deepcopy(razorleaf), deepcopy(tackle), None, None],                   'learnableAttacks': [deepcopy(vinewhip), deepcopy(quickattack), deepcopy(stunspore), deepcopy(gigadrain), deepcopy(frenzy), deepcopy(leafblade), deepcopy(solarbeam)][::-1]         },           
    'oddish':       {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'gloom',        'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [deepcopy(razorleaf), deepcopy(tackle), None, None],                   'learnableAttacks': [deepcopy(vinewhip), deepcopy(quickattack), deepcopy(stunspore), deepcopy(leafblade), deepcopy(solarbeam)][::-1]         },           
    'caterpie':     {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'metapod',      'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [deepcopy(stringshot), deepcopy(bugbite), deepcopy(leechlife), None],  'learnableAttacks': [deepcopy(tackle), deepcopy(harden), deepcopy(gust), deepcopy(whirlwind), deepcopy(wingattack)][::-1]        },           
    'weedle':       {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'kakuna',       'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [deepcopy(poisonsting), deepcopy(bugbite), deepcopy(stinger), None],   'learnableAttacks': [deepcopy(tackle), deepcopy(poisonpowder), deepcopy(gust), deepcopy(leechlife), deepcopy(wingattack)][::-1]        },           
    'pidgey':       {'type': 'flying',      'evolveAt': 16,     'evolveTo': 'pidgeotto',    'baseDef': 12,  'baseSpeed': 23, 'startAttacks': [deepcopy(quickattack), deepcopy(gust), None, None],                   'learnableAttacks': [deepcopy(whirlwind), deepcopy(agility), deepcopy(sandattack), deepcopy(wingattack), deepcopy(fly), deepcopy(aerialace), deepcopy(airslash), deepcopy(aeroblast)][::-1]       },           
    'ekans':        {'type': 'poison',      'evolveAt': 14,     'evolveTo': 'arbok',        'baseDef': 14,  'baseSpeed': 21, 'startAttacks': [deepcopy(acid), deepcopy(poisonsting), None, None],                   'learnableAttacks': [deepcopy(poisonpowder), deepcopy(quickattack), deepcopy(tailwhip), deepcopy(agility), deepcopy(leechlife), deepcopy(poisonfang), deepcopy(gunkshot)][::-1]       },           
    'sandshrew':    {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'sandslash',    'baseDef': 30,  'baseSpeed': 18, 'startAttacks': [deepcopy(sandattack), deepcopy(tackle), None, None],                  'learnableAttacks': [deepcopy(dig), deepcopy(quickattack), deepcopy(scratch), deepcopy(mudslap)][::-1]       },           
    'nidoran':      {'type': 'poison',      'evolveAt': 15,     'evolveTo': None,           'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [deepcopy(tackle), deepcopy(poisonsting), None, None],                 'learnableAttacks': [deepcopy(sandattack), deepcopy(quickattack), deepcopy(bite), deepcopy(agility), deepcopy(headbutt), deepcopy(megahorn), deepcopy(acid), deepcopy(hyperbeam), deepcopy(icebeam), deepcopy(icepunch), deepcopy(thunderbolt), deepcopy(earthquake)][::-1]        },           
    'vulpix':       {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'ninetales',    'baseDef': 18,  'baseSpeed': 19, 'startAttacks': [deepcopy(tackle), deepcopy(ember), None, None],                       'learnableAttacks': [deepcopy(flamethrower), deepcopy(quickattack), deepcopy(headbutt), deepcopy(firespin), deepcopy(scratch), deepcopy(bite), deepcopy(fireblast)][::-1]         },           
    'jigglypuff':   {'type': 'psychic',     'evolveAt': None,   'evolveTo': None,           'baseDef': 13,  'baseSpeed': 20, 'startAttacks': [deepcopy(pound), deepcopy(sing), None, None],                         'learnableAttacks': [deepcopy(tackle), deepcopy(heal), deepcopy(headbutt), deepcopy(infactuate), deepcopy(cut), deepcopy(curse), deepcopy(ironpunch), deepcopy(hyperbeam)][::-1]         },           
    'zubat':        {'type': 'flying',      'evolveAt': 14,     'evolveTo': 'golbat',       'baseDef': 14,  'baseSpeed': 23, 'startAttacks': [deepcopy(poisonsting), deepcopy(whirlwind), None, None],              'learnableAttacks': [deepcopy(wingattack), deepcopy(airslash), deepcopy(quickattack), deepcopy(poisonfang), deepcopy(stinger)][::-1]        },           
    'diglett':      {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'dugtrio',      'baseDef': 19,  'baseSpeed': 21, 'startAttacks': [deepcopy(sandattack), deepcopy(dig), None, None],                     'learnableAttacks': [deepcopy(mudslap), deepcopy(cut), deepcopy(rockthrow), deepcopy(headsmash), deepcopy(stoneedge), deepcopy(earthquake), deepcopy(landwrath)][::-1]        },           
    'meowth':       {'type': 'normal',      'evolveAt': 18,     'evolveTo': 'persian',      'baseDef': 18,  'baseSpeed': 21, 'startAttacks': [deepcopy(scratch), deepcopy(tackle), deepcopy(tailwhip), None],       'learnableAttacks': [deepcopy(agility), deepcopy(quickattack), deepcopy(sandattack), deepcopy(irontail), deepcopy(bite), deepcopy(feintattack), deepcopy(hyperbeam)][::-1]      },           
    'psyduck':      {'type': 'water',       'evolveAt': 18,     'evolveTo': 'golduck',      'baseDef': 17,  'baseSpeed': 11, 'startAttacks': [deepcopy(watergun), deepcopy(tackle), None, None],                    'learnableAttacks': [deepcopy(scratch), deepcopy(bubblebeam), deepcopy(agility), deepcopy(psybeam), deepcopy(confusion), deepcopy(heal), deepcopy(psyshock), deepcopy(hyperbeam)][::-1]      },           
    'growlithe':    {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'arcanine',     'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [deepcopy(tackle), deepcopy(bite), None, None],                        'learnableAttacks': [deepcopy(firespin), deepcopy(scratch), deepcopy(howl), deepcopy(quickattack), deepcopy(agility), deepcopy(flamethrower), deepcopy(sacredfire)][::-1]       },           
    'abra':         {'type': 'psychic',     'evolveAt': 12,     'evolveTo': 'kadabra',      'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [deepcopy(psybeam), deepcopy(tailwhip), None, None],                   'learnableAttacks': [deepcopy(disable), deepcopy(heal), deepcopy(irontail), deepcopy(confusion), deepcopy(shadowball), deepcopy(dreameater), deepcopy(psyshock), deepcopy(futuresight)][::-1]       },           
    'geodude':      {'type': 'rock',        'evolveAt': 18,     'evolveTo': 'graveler',     'baseDef': 31,  'baseSpeed': 16, 'startAttacks': [deepcopy(tackle), deepcopy(rockthrow), None, None],                   'learnableAttacks': [deepcopy(sandattack), deepcopy(mudslap), deepcopy(stoneedge), deepcopy(rockwrecker), deepcopy(headbutt), deepcopy(headsmash), deepcopy(earthquake)][::-1]         },           
    'shelldar':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'cloyster',     'baseDef': 19,  'baseSpeed': 16, 'startAttacks': [deepcopy(watergun), deepcopy(bubblebeam), None, None],                'learnableAttacks': [deepcopy(bite), deepcopy(icywind), deepcopy(lick), deepcopy(waterslap), deepcopy(aurorabeam), deepcopy(icebeam), deepcopy(iceburn), deepcopy(psyshock)][::-1]      },           
    'gastly':       {'type': 'ghost',       'evolveAt': 18,     'evolveTo': 'haunter',      'baseDef': 19,  'baseSpeed': 20, 'startAttacks': [deepcopy(lick), deepcopy(psybeam), None, None],                       'learnableAttacks': [deepcopy(hide), deepcopy(shadowball), deepcopy(curse), deepcopy(feintattack), deepcopy(pursuit), deepcopy(shadowpunch), deepcopy(crunch), deepcopy(dreameater), deepcopy(futuresight)][::-1]       },           
    'onix':         {'type': 'rock',        'evolveAt': None,   'evolveTo': None,           'baseDef': 31,  'baseSpeed': 20, 'startAttacks': [deepcopy(sandattack), deepcopy(rockthrow), None, None],               'learnableAttacks': [deepcopy(stoneedge), deepcopy(irontail), deepcopy(mudslap), deepcopy(earthquake), deepcopy(rockwrecker), deepcopy(headsmash), deepcopy(meteormash)][::-1]         },           
    'koffing':      {'type': 'poison',      'evolveAt': 18,     'evolveTo': 'weezing',      'baseDef': 21,  'baseSpeed': 15, 'startAttacks': [deepcopy(smokescreen), deepcopy(tackle), None, None],                 'learnableAttacks': [deepcopy(sandattack), deepcopy(acid), deepcopy(poisonfang), deepcopy(poisonpowder), deepcopy(sludgebomb), deepcopy(gunkshot)][::-1]      },           
    'horsea':       {'type': 'water',       'evolveAt': 18,     'evolveTo': 'seadra',       'baseDef': 15,  'baseSpeed': 14, 'startAttacks': [deepcopy(watergun), deepcopy(bubblebeam), None, None],                'learnableAttacks': [deepcopy(poisonsting), deepcopy(waterslap), deepcopy(hydropump), deepcopy(watercannon), deepcopy(icebeam)][::-1]         },           
    'staryu':       {'type': 'water',       'evolveAt': 16,     'evolveTo': 'starmie',      'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [deepcopy(watergun), deepcopy(swift), None, None],                     'learnableAttacks': [deepcopy(tackle), deepcopy(bubblebeam), deepcopy(quickattack), deepcopy(hydropump), deepcopy(watercannon), deepcopy(waterspout), deepcopy(hydrovortex)][::-1]        },           
    'scyther':      {'type': 'bug',         'evolveAt': None,   'evolveTo': None,           'baseDef': 17,  'baseSpeed': 33, 'startAttacks': [deepcopy(quickattack), deepcopy(cut), None, None],                    'learnableAttacks': [deepcopy(agility), deepcopy(razorleaf), deepcopy(leechlife), deepcopy(bugbite), deepcopy(scratch), deepcopy(stinger), deepcopy(megahorn), deepcopy(leafblade), deepcopy(hyperbeam)][::-1]      },           
    'magmar':       {'type': 'fire',        'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 19, 'startAttacks': [deepcopy(tackle), deepcopy(ember), None, None],                       'learnableAttacks': [deepcopy(flamethrower), deepcopy(headbutt), deepcopy(sandattack), deepcopy(ironpunch), deepcopy(firepunch), deepcopy(firespin), deepcopy(shelltrap), deepcopy(sacredfire)][::-1]      },           
    'magikarp':     {'type': 'water',       'evolveAt': 12,     'evolveTo': 'gyarados',     'baseDef': 19,  'baseSpeed': 14, 'startAttacks': [deepcopy(watergun), deepcopy(swift), None, None],                     'learnableAttacks': [deepcopy(tailwhip), deepcopy(pound), deepcopy(quickattack), deepcopy(waterslap), deepcopy(hydropump), deepcopy(watercannon), deepcopy(hydrovortex)][::-1]       },           
    'eevee':        {'type': 'normal',      'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 24, 'startAttacks': [deepcopy(tackle), deepcopy(swift), None, None],                       'learnableAttacks': [deepcopy(quickattack), deepcopy(bite), deepcopy(agility), deepcopy(scratch)][::-1]        },           
    
    
    'raichu':       {'type': 'electric',    'evolveAt': None,   'evolveTo': None            },           
    'charmeleon':   {'type': 'fire',        'evolveAt': 36,     'evolveTo': 'charizard'     },           
    'wartortle':    {'type': 'water',       'evolveAt': 38,     'evolveTo': 'blastoise'     },           
    'ivysaur':      {'type': 'grass',       'evolveAt': 36,     'evolveTo': 'venusaur'      },           
    'gloom':        {'type': 'grass',       'evolveAt': 28,     'evolveTo': 'vileplume'     },           
    'metapod':      {'type': 'bug',         'evolveAt': 10,     'evolveTo': 'butterfree'    },           
    'kakuna':       {'type': 'bug',         'evolveAt': 10,     'evolveTo': 'beedrill'      },           
    'pidgeotto':    {'type': 'flying',      'evolveAt': 32,     'evolveTo': 'pidgeot'       },           
    'arbok':        {'type': 'poison',      'evolveAt': None,   'evolveTo': None            },           
    'sandslash':    {'type': 'ground',      'evolveAt': None,   'evolveTo': None            },           
    'nidorina':     {'type': 'poison',      'evolveAt': 30,     'evolveTo': 'nidoqueen'     },           
    'nidorino':     {'type': 'poison',      'evolveAt': 30,     'evolveTo': 'nidoking'      },           
    'ninetales':    {'type': 'fire',        'evolveAt': None,   'evolveTo': None            },           
    'golbat':       {'type': 'flying',      'evolveAt': None,   'evolveTo': None            },           
    'dugtrio':      {'type': 'ground',      'evolveAt': None,   'evolveTo': None            },           
    'persian':      {'type': 'normal',      'evolveAt': None,   'evolveTo': None            },           
    'golduck':      {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'arcanine':     {'type': 'fire',        'evolveAt': None,   'evolveTo': None            },           
    'kadabra':      {'type': 'psychic',     'evolveAt': 26,     'evolveTo': 'alakazam'      },           
    'graveler':     {'type': 'rock',        'evolveAt': None,   'evolveTo': None            },           
    'cloyster':     {'type': 'ice',         'evolveAt': None,   'evolveTo': None            },           
    'haunter':      {'type': 'ghost',       'evolveAt': 34,     'evolveTo': 'gengar'        },           
    'weezing':      {'type': 'poison',      'evolveAt': None,   'evolveTo': None            },           
    'seadra':       {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'starmie':      {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'gyarados':     {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'vaporeon':     {'type': 'water',       'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [deepcopy(watergun), deepcopy(waterslap), deepcopy(aurorabeam), deepcopy(icywind), deepcopy(watercannon), deepcopy(blizzard), deepcopy(hydrovortex)][::-1]    },           
    'jolteon':      {'type': 'electric',    'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [deepcopy(thundershock), deepcopy(discharge), deepcopy(thunderbolt), deepcopy(bolttackle), deepcopy(electroball)][::-1]       },           
    'flareon':      {'type': 'fire',        'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [deepcopy(ember), deepcopy(flamethrower), deepcopy(firespin), deepcopy(fireblast), deepcopy(shelltrap)][::-1]     },           
    
    
    'charizard':    {'type': 'fire',        'evolveAt': None,   'evolveTo': None  },           
    'blastoise':    {'type': 'water',       'evolveAt': None,   'evolveTo': None  },           
    'venusaur':     {'type': 'grass',       'evolveAt': None,   'evolveTo': None  },           
    'vileplume':    {'type': 'grass',       'evolveAt': None,   'evolveTo': None  },           
    'butterfree':   {'type': 'flying',      'evolveAt': None,   'evolveTo': None  },           
    'beedrill':     {'type': 'flying',      'evolveAt': None,   'evolveTo': None  },           
    'pidgeot':      {'type': 'flying',      'evolveAt': None,   'evolveTo': None  },           
    'nidoqueen':    {'type': 'poison',      'evolveAt': None,   'evolveTo': None  },           
    'nidoking':     {'type': 'poison',      'evolveAt': None,   'evolveTo': None  },           
    'alakazam':     {'type': 'psychic',     'evolveAt': None,   'evolveTo': None  },           
    'gengar':       {'type': 'ghost',       'evolveAt': None,   'evolveTo': None  }           
}
