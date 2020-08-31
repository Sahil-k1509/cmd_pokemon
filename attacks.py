from random import random, seed, randint
from math import floor

def pprint(*args, **kwargs):
    print('\t', *args, **kwargs)
    

class Attack(object):
    __slots__ = 'name', 'attCategory', 'pLevel', 'recoil', 'heal', 'damage', 'baseDamage', 'accuracy', 'count', 'increasable'
    
    def __init__(self, name, attCategory, baseDamage, pokemonLevel, baseCount, increasable=1,recoil=0, heal=0, accuracy=1, *args, **kwargs):
        self.name = name
        self.attCategory = attCategory
        self.pLevel = pokemonLevel
        self.baseDamage = baseDamage
        self.recoil = - recoil
        self.count = baseCount
        self.heal = heal
        self.increasable = increasable
        self.accuracy = accuracy
        self.damage = self.calcDamage()
        
    def updateAttack(self, newLevel, newRecoil=0, newHeal=0, baseDamage=-1):
        self.pLevel = newLevel
        self.recoil = - (newRecoil*self.pLevel + self.recoil)
        self.heal = newHeal*self.pLevel + self.heal
        self.count = self.count + self.pLevel//randint(1, floor(self.pLevel)+1)*self.increasable
        self.damage = self.calcDamage(baseDamage)
        
    def calcDamage(self, baseDamage=-1):
        if baseDamage == -1:
            return floor(self.baseDamage + 5*(self.pLevel/2 + (1 - random())/3)**(1.2))
        else:
            return floor(baseDamage + 5*(self.pLevel/2 + (1 - random())/3)**(1.2))

    def printAttack(self):
        pprint('|-----------------------------------------------------------------------------------------')
        pprint(f"| Attack: {self.name:15} | Type:   {self.attCategory:10} | Damage: {self.damage:5} | Count: {self.count:3}")
        pprint(f"| Heal:   {self.heal:15} | Recoil: {self.recoil:10} | Accuracy: {self.accuracy}")
        pprint('|-----------------------------------------------------------------------------------------')
        
        
# a = Attack('pe', 'c', 5, 0, 9)
# for i in range(100):
#     a.updateAttack(i)
#     pprint(a.damage)