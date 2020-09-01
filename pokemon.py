from math import sqrt, floor, log10
from random import randint, shuffle, choice, random
from time import sleep
from pokemonStrengthChart import typeAdantages, typeDisadantages
from pokeworld import pokemonWorld


def pprint(*args, **kwargs):
    print('\t\t', *args, **kwargs)


class Pokemon(object):
	__slots__ = 'name', 'categories', 'level', 'health', 'maxHealth', 'experience', 'nextLevelAt', 'attacks', 'learnableAttacks', 'defence', 'speed', 'evolveAt', 'evolveTo', 'newAttackAt'
	experienceChart = [0] + [5 + 2 * (i + 1) ** 2 for i in range(100)]
	learningCheckpoints = [2, 7, 10, 15, 18, 23, 30, 39, 46, 55, 60, 64, 67, 72, 78, 89, 95, 100]

	def __init__(self, name, pokedata, level=0, *args, **kwargs):
		self.name = name
		self.newAttackAt = 0
		self.categories = pokedata['type']
		self.level = level
		self.maxHealth = 15 + floor(log10(self.level * 23 + 1) * self.level ** 1.7)
		self.health = self.maxHealth
		self.defence = pokedata['baseDef']
		self.speed = pokedata['baseSpeed']
		self.evolveAt = pokedata['evolveAt']
		self.evolveTo = pokedata['evolveTo']
		self.experience = 0
		self.nextLevelAt = self.experienceChart[self.level + 1]
		self.attacks = pokedata['startAttacks']
		self.learnableAttacks = pokedata['learnableAttacks']

	def updateLevel(self, playertype=None):
		self.level += 1
		self.maxHealth = 15 + floor(log10(self.level * 23 + 1) * self.level ** 1.7)
		self.defence += randint(0, 5)
		self.speed += randint(0, 5)
		self.experience = self.experience - self.nextLevelAt
		self.nextLevelAt = self.experienceChart[self.level + 1] if self.level < 100 else None
  
		if playertype is None:
			pprint(f"{self.name} levelled up...\n"); sleep(1.8)
			pprint(f"Current level: {self.level}"); sleep(1.8)
			pprint(f"Max Health increased by {self.maxHealth}"); sleep(1.8)
			pprint(f"Defence increased to {self.defence}"); sleep(1.8)
			pprint(f"Speed increased to {self.speed}\n"); sleep(1.8)

    
    
		if self.evolveAt is not None:
			if self.level >= self.evolveAt:
				self.evolvePokemon()

		if len(self.learnableAttacks) != 0:
			if self.level >= self.learningCheckpoints[self.newAttackAt]:
				self.newAttackAt += 1
				self.learnNewAttack(playertype)

		for attack in self.attacks:
			if attack is not None:
				if attack.heal == 0 and attack.recoil == 0:
					attack.updateAttack(self.level)
				if attack.heal != 0:
					attack.updateAttack(self.level, newHeal=5)
				if attack.recoil != 0:
					attack.updateAttack(self.level, newRecoil=5)


	def learnNewAttack(self, playertype=None):
		sleep(1.5)
		attackToLearn = self.learnableAttacks.pop()

		if not all(self.attacks):
			if playertype is None:
				pprint(f"{self.name} learnt {attackToLearn.name}"); sleep(1)
			indNone = self.attacks.index(None)
			self.attacks[indNone] = attackToLearn
		else:
			if playertype is None:
				pprint(self.name, 'wants to learn', attackToLearn.name, end='\n')
				sleep(1)
				pprint('CURRENT ATTACKS: '); sleep(1)
				i=0
				for attack in self.attacks:
					pprint(f"{i+1}) {attack.name}")
					i+=1
					sleep(1.5)
				pprint()
				pprint("New Attack Stats: \n")
				attackToLearn.printAttack()
				pprint()
				sleep(1.5)
				discard = input('\t\tWhich attack would you like to replace?\n\t\t(Choose 1, 2, 3, 4. Any other choice will result in not learning the attack): ')
				if discard in ['1', '2', '3', '4']:
					self.attacks[int(discard)-1] = attackToLearn
			else:
				idiscard = randint(0, len(self.attacks)-1)
				self.attacks[idiscard] = attackToLearn


	def evolvePokemon(self, playertype=None):
		if self.name == 'nidoran':
			dice = random()
			self.evolveTo = 'nidorino' if dice >= 0.4 else 'nidorina'
      
		evolveform = pokemonWorld[self.evolveTo]

		if playertype is None:
			sleep(1.5)
			pprint("\nWhat is happening !!!!\n")
			sleep(1.5)
			pprint(self.name, 'is evolving....\n')
			sleep(1)
			pprint(self.name, 'has evolved into', self.evolveTo)
			sleep(1.5)
			pprint()

		self.name = self.evolveTo
		self.evolveTo = evolveform['evolveTo']
		self.evolveAt = evolveform['evolveAt']
		self.categories = evolveform['type']
		self.defence += randint(10, 15)
		self.speed += randint(8, 15)

		if evolveform.get('learnableAttacks', None) is not None:
			self.learnableAttacks = evolveform['learnableAttacks'] + self.learnableAttacks


	def attack(self, enemyPokemon, attackUsedInd):
		attackUsed = self.attacks[attackUsedInd]
		pprint(f"\n{self.name} used {attackUsed.name}\n")
		sleep(1.5)
		attackType = attackUsed.attCategory
		enemyType = enemyPokemon.categories

		chanceToMiss = random()

		if chanceToMiss < attackUsed.accuracy:

			if attackUsed.name != 'Heal':
				criticalChance = random()
				initialHealth = enemyPokemon.health

				if criticalChance >= 0.92:
					pprint("Critical Hit...")
					sleep(1.5)
					enemyPokemon.health -= (0.3+random()*0.2)*attackUsed.damage

				if enemyType in typeAdantages[attackType]:
					pprint("It's Super Effective !!\n")
					sleep(1.5)
					enemyPokemon.health -= (0.4+random()*0.4)*attackUsed.damage

				elif enemyType in typeDisadantages[attackType]:
					pprint("It's not very effective !!\n")
					sleep(1.5)
					enemyPokemon.health += (0.2+random()*0.3)*attackUsed.damage

				enemyPokemon.health -= attackUsed.damage
				enemyPokemon.health = max(0, enemyPokemon.health)
				pprint(f"Health reduced by {initialHealth - enemyPokemon.health}\n")

				if attackUsed.recoil != 0:
					sleep(1.5)
					pprint(f"{self.name} got a recoil of {-attackUsed.recoil}")
					self.health += attackUsed.recoil
					self.health = max(0, self.health)

			else:
				self.health = min(self.maxHealth, self.health + attackUsed.heal)

		else:
			pprint(f"{self.name} missed...\n")

		self.attacks[attackUsedInd].count -= 1


	def printPokemon(self):
		pprint(f"Name: {self.name}\tLevel: {self.level}\tHP: {self.health}/{self.maxHealth}")
	
	
	def displayStats(self, trainer="player's"):
		if trainer == "player's":
			pprint(f"+---------------------------------------------+"); sleep(1.5)
			pprint(f"{trainer} {self.name}"); sleep(1.5)
			pprint(f"PokemonType: {self.categories}  Level: {self.level}"); sleep(1.5)
			pprint(f"Health: {self.health}  MaxHealth: {self.maxHealth}"); sleep(1.5)
			pprint(f"Defense: {self.defence}  Speed: {self.speed}"); sleep(1.5)
			pprint(f"Experience: {self.experience}/{self.nextLevelAt}"); sleep(1.5)
			pprint(f"Attacks: "); sleep(1.5)
			i=0
			for attack in self.attacks:
				if attack != None:
					pprint(f"{i+1}) {attack.name:20} :  {attack.count} left")
				else:
					pprint(f"{i+1}) {attack}")
				i+=1
				sleep(1.5)
			pprint(f"+---------------------------------------------+")
   
		else:
			pprint(f"+---------------------------------------------+")
			pprint(f"{trainer} {self.name}"); sleep(1.5)
			pprint(f"PokemonType: {self.categories}  Level: {self.level}"); sleep(1.5)
			pprint(f"Health: {self.health}  MaxHealth: {self.maxHealth}"); sleep(1.5)
			pprint(f"+---------------------------------------------+")
	
	
	def gain_exp(self, enemyPok, battletype='wild'):
		enemyType = enemyPok.categories
		multiplier = 1
  
		ExpIncrease = 3*(self.level*2 + 1)
  
		if enemyType in typeAdantages[self.categories]:
			multiplier = 0.4 + random()*0.5
		elif enemyType in typeDisadantages[self.categories]:
			multiplier = 1.3 + random()*0.7
   
		if battletype == 'gym': multiplier += 4
		elif battletype == 'duel': multiplier += 2
   
		enemylvl = enemyPok.level
		if enemylvl >= self.level:
			ExpIncrease += 6*(enemylvl-self.level)**2.8
		else:
			ExpIncrease -= 5*(self.level-enemylvl)**1.75
   
		ExpIncrease = max(7, ExpIncrease)*multiplier
	
		pprint(f"{self.name}'s Experience increased by {ExpIncrease}")
		self.experience += ExpIncrease
		# pprint(f"{self.experience} <- Total exp\n")
		sleep(0.8)
		if self.experience > self.nextLevelAt:
			self.updateLevel()
			

	def visitPokemonCentre(self):
		self.health = self.maxHealth
		for attack in self.attacks:
			attack.count = attack.maxcount

 
	# def npcPokemonReady(self):
	# 	self.updateLevel(playertype='npc')
	# 	self.updateLevel(playertype='npc')
 

# for i in range(100):
#     p = Pokemon('jabba', pokemonWorld['pikachu'], i)
#     pprint(p.maxHealth)
# p = Pokemon('jabba', pokemonWorld['pikachu'], 0)
# pprint(p.experienceChart)

# for i in range(3,20):
# 	for j in range(3,20):
# 		p1 = Pokemon('jabba', pokemonWorld['charmander'], i)
# 		p2 = Pokemon('dabba', pokemonWorld['charmander'], j)
# 		pprint(f"p1 lvl: {i} | p2 lvl: {j}", end=' ')
# 		p1.gain_exp(p2)	