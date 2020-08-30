from math import sqrt, floor, log10
from random import randint, shuffle, choice, random
from time import sleep
from pokemonStrengthChart import typeAdantages, typeDisadantages
from pokeworld import pokemonWorld


class Pokemon(object):
	__slots__ = 'name', 'categories', 'level', 'health', 'maxHealth', 'experience', 'nextLevelAt', 'attacks', 'learnableAttacks', 'defence', 'speed', 'evolveAt', 'evolveTo', 'newAttackAt'
	experienceChart = [0] + [5 + 2 * (i + 1) ** 2 for i in range(100)]
	learningCheckpoints = [2, 7, 15, 15, 23, 30, 39, 46, 55, 60, 64, 67, 72, 78, 89, 95, 100]

	def __init__(self, name, pokedata, level=0, *args, **kwargs):
		self.name = name
		self.newAttackAt = 0
		self.categories = pokedata['type']
		self.level = level
		self.maxHealth = 10 + floor(log10(self.level * 14 + 1) * self.level ** 1.5)
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
		self.maxHealth = 10 + floor(log10(self.level * 14 + 1) * self.level ** 1.5)
		self.defence += randint(0, 5)
		self.speed += randint(0, 5)
		self.experience = self.experience - self.nextLevelAt
		self.nextLevelAt = self.experienceChart[self.level + 1] if self.level < 100 else None

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
		sleep(0.5)
		attackToLearn = self.learnableAttacks.pop()

		if not all(self.attacks):
			if playertype is None:
				print(f"{self.name} learnt {attackToLearn.name}")
			indNone = self.attacks.index(None)
			self.attacks[indNone] = attackToLearn
		else:
			if playertype is None:
				print(self.name, 'wants to learn', attackToLearn.name, end='\n')
				sleep(1)
				print('CURRENT ATTACKS: ')
				i=0
				for attack in self.attacks:
					print(f"{i+1}) {attack.name}")
					i+=1
					sleep(0.5)
				print("\nNew Attack Stats: \n")
				attackToLearn.printAttack()
				print()
				sleep(0.5)
				discard = input('Which attack would you like to replace?\n(Choose 1, 2, 3, 4. Any other choice will result in not learning the attack): ')
				if discard in ['1', '2', '3', '4']:
					self.attacks[int(discard)-1] = attackToLearn
			else:
				idiscard = randint(0, 3)
				self.attacks[idiscard] = attackToLearn


	def evolvePokemon(self, playertype=None):
		evolveform = pokemonWorld[self.evolveTo]

		if playertype is None:
			sleep(0.5)
			print("\nWhat is happening !!!!\n")
			sleep(0.5)
			print(self.name, 'is evolving....\n')
			sleep(1)
			print(self.name, 'has evolved into', self.evolveTo)
			sleep(0.5)
			print()

		self.name = self.evolveTo
		self.evolveTo = evolveform['evolveTo']
		self.evolveAt = evolveform['evolveAt']
		self.categories = evolveform['type']
		self.defence += randint(10, 15)
		self.speed += randint(8, 15)

		if evolveform.get('learnableAttacks', None) is not None:
			self.learnableAttacks = evolveform['learnableAttacks'] + self.learnableAttacks


	def attack(self, enemyPokemon, attackUsed):
		print(f"\n{self.name} used {attackUsed.name}\n")
		sleep(0.5)
		attackType = attackUsed.attCategory
		enemyType = enemyPokemon.categories

		chanceToMiss = random()

		if chanceToMiss < attackUsed.accuracy:

			if attackUsed.name != 'Heal':
				criticalChance = random()
				initialHealth = enemyPokemon.health

				if criticalChance >= 0.92:
					print("Critical Hit...")
					sleep(0.5)
					enemyPokemon.health -= (0.3+random()*0.2)*attackUsed.damage

				if enemyType in typeAdantages[attackType]:
					print("It's Super Effective !!\n")
					sleep(0.5)
					enemyPokemon.health -= (0.4+random()*0.4)*attackUsed.damage

				elif enemyType in typeDisadantages[attackType]:
					print("It's not very effective !!\n")
					sleep(0.5)
					enemyPokemon.health += (0.2+random()*0.3)*attackUsed.damage

				enemyPokemon.health -= attackUsed.damage
				enemyPokemon.health = max(0, enemyPokemon.health)
				print(f"Health reduced by {initialHealth - enemyPokemon.health}\n")

				if attackUsed.recoil != 0:
					sleep(0.5)
					print(f"{self.name} got a recoil of {-attackUsed.recoil}")
					self.health += attackUsed.recoil

			else:
				self.health = min(self.maxHealth, self.health + attackUsed.heal)

		else:
			print(f"{self.name} missed...\n")

		attackUsed.count -= 1

	def printPokemon(self):
		print(f"Name: {self.name}\tLevel: {self.level}\tHP: {self.health}/{self.maxHealth}")
	
 
	# def npcPokemonReady(self):
	# 	self.updateLevel(playertype='npc')
	# 	self.updateLevel(playertype='npc')
 

# for i in range(100):
#     p = Pokemon('jabba', pokemonWorld['pikachu'], i)
#     print(p.maxHealth)