from attacklist import *


def deepcopy(actualAttack):
    if not actualAttack: return actualAttack
    newattack = Attack(actualAttack.name, actualAttack.attCategory, actualAttack.baseDamage, actualAttack.pLevel, actualAttack.maxcount, heal=actualAttack.heal, accuracy=actualAttack.accuracy, recoil=actualAttack.recoil)
    return newattack

small_pokemons = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'caterpie', 'weedle', 'pidgey', 'ekans', 
                  'sandshrew', 'nidoran', 'clefairy', 'vulpix', 'jigglypuff', 'zubat',  'diglett', 'meowth', 'psyduck',  
                  'growlithe', 'abra', 'geodude', 'shellder', 'gastly', 'onix', 'cubone', 'koffing', 'horsea', 'staryu', 'scyther', 'magmar', 'magikarp', 
                  'eevee']

medium_pokemons = ['raichu', 'charmeleon', 'wartortle', 'ivysaur', 'metapod', 'kakuna', 'pidgeotto', 'arbok', 'sandslash', 
                   'nidorina', 'nidorino', 'clefable', 'ninetales',  'golbat',  'dugtrio', 
                   'persian', 'golduck',  'arcanine', 'kadabra', 'graveler', 'cloyster', 'haunter', 'weezing', 'marowak', 'seadra', 'starmie', 
                   'gyarados', 'vaporeon', 'jolteon', 'flareon']

large_pokemons = ['charizard', 'blastoise', 'venusaur', 'butterfree', 'beedrill', 'pidgeot', 'nidoqueen', 'nidoking', 'alakazam',  'gengar']

legendary_pokemons = ['zapdos', 'moltres', 'articuno', 'selmon jong un']



