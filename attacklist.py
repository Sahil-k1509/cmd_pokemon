from attacks import Attack

# Initialize all attacks
# ----------------------------------------------------------------------------------------- #

# Fire type---------------------------

#new moves added
blastburn = Attack(name='blast burn', attCategory='fire', baseDamage=150, pokemonLevel=0, baseCount=5, recoil=15, heal=0, accuracy=0.9)
blazekick = Attack(name='blaze kick', attCategory='fire', baseDamage=85, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
fierydance = Attack(name='fiery dance', attCategory='fire', baseDamage=80, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
firefang = Attack(name='fire fang', attCategory='fire', baseDamage=65, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)
flameburst = Attack(name='flame burst', attCategory='fire', baseDamage=70, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
flamecharge = Attack(name='flame charge', attCategory='fire', baseDamage=50, pokemonLevel=0, baseCount=20, recoil=0, heal=10, accuracy=0.9)
flamewheel = Attack(name='flame wheel', attCategory='fire', baseDamage=60, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
flareblitz = Attack(name='flare blitz', attCategory='fire', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=20, heal=0, accuracy=1)
heatwave = Attack(name='heat wave', attCategory='fire', baseDamage=95, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)


#modified
flamethrower = Attack(name='flamethrower', attCategory='fire', baseDamage=85, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
ember = Attack(name='ember', attCategory='fire', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
firepunch = Attack(name='fire punch', attCategory='fire', baseDamage=75, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
firespin = Attack(name='fire spin', attCategory='fire', baseDamage=35, pokemonLevel=0, baseCount=35, recoil=0, heal=0, accuracy=0.85)
fireblast = Attack(name='fire blast', attCategory='fire', baseDamage=110, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.7)

#not modified
shelltrap = Attack(name='shell trap', attCategory='fire', baseDamage=235, pokemonLevel=0, baseCount=2, recoil=40, heal=0, accuracy=0.8)
sacredfire = Attack(name='sacred fire', attCategory='fire', baseDamage=350, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=30, accuracy=1)


# Electric type------------------------

#new
nuzzle = Attack(name='nuzzle', attCategory='electric', baseDamage=20, pokemonLevel=0, baseCount=20, recoil=0, heal=7, accuracy=1)
chargebeam = Attack(name='charge beam', attCategory='electric', baseDamage=50, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
paraboliccharge = Attack(name='parabolic charge', attCategory='electric', baseDamage=65, pokemonLevel=0, baseCount=15, recoil=0, heal=25, accuracy=1)
thunderfang = Attack(name='thunder fang', attCategory='electric', baseDamage=65, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)
wildcharge = Attack(name='wild charge', attCategory='electric', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=20, heal=0, accuracy=1)
thunder = Attack(name='thunder', attCategory='electric', baseDamage=110, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.7)

#modified
thundershock = Attack(name='thundershock', attCategory='electric', baseDamage=40, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=1)
thunderbolt = Attack(name='thunderbolt', attCategory='electric', baseDamage=90, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
thunderpunch = Attack(name='thunder punch', attCategory='electric', baseDamage=75, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
discharge = Attack(name='discharge', attCategory='electric', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)

#not modified
bolttackle = Attack(name='bolt tackle', attCategory='electric', baseDamage=140, pokemonLevel=0, baseCount=2, recoil=40, heal=0, accuracy=0.8)
electroball = Attack(name='electro ball', attCategory='electric', baseDamage=180, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.65)
catastropika = Attack(name='Catastropika', attCategory='electric', baseDamage=285, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=0, accuracy=1)


# Water type---------------------------------
#new
waterfall = Attack(name='waterfall', attCategory='water', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
waterpledge = Attack(name='water pledge', attCategory='water', baseDamage=75, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
surf = Attack(name='surf', attCategory='water', baseDamage=95, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.9)
aquaring = Attack(name='aqua ring', attCategory='water', baseDamage=0, pokemonLevel=0, baseCount=10, recoil=0, heal=30, accuracy=1)

#modified
watergun = Attack(name='watergun', attCategory='water', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
bubblebeam = Attack(name='bubblebeam', attCategory='water', baseDamage=85, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
hydropump = Attack(name='hydro pump', attCategory='water', baseDamage=110, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.8)

#not modified
hydrovortex = Attack(name='hydro vortex', attCategory='water', baseDamage=270, pokemonLevel=0, baseCount=1, increasable=0, recoil=0, heal=40, accuracy=1)
watercannon = Attack(name='watercannon', attCategory='water', baseDamage=100, pokemonLevel=0, baseCount=6, recoil=0, heal=0, accuracy=1)
waterspout = Attack(name='water spout', attCategory='water', baseDamage=80, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.65)
waterslap = Attack(name='water slap', attCategory='water', baseDamage=60, pokemonLevel=0, baseCount=7, recoil=0, heal=0, accuracy=0.85)


# Grass type-------------------------------
#new
synthesis = Attack(name='synthesis', attCategory='grass', baseDamage=0, pokemonLevel=0, baseCount=5, recoil=0, heal=60, accuracy=1)
woodhammer = Attack(name='wood hammer', attCategory='grass', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=20, heal=0, accuracy=1)
megadrain = Attack(name='mega drain', attCategory='grass', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=20, accuracy=0.9)

#modified
vinewhip = Attack(name='vine whip', attCategory='grass', baseDamage=85, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
razorleaf = Attack(name='razor leaf', attCategory='grass', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
stunspore = Attack(name='stun spore', attCategory='grass', baseDamage=30, pokemonLevel=0, baseCount=35, recoil=0, heal=0, accuracy=0.95)
frenzy = Attack(name='frenzy', attCategory='grass', baseDamage=110, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.8)
leafblade = Attack(name='leaf blade', attCategory='grass', baseDamage=95, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
gigadrain = Attack(name='giga drain', attCategory='grass', baseDamage=90, pokemonLevel=0, baseCount=10, recoil=0, heal=40, accuracy=0.9)


#not modified
solarbeam = Attack(name='solar beam', attCategory='grass', baseDamage=300, pokemonLevel=0, baseCount=2, increasable=0, recoil=20, heal=0, accuracy=1)

# Flying type--------------------------
#new
roost = Attack(name='roost', attCategory='flying', baseDamage=0, pokemonLevel=0, baseCount=5, recoil=0, heal=60, accuracy=1)
hurricane = Attack(name='hurricane', attCategory='flying', baseDamage=110, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.7)
peck = Attack(name='peck', attCategory='flying', baseDamage=35, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=0.95)


#modified
gust = Attack(name='gust', attCategory='flying', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
wingattack = Attack(name='wing attack', attCategory='flying', baseDamage=60, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.85)
airslash = Attack(name='air slash', attCategory='flying', baseDamage=75, pokemonLevel=0, baseCount=13, recoil=0, heal=0, accuracy=0.9)
aerialace = Attack(name='aerial ace', attCategory='flying', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
fly = Attack(name='fly', attCategory='flying', baseDamage=95, pokemonLevel=0, baseCount=10, increasable=0, recoil=0, heal=0, accuracy=0.9)
whirlwind = Attack(name='whirl wind', attCategory='flying', baseDamage=50, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)

#not modified
aeroblast = Attack(name='aero blast', attCategory='flying', baseDamage=100, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.85)



# Normal type------------------------------
#new
headcharge = Attack(name='head charge', attCategory='normal', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=20, heal=0, accuracy=1)


#modified
pound = Attack(name='pound', attCategory='normal', baseDamage=35, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=1)
tackle = Attack(name='tackle', attCategory='normal', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
swift = Attack(name='swift', attCategory='normal', baseDamage=60, pokemonLevel=0, baseCount=15,recoil=0, heal=0, accuracy=1)
tailwhip = Attack(name='tail whip', attCategory='normal', baseDamage=25, pokemonLevel=0, baseCount=40, recoil=0, heal=0, accuracy=0.95)
quickattack = Attack(name='quick attack', attCategory='normal', baseDamage=45, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.95)
scratch = Attack(name='scratch', attCategory='normal', baseDamage=40, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
cut = Attack(name='cut', attCategory='normal', baseDamage=50, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.9)
headbutt = Attack(name='headbutt', attCategory='normal', baseDamage=70, pokemonLevel=0, baseCount=15, recoil=5, heal=0, accuracy=1)
disable = Attack(name='disable', attCategory='normal', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.85)


#not modified
hyperbeam = Attack(name='hyper beam', attCategory='normal', baseDamage=230, pokemonLevel=0, baseCount=2, increasable=0, recoil=20, heal=0, accuracy=0.9)
agility = Attack(name='agility', attCategory='normal', baseDamage=0, pokemonLevel=0, baseCount=8, recoil=0, heal=0, accuracy=1)
harden = Attack(name='harden', attCategory='normal', baseDamage=0, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)


# Ice type------------------------------
#new
sheercold = Attack(name='sheer cold', attCategory='ice', baseDamage=300, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.2)
icefang = Attack(name='ice fang', attCategory='ice', baseDamage=65, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)
powdersnow = Attack(name='powder snow', attCategory='ice', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)

#modified
icepunch = Attack(name='ice punch', attCategory='ice', baseDamage=75, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
aurorabeam = Attack(name='aurora beam', attCategory='ice', baseDamage=65, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.9)
icebeam = Attack(name='ice beam', attCategory='ice', baseDamage=85, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
icywind = Attack(name='icy wind', attCategory='ice', baseDamage=55, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.9)
blizzard = Attack(name='blizzard', attCategory='ice', baseDamage=110, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.7)

#not modified
iceburn = Attack(name='ice burn', attCategory='ice', baseDamage=250, pokemonLevel=0, baseCount=2, recoil=0, heal=20, accuracy=1)


# Ground type------------------------------
#new
fissure = Attack(name='fissure', attCategory='ground', baseDamage=300, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.2)
mudbomb = Attack(name='mud bomb', attCategory='ground', baseDamage=65, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.85)
mudshot = Attack(name='mud shot', attCategory='ground', baseDamage=55, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)


#modified
sandattack = Attack(name='sandattack', attCategory='ground', baseDamage=15, pokemonLevel=0, baseCount=15, recoil=0, heal=5, accuracy=0.8)
dig = Attack(name='dig', attCategory='ground', baseDamage=80, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
earthquake = Attack(name='earthquake', attCategory='ground', baseDamage=100, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
mudslap = Attack(name='mudslap', attCategory='ground', baseDamage=20, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)

#not modified
landwrath = Attack(name='land\'s wrath', attCategory='ground', baseDamage=210, pokemonLevel=0, baseCount=3, recoil=30, heal=0, accuracy=1)


# Poison type-----------------------------
#new
crosspoison = Attack(name='cross poison', attCategory='poison', baseDamage=70, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
poisonjab = Attack(name='poison jab', attCategory='poison', baseDamage=80, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
poisontail = Attack(name='poison tail', attCategory='poison', baseDamage=50, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)

#modified
poisonsting = Attack(name='poison sting', attCategory='poison', baseDamage=15, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=0.95)
acid = Attack(name='acid', attCategory='poison', baseDamage=40, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
gunkshot = Attack(name='gunk shot', attCategory='poison', baseDamage=120, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.8)
sludgebomb = Attack(name='sludge bomb', attCategory='poison', baseDamage=85, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
poisonfang = Attack(name='poison fang', attCategory='poison', baseDamage=65, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)


#not modified
poisonpowder = Attack(name='poison powder', attCategory='poison', baseDamage=5, pokemonLevel=0, baseCount=9, recoil=0, heal=0, accuracy=1)
smokescreen = Attack(name='smoke screen', attCategory='poison', baseDamage=10, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=1)

# Bug type----------------------------------
#new 
bugbuzz = Attack(name='bug buzz', attCategory='bug', baseDamage=90, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
signalbeam = Attack(name='signal beam', attCategory='bug', baseDamage=75, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
xscissor = Attack(name='x-scissor', attCategory='bug', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)


#modified
stringshot = Attack(name='string shot', attCategory='bug', baseDamage=15, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=0.95)
leechlife = Attack(name='leech life', attCategory='bug', baseDamage=80, pokemonLevel=0, baseCount=10, recoil=0, heal=30, accuracy=1)
megahorn = Attack(name='mega horn', attCategory='bug', baseDamage=120, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.85)
bugbite = Attack(name='bug bite', attCategory='bug', baseDamage=60, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
stinger = Attack(name='stinger', attCategory='bug', baseDamage=50, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)


# Rock type----------------------------------
#new
rockslide = Attack(name='rock slide', attCategory='rock', baseDamage=75, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)
rocktomb = Attack(name='rock tomb', attCategory='rock', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)
rollout = Attack(name='rollout', attCategory='rock', baseDamage=30, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=0.9)
rockpolish = Attack(name='rock polish', attCategory='rock', baseDamage=0, pokemonLevel=0, baseCount=10, recoil=0, heal=30, accuracy=1)

#modified
rockthrow = Attack(name='rock throw', attCategory='rock', baseDamage=50, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.9)
rockwrecker = Attack(name='rock wrecker', attCategory='rock', baseDamage=150, pokemonLevel=0, baseCount=5, recoil=25, heal=0, accuracy=0.95)
stoneedge = Attack(name='stone edge', attCategory='rock', baseDamage=100, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=0.8)
headsmash = Attack(name='head smash', attCategory='rock', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=20, heal=0, accuracy=1)


# Steel type-----------------------------------
#new
bulletpunch = Attack(name='bullet punch', attCategory='steel', baseDamage=40, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=1)
metalclaw = Attack(name='metal claw', attCategory='steel', baseDamage=50, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=0.95)
magnetbomb = Attack(name='magnet bomb', attCategory='steel', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
mirrorshot = Attack(name='mirror shot', attCategory='steel', baseDamage=65, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.85)
steelwing = Attack(name='steel wing', attCategory='steel', baseDamage=70, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.9)
ironhead = Attack(name='iron head', attCategory='steel', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
flashcannon = Attack(name='flash cannon', attCategory='steel', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)


#modified
irontail = Attack(name='iron tail', attCategory='steel', baseDamage=100, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.75)
meteormash = Attack(name='meteor mash', attCategory='steel', baseDamage=90, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.9)

#not modified
ironpunch = Attack(name='iron punch', attCategory='steel', baseDamage=80, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)


# Ghost type-------------------------------------
#new
shadowsneak = Attack(name='shadow sneak', attCategory='ghost', baseDamage=40, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=0.95)
shadowclaw = Attack(name='shadow claw', attCategory='ghost', baseDamage=70, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
shadowforce = Attack(name='shadow force', attCategory='ghost', baseDamage=120, pokemonLevel=0, baseCount=15, recoil=30, heal=0, accuracy=1)
spectralthief = Attack(name='spectral thief', attCategory='ghost', baseDamage=90, pokemonLevel=0, baseCount=10, recoil=0, heal=40, accuracy=1)

#modified
lick = Attack(name='lick', attCategory='ghost', baseDamage=30, pokemonLevel=0, baseCount=30, recoil=0, heal=0, accuracy=1)
shadowball = Attack(name='shadow ball', attCategory='ghost', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
shadowpunch = Attack(name='shadow punch', attCategory='ghost', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
hide = Attack(name='hide', attCategory='ghost', baseDamage=0, pokemonLevel=0, baseCount=10, recoil=0, heal=40, accuracy=1)

#not modified
curse = Attack(name='curse', attCategory='ghost', baseDamage=90, pokemonLevel=0, baseCount=5, recoil=0, heal=0, accuracy=1)


# Dark type---------------------------------------
#new
snarl = Attack(name='snarl', attCategory='dark', baseDamage=55, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=0.95)
thief = Attack(name='thief', attCategory='dark', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=20, accuracy=1)
nightslash = Attack(name='night slash', attCategory='dark', baseDamage=70, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
darkpulse = Attack(name='dark pulse', attCategory='dark', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)


#Modified
bite = Attack(name='bite', attCategory='dark', baseDamage=60, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=0.95)
feintattack = Attack(name='feint attack', attCategory='dark', baseDamage=60, pokemonLevel=0, baseCount=15, recoil=0, heal=0, accuracy=1)
pursuit = Attack(name='pursuit', attCategory='dark', baseDamage=40, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=1)
crunch = Attack(name='crunch', attCategory='dark', baseDamage=80, pokemonLevel=0, baseCount=15, recoil=0, heal=40, accuracy=0.9)

#not modified
howl = Attack(name='howl', attCategory='dark', baseDamage=0, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.4)

# Psychic type---------------------------------------
#new
primaticlaser = Attack(name='prismatic laser', attCategory='psychic', baseDamage=160, pokemonLevel=0, baseCount=5, recoil=40, heal=0, accuracy=0.9)
psystrike = Attack(name='psystrike', attCategory='psychic', baseDamage=100, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=0.85)
psychic = Attack(name='psychic', attCategory='psychic', baseDamage=90, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)



#modified
psybeam = Attack(name='psybeam', attCategory='psychic', baseDamage=65, pokemonLevel=0, baseCount=20, recoil=0, heal=0, accuracy=0.95)
confusion = Attack(name='confusion', attCategory='psychic', baseDamage=50, pokemonLevel=0, baseCount=25, recoil=0, heal=0, accuracy=1)
dreameater = Attack(name='dream eater', attCategory='psychic', baseDamage=100, pokemonLevel=0, baseCount=10, recoil=10, heal=0, accuracy=0.8)
futuresight = Attack(name='future sight', attCategory='psychic', baseDamage=120, pokemonLevel=0, baseCount=10, recoil=30, heal=0, accuracy=1)
sing = Attack(name='sing', attCategory='psychic', baseDamage=30, pokemonLevel=0, baseCount=20, recoil=0, heal=10, accuracy=1)
psyshock = Attack(name='psyshock', attCategory='psychic', baseDamage=80, pokemonLevel=0, baseCount=10, recoil=0, heal=0, accuracy=1)
heal = Attack(name='heal', attCategory='psychic', baseDamage=0, pokemonLevel=0, baseCount=10, recoil=0, heal=30, accuracy=1)

#not modified
infactuate = Attack(name='infactuate', attCategory='psychic', baseDamage=0, pokemonLevel=0, baseCount=4, recoil=0, heal=0, accuracy=0.5)


# ----------------------------------------------------------------------------------------- #

