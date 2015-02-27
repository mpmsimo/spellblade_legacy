"""
player.py - Default player class

Add player with HP, Attack, and defence.
msimo - 1/7/2015
"""

class Character(object):
	def __init__(self, hp, max_hp, name):
		"""Base character class for players, enemies and NPC's."""
		self.hp = hp
		self.max_hp = max_hp
		self.name = name

class Soulgem(object):
	def __init__(self, level, exp, max_exp):
		"""Contains the level and experience for the soulgem."""
		self.level = level
		self.exp = exp
		self.max_exp = max_exp

class Player(Character):
	def __init__(self, hp, max_hp, name, strength, affinity, dexterity):
		"""Creates the player object, and has the methods which the player can use."""
		self.hp = hp
		self.max_hp = max_hp
		self.name = name

		self.strength = strength
		self.affinity = affinity
		self.dexterity = dexterity

	def print_stats(self):
		"""Prints player statistics."""
		print(("=========================\n"
				"{0} - [{1}/{2} hitpoints]\n"
				"\t* Strength: {3}\n"
				"\t* Affinity: {4}\n"
				"\t* Dexterity: {5}\n" 
				"=========================").format(self.name, self.hp, self.max_hp, \
													self.strength, self.affinity, \
													self.dexterity))

	def equip_weapon(self, weapon):
		weapon_stats = weapon.get_stats()
		self.strength += weapon_stats["strength"]
		self.affinity += weapon_stats["affinity"]
		self.dexterity += weapon_stats["dexterity"]

	def basic_attack(self, weapon):
		physical_damage = self.strength
		print("basic_attack - {0} physical_damage".format(physical_damage))
		return physical_damage

		#Choose attack - Autoattack, skill1, skill2, item
		player_damage = self.damage
		quick_attack_1 = self.attack * .75
		quick_attack_2 = self.attack * .50
		es = self.attack + self.level

		if choice == 1:
			basic_attack()
		elif int(choice) == 2:
			if player_damage <= 0:
				print("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
				print("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
			else:
				enemy.hp -= quick_attack1
				enemy.hp -= quick_attack2
				print("[PLAYER] >> [Quick Attack] deals ({0}) physical \
						damage.".format(quick_attack1))
				print("[PLAYER] >> [Quick Attack] deals ({0}) physical \
						damage.".format(quick_attack2))
		elif int(choice) == 3:
			enemy.hp -= es
			print("[PLAYER] >> [Ethereal Strike] deals ({0}) ethereal \
					 damage.".format(es))
		elif int(choice) == 4:
			print("[PLAYER] >> {0} uses [Random Potion]!".format(self.name))
		elif int(choice) == 5:
			print("Resetting Game")
			#reset()
		else:
			print("Invalid Entry - Please selet an option.")
			Player.attack(self, enemy)
		pass
			
	def sequence(self, enemy):
		Player.checkhp(self)
		if self.alive == False:
			Player.gameover(self)
		else:
			Player.attack(self, enemy)

########## Accessors and Mutators ##########
	def setStats(self, hp, attack, defence):
		self.hp = hp
		self.attack = attack
		self.defence = defence

	def setName(self, name):
		self.name = name

	def setSpec(self, spec):
		self.spec = spec

########## Gold & Experience ##########
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
		print("You are now level {0}! You have gained 3 hp, 1 attack, \
				and 1 defence.\n".format(self.level))

		""" Stats for Acolyte && ez mode level up """
		self.maxhp += 3
		self.hp = self.maxhp
		self.attack += 1
		self.defence += 1
'''
Player.print methods

	def playerStats(self):
		pStats = (" {}, {} - Level {} - Experience: {}/{}\n hp: {}/{} Attack: {} Defence: {}\n Gold: {} \n Rage: {}/{}" % (self.name, self.spec, self.level, self.exp, self.maxExp, self.hp, self.maxhp, self.attack ,self.defence, self.gold)
		return pStats		

class Warrior(Player):
	
	# Warrior Class
	# Resource: Rage
	# Strong melee attacker, can perform Quick Strike and Ethereal Strike 
	
	def __init__(self, hp, attack, defence):
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
		player_damage = self.attack - enemy.defence
		enemy.hp -= player_damage
		if player_damage <= 0:
			print ("Your attack deals no damage.")
		else:
			self.rage += player_damage
			if self.rage > self.maxRage:
				self.rage = self.maxRage
			print ("You attack {} for {} and now have {}/{} rage, it has {} hp remaining." % (enemy.name, player_damage, self.rage, self.maxRage, enemy.hp))
			if self.rage >= self.skill1rr and self.rage >= 10:
				Player.skill1(self, enemy)
			print ""
		pass

	def skill1(self, enemy):
		if enemy.hp >= 1: 
			skill1Damage = self.attack - enemy.defence
			enemy.hp -= skill1Damage
			print ("You perform a {} for {}, {} has {} hp remaining." % (self.skill1, skill1Damage, enemy.name, enemy.hp))
			self.rage -= 10
'''