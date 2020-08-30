pokemon_types = ['fire', 'water', 'grass', 'electric', 'flying', 'normal', 'ice', 'ground', 
                'poison', 'bug', 'rock', 'steel', 'ghost', 'dark', 'psychic']


typeAdantages = {
    'fire': ['grass', 'steel', 'bug', 'ice'],
    'water': ['fire', 'rock', 'ground'],
    'grass': ['water', 'rock', 'ground'],
    'electric': ['water', 'flying'],
    'ice': ['grass', 'flying'],
    'psychic': [None],
    'ghost': ['psychic'],
    'dark': ['psychic', 'ghost'],
    'flying': ['bug', 'grass'],
    'normal': [None],
    'ground': ['fire', 'steel', 'rock', 'electric'],
    'poison': ['grass'],
    'steel': ['rock', 'ice'],
    'bug': ['psychic', 'dark'],
    'rock': ['ice', 'flying', 'fire', 'electric']
}

typeDisadantages = {
    'fire': ['water', 'rock', 'ground'],
    'water': ['grass', 'electric'],
    'grass': ['fire', 'bug', 'flying', 'poison'],
    'electric': ['rock', 'ground', 'steel'],
    'ice': ['steel', 'rock', 'fire'],
    'psychic': ['ghost', 'dark', 'bug'],
    'ghost': ['dark'],
    'dark': ['bug'],
    'flying': ['electric', 'ice', 'rock'],
    'normal': [None],
    'ground': ['water', 'grass', 'bug', 'ice'],
    'poison': ['ground', 'psychic'],
    'steel': ['fire', 'ground'],
    'bug': ['fire', 'flying', 'rock'],
    'rock': ['water', 'grass', 'steel']
}