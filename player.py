"""
player.py - Default player class

Add player with HP, Attack, and defence.
msimo - 1/7/2015
"""

class Player(object):
	""" __init__(int, int, int)__
		hp - Base player hp
		max_hp - Base player maximum hp
		attack - Base player damage
		affinity - Base player affinity

		level - Player level
		exp - Player experience
		level_exp - Max exp for player level (Maybe should be in the leveling function)
		
		name - Player's Character name.
		class - Player's class.

		is_alive - Is the character alive?
	"""
	def __init__(self, hp, max_hp, strength, affinity, precision, level, exp, max_exp, name, is_alive):
		#base stats
		self.hp = hp
		self.max_hp = max_hp

		self.strength = strength
		self.affinity = affinity
		self.precision = precision
		
		#level
		self.level = level
		self.exp = exp
		self.max_exp = max_exp
		

		#player info
		self.name = name
		self.is_alive = is_alive

	def print_stats(self):
		"""Prints player statistics."""
		player_stats = (("""{0} || Level: {1} || Experience: {2}/{3}
Health: {4}/{5} || Strength: {6} || Affinity: {7} || Precision: {8}
is_alive: {9}!""").format(self.name, self.level, self.exp, self.max_exp, self.hp, self.max_hp, self.strength ,self.affinity, self.precision, self.is_alive))
		print(player_stats)

	def check_hp(self):
		print("check_hp - before:  %s/%s" % (self.hp, self.max_hp))
		if self.hp > self.max_hp:
			print("check_hp - cur greater than max_hp: %s/%s" % (self.hp, self.max_hp))
			self.hp = self.max_hp
			print("check_hp - after:  %s/%s" % (self.hp, self.max_hp))		
		elif self.hp <= 0:
			print("check_hp - dead hp: %s/%s" % (self.hp, self.max_hp))
			self.is_alive = False
			print("is_alive: %s!" % self.is_alive)
			Player.gameover(self)
		else:
			print("check_hp - Valid: %s/%s" % (self.hp, self.max_hp))

	def update_stats(self):
		pass

	def equip_weapon(self, weapon):
		self.strength = self.strength + weapon.stats['strength']
		self.affinity = self.affinity + weapon.stats['affinity']
		self.precision = self.precision + weapon.stats['precision']

	def basic_attack(self):
		physical_damage = self.strength
		print("basic_attack - %s physical_damage" % physical_damage)
		return physical_damage

	def gameover(self):
		print("Your journey has ended.")
		#save
		#system exit
'''
	def attack(self, enemy):
		print (" %s, %s - Level %d\n hp: %d/%d\n Attack: %d\n Defence: %d\n Rage: %s/%s" % (self.name, self.spec, self.level, self.hp, self.maxhp, self.attack ,self.defence, self.rage, self.maxRage))
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
				enemy.hp -= pDamage
				print ("[PLAYER] >> [Basic Attack] deals (%d) physical damage." % (pDamage))
		elif int(choice) == 2:
			if pDamage <= 0:
				print ("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
				print ("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
			else:
				enemy.hp -= qa1
				enemy.hp -= qa2
				print ("[PLAYER] >> [Quick Attack] deals (%d) physical damage." % (qa1))
				print ("[PLAYER] >> [Quick Attack] deals (%d) physical damage." % (qa2))
		elif int(choice) == 3:
			enemy.hp -= es
			print ("[PLAYER] >> [Ethereal Strike] deals (%d) ethereal damage." % (es))
		elif int(choice) == 4:
			print "[PLAYER] >> %s uses [Random Potion]!" % self.name
		elif int(choice) == 5:
			print "Resetting Game"
			#reset()
		else:
			print "Invalid Entry - Please selet an option."
			Player.attack(self, enemy)
		pass

			
	def gameover(self):
		if self.alive == False:
			print("No! I have lost!")
			sys.exit(0)

	def sequence(self, enemy):
		Player.checkhp(self)
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
		Player.checkhp(self)
		if self.alive == False:
			Player.gameover(self)
		else:
			Player.attack(self, enemy)
###
# Accessors and Mutators
###
	def setStats(self, hp, attack, defence):
		self.hp = hp
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
		print ("You are now level %d! You have gained 3 hp, 1 attack, and 1 defence.\n" % (self.level))

		""" Stats for Acolyte && ez mode level up """
		self.maxhp += 3
		self.hp = self.maxhp
		self.attack += 1
		self.defence += 1

"""
Player.print methods

	def playerStats(self):
		pStats = (" %s, %s - Level %d - Experience: %d/%d\n hp: %d/%d Attack: %d Defence: %d\n Gold: %d \n Rage: %s/%s" % (self.name, self.spec, self.level, self.exp, self.maxExp, self.hp, self.maxhp, self.attack ,self.defence, self.gold)
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
		pDamage = self.attack - enemy.defence
		enemy.hp -= pDamage
		if pDamage <= 0:
			print ("Your attack deals no damage.")
		else:
			self.rage += pDamage
			if self.rage > self.maxRage:
				self.rage = self.maxRage
			print ("You attack %s for %d and now have %d/%d rage, it has %d hp remaining." % (enemy.name, pDamage, self.rage, self.maxRage, enemy.hp))
			if self.rage >= self.skill1rr and self.rage >= 10:
				Player.skill1(self, enemy)
			print ""
		pass

	def skill1(self, enemy):
		if enemy.hp >= 1: 
			skill1Damage = self.attack - enemy.defence
			enemy.hp -= skill1Damage
			print ("You perform a %s for %d, %s has %d hp remaining." % (self.skill1, skill1Damage, enemy.name, enemy.hp))
			self.rage -= 10
"""
'''

if __name__ == "__main__":
	dead_player = Player(0, 10, 1, 1, 1, 1, 1, 10, "Medell", None, True)
	alive_player = Player(100, 123, 5, 5, 10, 4, 299, 300, "Althea", "Ethereal", True)
	glitch_player = Player(999, 998, 99, 99, 99, 23, 10, 25, "Reulan", "Spellblade", True)
	
	print("=========================D")
	Player.print_stats(dead_player)
	Player.check_hp(dead_player)
	Player.basic_attack(dead_player)
	print("=========================A")
	Player.print_stats(alive_player)
	Player.check_hp(alive_player)
	Player.basic_attack(alive_player)
	print("=========================G")
	Player.print_stats(glitch_player)
	Player.check_hp(glitch_player)
	Player.basic_attack(glitch_player)	