pokemonWorld = {
    
    'zapdos':          {'type': 'electric', 'evolveAt': None,   'evolveTo': None,          'baseDef': 100, 'baseSpeed': 130, 'startAttacks': [(thunderbolt), (electroball), (catastropika), (hyperbeam), (aeroblast), (aerialace), (heal), (airslash)], 'learnableAttacks': []         },           
    'moltres':         {'type': 'fire',     'evolveAt': None,   'evolveTo': None,          'baseDef': 150, 'baseSpeed': 120, 'startAttacks': [(firespin), (flamethrower), (sacredfire), (fireblast), (aeroblast), (heal)], 'learnableAttacks': []      },           
    'articuno':        {'type': 'water',    'evolveAt': None,   'evolveTo': None,          'baseDef': 240, 'baseSpeed': 121, 'startAttacks': [(watercannon), (hydrovortex), (waterspout), (iceburn), (icebeam), (blizzard), (aurorabeam), (hyperbeam), (aerialace)], 'learnableAttacks': []        },           
    'selmon jong un':  {'type': 'dark',     'evolveAt': None,   'evolveTo': None,          'baseDef': 600, 'baseSpeed': 320, 'startAttacks': [(crunch), (hyperbeam), (futuresight), (shadowpunch), (landwrath), (catastropika), (sacredfire), (watercannon), (gigadrain), (heal)], 'learnableAttacks': []      },           
    

    'pikachu':      {'type': 'electric',    'evolveAt': None,   'evolveTo': 'raichu',       'baseDef': 10,  'baseSpeed': 30, 'startAttacks': [(thundershock), (tackle), None, None],                'learnableAttacks': [(quickattack), (thunderbolt), (agility), (irontail), (thunderpunch), (discharge), (bolttackle), (electroball), (catastropika)][::-1]       },           
    'charmander':   {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'charmeleon',   'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(ember), (tackle), None, None],                     'learnableAttacks': [(swift), (flamethrower), (firepunch), (firespin), (shelltrap), (fireblast), (sacredfire)][::-1]       },           
    'squirtle':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'wartortle',    'baseDef': 24,  'baseSpeed': 21, 'startAttacks': [(watergun), (tackle), None, None],                    'learnableAttacks': [(headbutt), (bubblebeam), (mudslap), (hydropump), (watercannon), (hydrovortex)][::-1]         },           
    'bulbasaur':    {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'ivysaur',      'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(razorleaf), (tackle), None, None],                   'learnableAttacks': [(vinewhip), (disable), (stunspore), (gigadrain), (frenzy), (leafblade), (solarbeam)][::-1]         },           
    'oddish':       {'type': 'grass',       'evolveAt': 18,     'evolveTo': 'gloom',        'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(razorleaf), (tackle), None, None],                   'learnableAttacks': [(vinewhip), (quickattack), (stunspore), (leafblade), (solarbeam)][::-1]         },           
    'caterpie':     {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'metapod',      'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [(stringshot), (bugbite), (leechlife), None],  'learnableAttacks': [(tackle), (harden), (gust), (whirlwind), (wingattack)][::-1]        },           
    'weedle':       {'type': 'bug',         'evolveAt': 7,      'evolveTo': 'kakuna',       'baseDef': 5,   'baseSpeed': 13, 'startAttacks': [(poisonsting), (bugbite), (stinger), None],   'learnableAttacks': [(tackle), (poisonpowder), (gust), (leechlife), (wingattack)][::-1]        },           
    'pidgey':       {'type': 'flying',      'evolveAt': 16,     'evolveTo': 'pidgeotto',    'baseDef': 12,  'baseSpeed': 23, 'startAttacks': [(quickattack), (gust), None, None],                   'learnableAttacks': [(whirlwind), (agility), (sandattack), (wingattack), (fly), (aerialace), (airslash), (aeroblast)][::-1]       },           
    'ekans':        {'type': 'poison',      'evolveAt': 14,     'evolveTo': 'arbok',        'baseDef': 14,  'baseSpeed': 21, 'startAttacks': [(acid), (poisonsting), None, None],                   'learnableAttacks': [(poisonpowder), (quickattack), (tailwhip), (agility), (leechlife), (poisonfang), (gunkshot)][::-1]       },           
    'sandshrew':    {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'sandslash',    'baseDef': 30,  'baseSpeed': 18, 'startAttacks': [(sandattack), (tackle), None, None],                  'learnableAttacks': [(dig), (quickattack), (scratch), (mudslap)][::-1]       },           
    'nidoran':      {'type': 'poison',      'evolveAt': 15,     'evolveTo': None,           'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(tackle), (poisonsting), None, None],                 'learnableAttacks': [(sandattack), (quickattack), (bite), (agility), (headbutt), (megahorn), (acid), (hyperbeam), (icebeam), (icepunch), (thunderbolt), (earthquake)][::-1]        },           
    'clefairy':     {'type': 'normal',      'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 16, 'startAttacks': [(growl), (pound), None, None],                        'learnableAttacks': [(sing)][::-1]        },           
    'vulpix':       {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'ninetales',    'baseDef': 18,  'baseSpeed': 19, 'startAttacks': [(tackle), (ember), None, None],                       'learnableAttacks': [(flamethrower), (quickattack), (headbutt), (firespin), (scratch), (bite), (fireblast)][::-1]         },           
    'jigglypuff':   {'type': 'psychic',     'evolveAt': None,   'evolveTo': None,           'baseDef': 13,  'baseSpeed': 20, 'startAttacks': [(pound), (sing), None, None],                         'learnableAttacks': [(tackle), (heal), (headbutt), (infactuate), (cut), (curse), (ironpunch), (hyperbeam)][::-1]         },           
    'zubat':        {'type': 'flying',      'evolveAt': 14,     'evolveTo': 'golbat',       'baseDef': 14,  'baseSpeed': 23, 'startAttacks': [(poisonsting), (whirlwind), None, None],              'learnableAttacks': [(wingattack), (airslash), (quickattack), (poisonfang), (stinger)][::-1]        },           
    'diglett':      {'type': 'ground',      'evolveAt': 18,     'evolveTo': 'dugtrio',      'baseDef': 19,  'baseSpeed': 21, 'startAttacks': [(sandattack), (dig), None, None],                     'learnableAttacks': [(mudslap), (cut), (rockthrow), (headsmash), (stoneedge), (earthquake), (landwrath)][::-1]        },           
    'meowth':       {'type': 'normal',      'evolveAt': 18,     'evolveTo': 'persian',      'baseDef': 18,  'baseSpeed': 21, 'startAttacks': [(scratch), (tackle), (tailwhip), None],       'learnableAttacks': [(agility), (quickattack), (sandattack), (irontail), (bite), (feintattack), (hyperbeam)][::-1]      },           
    'psyduck':      {'type': 'water',       'evolveAt': 18,     'evolveTo': 'golduck',      'baseDef': 17,  'baseSpeed': 11, 'startAttacks': [(watergun), (tackle), None, None],                    'learnableAttacks': [(scratch), (bubblebeam), (agility), (psybeam), (confusion), (heal), (psyshock), (hyperbeam)][::-1]      },           
    'growlithe':    {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'arcanine',     'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [(tackle), (bite), None, None],                        'learnableAttacks': [(firespin), (scratch), (howl), (quickattack), (agility), (flamethrower), (sacredfire)][::-1]       },           
    'abra':         {'type': 'psychic',     'evolveAt': 12,     'evolveTo': 'kadabra',      'baseDef': 19,  'baseSpeed': 23, 'startAttacks': [(psybeam), (tailwhip), None, None],                   'learnableAttacks': [(disable), (heal), (irontail), (confusion), (shadowball), (dreameater), (psyshock), (futuresight)][::-1]       },           
    'geodude':      {'type': 'rock',        'evolveAt': 18,     'evolveTo': 'graveler',     'baseDef': 31,  'baseSpeed': 16, 'startAttacks': [(tackle), (rockthrow), None, None],                   'learnableAttacks': [(sandattack), (mudslap), (stoneedge), (rockwrecker), (headbutt), (headsmash), (earthquake)][::-1]         },           
    'shelldar':     {'type': 'water',       'evolveAt': 18,     'evolveTo': 'cloyster',     'baseDef': 19,  'baseSpeed': 16, 'startAttacks': [(watergun), (bubblebeam), None, None],                'learnableAttacks': [(bite), (icywind), (lick), (waterslap), (aurorabeam), (icebeam), (iceburn), (psyshock)][::-1]      },           
    'gastly':       {'type': 'ghost',       'evolveAt': 18,     'evolveTo': 'haunter',      'baseDef': 19,  'baseSpeed': 20, 'startAttacks': [(lick), (psybeam), None, None],                       'learnableAttacks': [(hide), (shadowball), (curse), (feintattack), (pursuit), (shadowpunch), (crunch), (dreameater), (futuresight)][::-1]       },           
    'onix':         {'type': 'rock',        'evolveAt': None,   'evolveTo': None,           'baseDef': 31,  'baseSpeed': 20, 'startAttacks': [(sandattack), (rockthrow), None, None],               'learnableAttacks': [(stoneedge), (irontail), (mudslap), (earthquake), (rockwrecker), (headsmash), (meteormash)][::-1]         },           
    'cubone':       {'type': 'ground',      'evolveAt': 28,     'evolveTo': 'marowak',      'baseDef': 20,  'baseSpeed': 16, 'startAttacks': [(growl), (boneclub), None, None],                     'learnableAttacks': [(tailwhip), (headbutt), (bonemerang)][::-1]         },           
    'koffing':      {'type': 'poison',      'evolveAt': 18,     'evolveTo': 'weezing',      'baseDef': 21,  'baseSpeed': 15, 'startAttacks': [(smokescreen), (tackle), None, None],                 'learnableAttacks': [(sandattack), (acid), (poisonfang), (poisonpowder), (sludgebomb), (gunkshot)][::-1]      },           
    'horsea':       {'type': 'water',       'evolveAt': 18,     'evolveTo': 'seadra',       'baseDef': 15,  'baseSpeed': 14, 'startAttacks': [(watergun), (bubblebeam), None, None],                'learnableAttacks': [(poisonsting), (waterslap), (hydropump), (watercannon), (icebeam)][::-1]         },           
    'staryu':       {'type': 'water',       'evolveAt': 16,     'evolveTo': 'starmie',      'baseDef': 13,  'baseSpeed': 15, 'startAttacks': [(watergun), (swift), None, None],                     'learnableAttacks': [(tackle), (bubblebeam), (quickattack), (hydropump), (watercannon), (waterspout), (hydrovortex)][::-1]        },           
    'scyther':      {'type': 'bug',         'evolveAt': None,   'evolveTo': None,           'baseDef': 17,  'baseSpeed': 33, 'startAttacks': [(quickattack), (cut), None, None],                    'learnableAttacks': [(agility), (razorleaf), (leechlife), (bugbite), (scratch), (stinger), (megahorn), (leafblade), (hyperbeam)][::-1]      },           
    'magmar':       {'type': 'fire',        'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 19, 'startAttacks': [(tackle), (ember), None, None],                       'learnableAttacks': [(flamethrower), (headbutt), (sandattack), (ironpunch), (firepunch), (firespin), (shelltrap), (sacredfire)][::-1]      },           
    'magikarp':     {'type': 'water',       'evolveAt': 12,     'evolveTo': 'gyarados',     'baseDef': 19,  'baseSpeed': 14, 'startAttacks': [(watergun), (swift), None, None],                     'learnableAttacks': [(tailwhip), (pound), (quickattack), (waterslap), (hydropump), (watercannon), (hydrovortex)][::-1]       },           
    'eevee':        {'type': 'normal',      'evolveAt': None,   'evolveTo': None,           'baseDef': 19,  'baseSpeed': 24, 'startAttacks': [(tackle), (swift), None, None],                       'learnableAttacks': [(quickattack), (bite), (agility), (scratch)][::-1]        },           
    
    
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
    'clefable':     {'type': 'normal',      'evolveAt': None,   'evolveTo': None            },           
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
    'marowak':      {'type': 'ground',      'evolveAt': None,   'evolveTo': None            },           
    'weezing':      {'type': 'poison',      'evolveAt': None,   'evolveTo': None            },           
    'seadra':       {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'starmie':      {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'gyarados':     {'type': 'water',       'evolveAt': None,   'evolveTo': None            },           
    'vaporeon':     {'type': 'water',       'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [(watergun), (waterslap), (aurorabeam), (icywind), (watercannon), (blizzard), (hydrovortex)][::-1]    },           
    'jolteon':      {'type': 'electric',    'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [(thundershock), (discharge), (thunderbolt), (bolttackle), (electroball)][::-1]       },           
    'flareon':      {'type': 'fire',        'evolveAt': None,   'evolveTo': None,       'learnableAttacks': [(ember), (flamethrower), (firespin), (fireblast), (shelltrap)][::-1]     },           
    
    
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


for pokemon in pokemonWorld:
    startAttacks = pokemonWorld[pokemon].get('startAttacks', [])
    learnableAttacks = pokemonWorld[pokemon].get('learnableAttacks', [])
    for i in range(len(startAttacks)):
        startAttacks[i] = deepcopy(startAttacks[i])

    for i in range(len(learnableAttacks)):
        learnableAttacks[i] = deepcopy(learnableAttacks[i])

    if startAttacks:
        pokemonWorld[pokemon]['startAttacks'] = startAttacks
    if learnableAttacks:
        pokemonWorld[pokemon]['learnableAttacks'] = learnableAttacks