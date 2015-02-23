#!/usr/bin/env python
#combat.py - Combat testing, auto combat.

import random

#Add player with HP, Attack, and Defense.
class Player(object):
	""" Our hero """
	def __init__(self, ha= health
		self.attack = attack
		self.defense = defense
		self.alive = True
		self.level = 1
		self.xp = 0
		self.gold = 0

	def __str__(self):
		pStats = ("Hero Stats\n Level %d - Experience: %d\n Health: %d Attack: %d Defense: %d\n Gold: %d " % (self.level, self.xp, self.health, self.attack ,self.defense, self.gold))
		return pStats
	def checkHealth(self, enemy):
		if self.health <= 0:
			self.alive = False
		elif(enemy.health <= 0):
			enemy.alive = False
			loot(self, enemy)
		else:
			passa

	def attack(self, enemy):
		pDamage = self.attack - enemy.defense
		enemy.health -= apDamage
		if pDamage <= 0:a
			print ("a
			print ("You attack %s for %d, it has %d hp remaining." % (enemy.name, pDamage, enemy.health))
		pass
a
	def gameover(self):
		if self.alive == False:
			print("No! I have lost!")

	def sequence(self, enemy):
		Player.checkHealth(self, enemy)
		if self.alive == False:
			Player.gameover(self)
		else:
			Player.attack(self, enemy)

#Add monsters with HP, Attack, and Defense.
class Enemy(object):
	""" An enemy """
	def __init__(self, name, level, health, attack, defense):
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense
		self.level = level
		self.alive = True

	def __str__(self):
		pStats = ("%s Stats\n Level %s\n Health: %d\n Attack: %d\n Defense: %d" % (self.name, self.level, self.health, self.attack ,self.defense))
		return pStats

	def checkHealth(self):
		if self.health <= 0:
			self.alive = False
		pass

	def attack(self, hero):
		eDamage = self.attack - hero.defense
		hero.health -= eDamage
		if eDamage <= 0:
			print ("%s's attack has no effect." % (self.name))
		else:
			print ("%s's attack hits you for %d." % (self.name, eDamage))
			pass

def loot(hero, enemy):
	if enemy.alive == False:
		xp = enemy.level*randint(1,2)
		gold = enemy.level*randint(3,6)
		hero.xp += xp
		hero.gold += gold
		print ("You have gained %d exp and looted %d gold from %s" % (xp, gold, enemy.name))
	else:
		pass

def randEnemy():
	randEnemy = random.choice(enemyList)
	enemy = Enemy(randEnemy.name, randEnemy.level, randEnemy.health, randEnemy.attack, randEnemy.defense)
	enemy.alive = True
	print ("You encounter a %s!" % (enemy.name))
	print enemy
	return enemy

#Print stats (kills, total damage dealt, total damage taken, absorbed damage?)

#Get gold based on stats. Buy new gear?

###
# Instantiate variables
###
hero = Player(health=10, attack=2, defense=2)
round = 1

###
# Instantiate enemies
###
rat = Enemy(name="Rat", level=1, health=4, attack=2, defense=0)
goblin = Enemy(name="Goblin", level=2, health=6, attack=3, defense=1)
skeleton = Enemy(name="Skeleton", level=3, health=10, attack=3, defense=1)
blackGoblin = Enemy(name="Black Goblin", level=4, health=12, attack=4, defense=2)

enemyList = (rat, goblin, skeleton, blackGoblin)

###
# Play Game
###

#1v1 combat until player or enemy death.
randEnemy()

while hero.alive == True and enemy.alive == True:
	print enemy
	print ("\nRound %d" % (round))
	print(hero)
	Player.sequence(hero, enemy)
	Enemy.attack(enemy, hero)
	round += 1
round = 1
