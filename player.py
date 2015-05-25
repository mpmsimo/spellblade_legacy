"""
player.py - Default player class

Author: mpmsimo
Created: 1/7/2015

A player object with HP, name, level, exp, and basic stats.
"""

class Player(object):
    def __init__(self, max_hp, name, level, exp, max_exp, strength, dexterity, intelligence):
        """Creates the player object, and has the methods which the player can use."""
        self.max_hp = max_hp
        self.hp = max_hp
        self.name = name
        self.level = level
        self.exp = exp
        self.max_exp = max_exp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def print_stats(self):
        """Prints player statistics."""
        print(("\n========================\n"
            "{0}, Level {1}\n"
            "XP: [{2}/{3}]\n"
            "HP: [{4}/{5}]\n"
            "\t* Strength: {6}\n"
            "\t* Dexterity: {7}\n"
            "\t* Intelligence: {8}\n"
            "=========================").format(self.name, self.level, self.exp, \
                                                    self.max_exp, self.hp, self.max_hp, self.strength, \
                                                    self.dexterity, self.intelligence))

    def equip_weapon(self, weapon):
        """Equips a weapon gaining the statistics from the spellgems"""
        weapon_stats = weapon.get_stats()
        self.strength += weapon_stats["strength"]
        self.intelligence += weapon_stats["intelligence"]
        self.dexterity += weapon_stats["dexterity"]

    def basic_attack(self, weapon):
        """Returns and prints amount of damage a basic attak does"""
        physical_damage = self.strength
        print("basic_attack - {0} physical_damage".format(physical_damage))
        return physical_damage

'''
	def check_hp(self):
		#print("check_hp - before:  {0}/{1}".format(self.hp, self.max_hp))
		if self.hp > self.max_hp:
			#print("check_hp - cur greater than max_hp: {0}/{1}".format(self.hp, self.max_hp))
			self.hp = self.max_hp
			#print("check_hp - after:  {0}/{1}".format(self.hp, self.max_hp))		
		elif self.hp <= 0:
			#print("check_hp - dead hp: {0}/{1}".format(self.hp, self.max_hp))
			self.is_alive = False
			#print("is_alive: {0}!".format(self.is_alive))
		else:
            pass
			#print("check_hp - Valid: {0}/{1}".format(self.hp, self.max_hp))
		
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