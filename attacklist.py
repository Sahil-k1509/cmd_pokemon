from attacks import Attack

# Initialize all attacks
# ----------------------------------------------------------------------------------------- #

# Fire type
flamethrower = Attack(name='flamethrower', attCategory='fire', baseDamage=20, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
ember = Attack(name='ember', attCategory='fire', baseDamage=13, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.65)
firepunch = Attack(name='fire punch', attCategory='fire', baseDamage=16, pokemonLevel=0, baseCount=8, recoil=0, heal=0, accuracy=0.9)
firespin = Attack(name='fire spin', attCategory='fire', baseDamage=30, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.8)
shelltrap = Attack(name='shell trap', attCategory='fire', baseDamage=135, pokemonLevel=0, baseCount=2, recoil=40, heal=0, accuracy=0.8)
fireblast = Attack(name='fire blast', attCategory='fire', baseDamage=140, pokemonLevel=0, baseCount=4, recoil=30, heal=0, accuracy=0.85)
sacredfire = Attack(name='sacred fire', attCategory='fire', baseDamage=350, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=30, accuracy=1)


# Electric type
thundershock = Attack(name='thundershock', attCategory='electric', baseDamage=10, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
thunderbolt = Attack(name='thunderbolt', attCategory='electric', baseDamage=35, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.95)
thunderpunch = Attack(name='thunder punch', attCategory='electric', baseDamage=50, pokemonLevel=0, baseCount=8, recoil=0, heal=0, accuracy=0.96)
bolttackle = Attack(name='bolt tackle', attCategory='electric', baseDamage=100, pokemonLevel=0, baseCount=2, recoil=40, heal=0, accuracy=0.8)
electroball = Attack(name='electro ball', attCategory='electric', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.65)
discharge = Attack(name='discharge', attCategory='electric', baseDamage=50, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=0.85)
catastropika = Attack(name='Catastropika', attCategory='electric', baseDamage=285, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=0, accuracy=1)


# Water type
watergun = Attack(name='watergun', attCategory='water', baseDamage=15, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
watercannon = Attack(name='watercannon', attCategory='water', baseDamage=100, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=1)
hydropump = Attack(name='hydro pump', attCategory='water', baseDamage=67, pokemonLevel=0, baseCount=8, recoil=0, heal=0, accuracy=1)
bubblebeam = Attack(name='bubblebeam', attCategory='water', baseDamage=40, pokemonLevel=0, baseCount=8, recoil=20, heal=0, accuracy=0.8)
waterspout = Attack(name='water spout', attCategory='water', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.65)
waterslap = Attack(name='water slap', attCategory='water', baseDamage=50, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=0.85)
hydrovortex = Attack(name='hydro vortex', attCategory='water', baseDamage=270, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=40, accuracy=1)


# Grass type
vinewhip = Attack(name='vine whip', attCategory='grass', baseDamage=12, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
razorleaf = Attack(name='razor leaf', attCategory='grass', baseDamage=5, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
stunspore = Attack(name='stun spore', attCategory='grass', baseDamage=8, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.5)
gigadrain = Attack(name='giga drain', attCategory='grass', baseDamage=80, pokemonLevel=0, baseCount=3, recoil=0, heal=40, accuracy=0.9)
frenzy = Attack(name='frenzy', attCategory='grass', baseDamage=60, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.75)
leafblade = Attack(name='leaf blade', attCategory='grass', baseDamage=80, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=0.85)
solarbeam = Attack(name='solar beam', attCategory='grass', baseDamage=300, pokemonLevel=0, baseCount=2, increasable=0, recoil=20, heal=0, accuracy=1)


# Flying type
gust = Attack(name='gust', attCategory='flying', baseDamage=4, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
whirlwind = Attack(name='whirl wind', attCategory='flying', baseDamage=20, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
wingattack = Attack(name='wing attack', attCategory='flying', baseDamage=37, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
airslash = Attack(name='air slash', attCategory='flying', baseDamage=80, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)
aerialace = Attack(name='aerial ace', attCategory='flying', baseDamage=60, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.75)
aeroblast = Attack(name='aero blast', attCategory='flying', baseDamage=100, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.85)
fly = Attack(name='fly', attCategory='flying', baseDamage=60, pokemonLevel=0, baseCount=4, increasable=0, recoil=0, heal=0, accuracy=1)


# Normal type
pound = Attack(name='pound', attCategory='normal', baseDamage=10, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
tackle = Attack(name='tackle', attCategory='normal', baseDamage=5, pokemonLevel=0, baseCount=13, recoil=0, heal=0, accuracy=1)
swift = Attack(name='swift', attCategory='normal', baseDamage=5, pokemonLevel=0, baseCount=13, recoil=0, heal=0, accuracy=1)
tailwhip = Attack(name='tail whip', attCategory='normal', baseDamage=8, pokemonLevel=0, baseCount=13, recoil=0, heal=0, accuracy=1)
agility = Attack(name='agility', attCategory='normal', baseDamage=0, pokemonLevel=0, baseCount=8, recoil=0, heal=0, accuracy=1)
harden = Attack(name='harden', attCategory='normal', baseDamage=0, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)
quickattack = Attack(name='quick attack', attCategory='normal', baseDamage=15, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)
scratch = Attack(name='scratch', attCategory='normal', baseDamage=8, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)
cut = Attack(name='cut', attCategory='normal', baseDamage=15, pokemonLevel=0, baseCount=13, recoil=0, heal=0, accuracy=0.9)
headbutt = Attack(name='headbutt', attCategory='normal', baseDamage=6, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.75)
disable = Attack(name='disable', attCategory='normal', baseDamage=40, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
hyperbeam = Attack(name='hyper beam', attCategory='normal', baseDamage=150, pokemonLevel=0, baseCount=2, increasable=0, recoil=20, heal=0, accuracy=0.9)


# Ice type
icepunch = Attack(name='ice punch', attCategory='ice', baseDamage=70, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
aurorabeam = Attack(name='aurora beam', attCategory='ice', baseDamage=50, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.9)
icebeam = Attack(name='ice beam', attCategory='ice', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)
icywind = Attack(name='icy wind', attCategory='ice', baseDamage=40, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)
blizzard = Attack(name='blizzard', attCategory='ice', baseDamage=70, pokemonLevel=0, baseCount=3, recoil=30, heal=0, accuracy=1)
iceburn = Attack(name='ice burn', attCategory='ice', baseDamage=150, pokemonLevel=0, baseCount=2, recoil=0, heal=20, accuracy=1)


# Ground type
sandattack = Attack(name='sandattack', attCategory='ground', baseDamage=17, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
dig = Attack(name='dig', attCategory='ground', baseDamage=35, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
earthquake = Attack(name='earthquake', attCategory='ground', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)
mudslap = Attack(name='mudslap', attCategory='ground', baseDamage=16, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)
landwrath = Attack(name='land\'s wrath', attCategory='ground', baseDamage=170, pokemonLevel=0, baseCount=3, recoil=30, heal=0, accuracy=1)


# Poison type
poisonsting = Attack(name='poison sting', attCategory='poison', baseDamage=3, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=0.8)
poisonpowder = Attack(name='poison powder', attCategory='poison', baseDamage=5, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)
acid = Attack(name='acid', attCategory='poison', baseDamage=20, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=1)
gunkshot = Attack(name='gunk shot', attCategory='poison', baseDamage=120, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=1)
sludgebomb = Attack(name='sludge bomb', attCategory='poison', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)
poisonfang = Attack(name='poison fang', attCategory='poison', baseDamage=21, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)
smokescreen = Attack(name='smoke screen', attCategory='poison', baseDamage=0, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)


# Bug type
stringshot = Attack(name='string shot', attCategory='bug', baseDamage=3, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=0.9)
leechlife = Attack(name='leech life', attCategory='bug', baseDamage=14, pokemonLevel=0, baseCount=6, recoil=0, heal=10, accuracy=1)
megahorn = Attack(name='mega horn', attCategory='bug', baseDamage=120, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)
bugbite = Attack(name='bug bite', attCategory='bug', baseDamage=8, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)
stinger = Attack(name='stinger', attCategory='bug', baseDamage=10, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)


# Rock type
rockthrow = Attack(name='rock throw', attCategory='rock', baseDamage=40, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
rockwrecker = Attack(name='rock wrecker', attCategory='rock', baseDamage=90, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
stoneedge = Attack(name='stone edge', attCategory='rock', baseDamage=60, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.8)
headsmash = Attack(name='head smash', attCategory='rock', baseDamage=140, pokemonLevel=0, baseCount=3, recoil=0, heal=0, accuracy=0.9)


# Steel type
ironpunch = Attack(name='iron punch', attCategory='steel', baseDamage=80, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
irontail = Attack(name='iron tail', attCategory='steel', baseDamage=60, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=0.9)
meteormash = Attack(name='meteor mash', attCategory='steel', baseDamage=90, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.9)


# Ghost type
lick = Attack(name='lick', attCategory='ghost', baseDamage=40, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
curse = Attack(name='curse', attCategory='ghost', baseDamage=90, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
shadowball = Attack(name='shadow ball', attCategory='ghost', baseDamage=60, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.8)
shadowpunch = Attack(name='shadow punch', attCategory='ghost', baseDamage=140, pokemonLevel=0, baseCount=3, recoil=0, heal=0, accuracy=0.9)
hide = Attack(name='hide', attCategory='ghost', baseDamage=0, pokemonLevel=0, baseCount=2, recoil=0, heal=40, accuracy=1)


# Dark type
bite = Attack(name='bite', attCategory='dark', baseDamage=60, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
feintattack = Attack(name='feint attack', attCategory='dark', baseDamage=60, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
howl = Attack(name='howl', attCategory='dark', baseDamage=0, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
pursuit = Attack(name='pursuit', attCategory='dark', baseDamage=50, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.9)
crunch = Attack(name='crunch', attCategory='dark', baseDamage=90, pokemonLevel=0, baseCount=6, recoil=0, heal=40, accuracy=1)


# Psychic type
psybeam = Attack(name='psy beam', attCategory='psychic', baseDamage=40, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=1)
confusion = Attack(name='confusion', attCategory='psychic', baseDamage=90, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)
dreameater = Attack(name='dream eater', attCategory='psychic', baseDamage=60, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=0.8)
futuresight = Attack(name='future sight', attCategory='psychic', baseDamage=140, pokemonLevel=0, baseCount=3, recoil=0, heal=0, accuracy=0.9)
sing = Attack(name='sing', attCategory='psychic', baseDamage=0, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.5)
infactuate = Attack(name='infactuate', attCategory='psychic', baseDamage=0, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.5)
psyshock = Attack(name='psyshock', attCategory='psychic', baseDamage=130, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.9)
heal = Attack(name='heal', attCategory='psychic', baseDamage=0, pokemonLevel=0, baseCount=5, recoil=0, heal=40, accuracy=1)



# ----------------------------------------------------------------------------------------- #

