#!/usr/bin/python
#combat.py - Combat testing, auto combat.
#msimo - 09/06/14
import random, sys, getpass

"""
Player Class

Add player with HP, Attack, and defence.

"""

class Player(object):
	""" __init__(int, int, int)__
		attack - Base player damage
		health - Base player health
		maxHealth - Base player maximum health
		defence - Base player defence

		level - Player level
		xp - Player experience
		class - Player's class.

		name - Player's Character name.
		alive - Is the character alive?

		gold - Total gold of player.
		saveFileName - The name of the savefile for this character."""
	def __init__(self, health, attack, defence):
		#base stats
		self.attack = attack
		self.health = health
		self.maxHealth = health
		self.defence = defence
		
		#level
		self.level = 1
		self.exp = 0
		self.maxExp =  50
		self.spec = "Spellblade"

		#rage - skills
		self.rage = 0
		self.maxRage = 10 * self.level
		#Quick Strike - Player attacks an additional time.
		self.skill1 = "Quick Strike" 
		self.skill1rr = 10
		#Ethereal Strike - Player performs an attack 250% damage.
		self.skill2 = "Ethereal Strike"
		self.skill2rr = 20

		#char attr
		self.name = ""
		self.alive = True

		#inventory
		self.gold = 0

		#savefile
		self.saveFileName = ("%s.txt" % (self.name))

	def __str__(self):
		pStats = (" %s, %s - Level %d - Experience: %d/%d\n Health: %d/%d Attack: %d Defence: %d\n Gold: %d \n Rage: %s/%s\n" % (self.name, self.spec, self.level, self.exp, self.maxExp, self.health, self.maxHealth, self.attack ,self.defence, self.gold, self.rage, self.maxRage))
		return pStats

	def checkHealth(self):
		if self.health <= 0:
			self.alive = False
		else:
			pass

	def attack(self, enemy):
		print (" %s, %s - Level %d\n Health: %d/%d\n Attack: %d\n Defence: %d\n Rage: %s/%s" % (self.name, self.spec, self.level, self.health, self.maxHealth, self.attack ,self.defence, self.rage, self.maxRage))
		print ""
		print "Please select an attack.\n1. Basic Attack\n2. %s\n3. %s\n4. Items\n" % (self.skill1, self.skill2)
		
		try:		
			choice = raw_input("CHOICE >> ")
		except ValueError:
			print "%s is not an integer!" % choice
			print "Forgive me, but you have not entered a valid integer option..."
			print "Closing game, sorry bro"

		print ""
		
		#Choose attack - Autoattack, skill1, skill2, item
		pDamage = self.attack - enemy.defence
		qa1 = self.attack * .75
		qa2 = self.attack * .50
		es = self.attack + self.level

		if choice == 1:
			if pDamage <= 0:
				print ("[PLAYER] >> [Basic Attack] deals 0 physical damage.")
			else:
				enemy.health -= pDamage
				print ("[PLAYER] >> [Basic Attack] deals (%d) physical damage." % (pDamage))
		elif int(choice) == 2:
			if pDamage <= 0:
				print ("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
				print ("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
			else:
				enemy.health -= qa1
				enemy.health -= qa2
				print ("[PLAYER] >> [Quick Attack] deals (%d) physical damage." % (qa1))
				print ("[PLAYER] >> [Quick Attack] deals (%d) physical damage." % (qa2))
		elif int(choice) == 3:
			enemy.health -= es
			print ("[PLAYER] >> [Ethereal Strike] deals (%d) ethereal damage." % (es))
		elif int(choice) == 4:
			print "[PLAYER] >> %s uses [Random Potion]!" % self.name
		elif int(choice) == 5:
			print "Resetting Game"
			reset()
		else:
			print "Invalid Entry - Please selet an option."
			Player.attack(self, enemy)
		pass

			
	def gameover(self):
		if self.alive == False:
			print("No! I have lost!")
			sys.exit(0)

	def sequence(self, enemy):
		Player.checkHealth(self)
		if self.alive == False:
			Player.gameover(self)
		else:
			Player.attack(self, enemy)


		if pDamage <= 0:
			print ("[PLAYER] >> [Basic Attack] deals 0 physical damage.")
		else:
			print ("[PLAYER] >> [Basic Attack] deals (%d) physical damage." % (pDamage))
		pass
		
	def gameover(self):
		if self.alive == False:
			print("No! I have lost!")
			sys.exit(0)

	def sequence(self, enemy):
		Player.checkHealth(self)
		if self.alive == False:
			Player.gameover(self)
		else:
			Player.attack(self, enemy)
###
# Accessors and Mutators
###
	def setStats(self, health, attack, defence):
		self.health = health
		self.attack = attack
		self.defence = defence

	def setName(self, name):
		self.name = name

	def setSpec(self, spec):
		self.spec = spec

	#def setMainHand(self, mainHand)

###
# Gold & Experience
###
	def calculateExp(self, exp):
		totalExp = exp + self.exp
		if totalExp >= self.maxExp:
			diffExp = abs(totalExp - self.maxExp)
			Player.levelUp(self)
			self.maxExp =  50 * self.level
			if diffExp >= self.maxExp:
				remainingExp = abs(diffExp - self.maxExp)
				Player.levelUp(self)
				Player.calculateExp(self, remainingExp)
			self.exp = diffExp
		else:
			self.exp = self.exp + exp

	def levelUp(self):
		self.level += 1
		print ("You are now level %d! You have gained 3 health, 1 attack, and 1 defence.\n" % (self.level))

		""" Stats for Acolyte && ez mode level up """
		self.maxHealth += 3
		self.health = self.maxHealth
		self.attack += 1
		self.defence += 1

"""
Player.print methods

	def playerStats(self):
		pStats = (" %s, %s - Level %d - Experience: %d/%d\n Health: %d/%d Attack: %d Defence: %d\n Gold: %d \n Rage: %s/%s" % (self.name, self.spec, self.level, self.exp, self.maxExp, self.health, self.maxHealth, self.attack ,self.defence, self.gold)
		return pStats		

class Warrior(Player):
	
	# Warrior Class
	# Resource: Rage
	# Strong melee attacker, can perform Quick Strike and Ethereal Strike 
	
	def __init__(self, health, attack, defence):
		#level
		self.level = 1
		self.xp = 0
		
		#rage - skills
		self.rage = 0
		self.maxRage = 10 * self.level

		#Quick Strike - Player attacks an additional time.
		self.skill1 = "Quick Strike" 
		self.skill1rr = 10

		#Ethereal Strike - Player performs an attack 250% damage.
		self.skill2 = "Ethereal Strike"
		self.skill2rr = 20
	
	def attack(self, enemy):
		pDamage = self.attack - enemy.defence
		enemy.health -= pDamage
		if pDamage <= 0:
			print ("Your attack deals no damage.")
		else:
			self.rage += pDamage
			if self.rage > self.maxRage:
				self.rage = self.maxRage
			print ("You attack %s for %d and now have %d/%d rage, it has %d hp remaining." % (enemy.name, pDamage, self.rage, self.maxRage, enemy.health))
			if self.rage >= self.skill1rr and self.rage >= 10:
				Player.skill1(self, enemy)
			print ""
		pass

	def skill1(self, enemy):
		if enemy.health >= 1: 
			skill1Damage = self.attack - enemy.defence
			enemy.health -= skill1Damage
			print ("You perform a %s for %d, %s has %d hp remaining." % (self.skill1, skill1Damage, enemy.name, enemy.health))
			self.rage -= 10
"""

#Add monsters with HP, Attack, and defence.
class Enemy(object):
	""" __init__(string, int, int, int, int) 
		name - Level of the enemy.
		attack - Attack of the enemy.
		health - Health of the enemy.
		defence - Defence of the enemy.

		alive - Is the enemy alive?"""
	def __init__(self, name, level, health, attack, defence):
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence
		self.level = level
		self.alive = True

	def __str__(self):
		#pStats = ("%s Stats\n Level %s\n Health: %d\n Attack: %d\n defence: %d" % (self.name, self.level, self.health, self.attack ,self.defence))
		pStats = (" Level %s\n Health: %d\n Attack: %d\n Defence: %d" % (self.level, self.health, self.attack ,self.defence))
		return pStats

	def checkHealth(self):
		if self.health <= 0:
			self.alive = False
			#overkill = self.health
		else:
			pass

	def attack(self, hero):
		eDamage = self.attack - hero.defence
		hero.health -= eDamage
		if eDamage <= 0:
			print ("[ENEMY]  >> %s's attack has no effect." % (self.name))
		else:
			print ("[ENEMY]  >> %s's attack hits you for %d." % (self.name, eDamage))
			pass
			
	def sequence(self, hero):
		Enemy.checkHealth(self)
		if self.alive == False:
			pass
		else:
			Enemy.attack(self, hero)

	def setStats(self, name, level, health, attack, defence):
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence
		self.level = level

	def setAlive(self, value):
		if value == True:
			self.alive = True
		else:
			print ("You have used setAlive() wrongly.")

#Get that loot!
def loot(hero, enemy):
	if enemy.alive == False:
		#xp = enemy.level*randint(1,2)
		exp = enemy.level * 10
		#gold = enemy.level*randint(3,6)
		gold = enemy.level*3 
		hero.calculateExp(exp)
		hero.gold += gold
		print ""
		print ("You have gained %d exp and looted %d gold from %s" % (exp, gold, enemy.name))
		print ""
	else:
		pass

#fight enemy
def fightEnemy():
	print ("You have encountered %s." % (enemy.name))
	while hero.alive == True and enemy.alive == True:
		Player.sequence(hero, enemy)
		Enemy.sequence(enemy, hero)
	loot(hero, enemy)
	#battle += 1

#reset
def reset():
	hero = Player(30,3,3)
	hero.level = 1
	hero.exp = 0
	hero.maxExp =  50
	hero.spec = "Spellblade"
	hero.rage = 0
	hero.maxRage = 10 * hero.level
	hero.skill1 = "Quick Strike" 
	hero.skill1rr = 10
	hero.skill2 = "Ethereal Strike"
	hero.skill2rr = 20
	hero.name = ""
	print "DEBUG >> %s" % hero.name
	hero.alive = True
	hero.gold = 0
	createChar(hero)

#Print total combat stats (kills, total damage dealt, total damage taken, absorbed damage?)

###
# Character Creation
###
def createChar(hero):
	count = 1
	specList = ["Acolyte", "Warrior", "Ranger", "Herald"]
	
	name = raw_input('Character name: ')
	hero.setName(name)
	print ""
	print("Select a specialization.\n")

	for x in specList:
		print ("%d. %s" % (count, specList[count-1]))
		count += 1
	
	print ""
	choice = raw_input("CHOICE >> ")
	print ""
	
	#Choose class - class(hp, attack, defence)
	if int(choice) == 1:
		hero.setStats(15, 4, 0)
		hero.setSpec("Acolyte")
	elif int(choice) == 2:
		hero.setStats(20, 2, 2)
		hero.setSpec("Warrior")
	elif int(choice) == 3:
		hero.setStats(15, 3, 1)
		hero.setSpec("Ranger")
	elif int(choice) == 4:
		hero.setStats(27, 1, 1)
		hero.setSpec("Herald")
	else:
		print "Error: createChar"

###
# Enemy Creation
# name, level, health, attack, defence
###

def selectMonster(enemy):
	enemyList = []
	enemyList.append((Enemy("Training Dummy", 1, 20, 0, 0)))
	enemyList.append(Enemy("Rat", 1, 4, 2, 0))
	enemyList.append(Enemy("Goblin", 2, 6, 3, 1))
	enemyList.append(Enemy("Skeleton", 3, 10, 3, 1))
	enemyList.append(Enemy("Black Goblin", 4, 12, 4, 0))
	enemyNum = random.randint(0, len(enemyList)-1)
	randEnemy = Enemy(name=enemyList[enemyNum].name, level=enemyList[enemyNum].level, health=enemyList[enemyNum].health, attack=enemyList[enemyNum].attack, defence=enemyList[enemyNum].defence)

	enemy.setStats(randEnemy.name, randEnemy.level, randEnemy.health, randEnemy.attack, randEnemy.defence)
	enemy.setAlive(True)
	
def safeFight(hero, enemy):
	selectMonster(enemy)
	while hero.level < enemy.level:
		selectMonster(enemy)
	fightEnemy()

def randomFight(hero, enemy):
	selectMonster(enemy)
	fightEnemy()

def arenaFight(hero, enemy, rounds):
	roundCount = rounds
	x = 1

	while x <= roundCount:
		print "==================\n"
		print "=====Round %d=====\n" % x
		print "==================\n"
		print hero
		randomFight(hero, enemy)
		x += 1
	if (hero.alive == True) and (x > roundCount):
		exp = 100 + (roundCount * 50) 
		gold = roundCount * 100
		print ("You have completed %d rounds of the the Arena!" % (roundCount))
		print ("You are rewarded %d exp and %d gold, well done!" % (exp, gold))
		hero.calculateExp(exp)
		hero.gold += gold
	else: 
		"You have died in the arena, rip in pepperoni m8."


"""
enemyNum = random.randint(0, len(enemyList)-1)
enemy = Enemy(name=enemyList[enemyNum].name, level=enemyList[enemyNum].level, health=enemyList[enemyNum].health, attack=enemyList[enemyNum].attack, defence=enemyList[enemyNum].defence)
print ("You have encountered %s." % (enemyList[enemyNum].name))
print enemy
print "

"""
###
# Play Game
###
#1v1 combat until player or enemy death
hero = Player(30,3,3)
enemy = Enemy("Wanderer", 1, 1, 1, 1)
createChar(hero)


#################
## TESTING
#################
arenaFight(hero, enemy, 10)
