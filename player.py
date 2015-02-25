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
		"""
		Prints player statistics.
		"""
		player_stats = ("========================\n{0}, Level {1} \nXP: [{2}/{3}] \nHP: [{4}/{5}] \n* Strength: {6} \n* Affinity: {7} \n* Precision: {8} \n=========================".format(self.name, self.level, self.exp, self.max_exp, self.hp, self.max_hp, self.strength ,self.affinity, self.precision))
		print(player_stats)

	def check_hp(self):
		print("check_hp - before:  {0}/{1}".format(self.hp, self.max_hp))
		if self.hp > self.max_hp:
			print("check_hp - cur greater than max_hp: {0}/{1}".format(self.hp, self.max_hp))
			self.hp = self.max_hp
			print("check_hp - after:  {0}/{1}".format(self.hp, self.max_hp))		
		elif self.hp <= 0:
			print("check_hp - dead hp: {0}/{1}".format(self.hp, self.max_hp))
			self.is_alive = False
			print("is_alive: {0}!".format(self.is_alive))
		else:
			print("check_hp - Valid: {0}/{1}".format(self.hp, self.max_hp))

	def update_stats(self):
		pass

	def equip_weapon(self, weapon):
		self.strength = self.strength + weapon.stats['strength']
		self.affinity = self.affinity + weapon.stats['affinity']
		self.precision = self.precision + weapon.stats['precision']

	def basic_attack(self):
		physical_damage = self.strength
		print("basic_attack - {0} physical_damage".format(physical_damage))
		return physical_damage

	def attack(self, enemy):
		print(" {0}, {1} - Level {2}\n hp: {3}/{4}\n Attack: {5}\n Defence: {6}\n Rage: {7}/{8}".format(self.name, self.spec, self.level, self.hp, self.maxhp, self.attack ,self.defence, self.rage, self.maxRage))
		print("")
		print("Please select an attack.\n1. Basic Attack\n2. {0}\n3. {1}\n4. Items\n".format(self.skill1, self.skill2))
		
		try:		
			choice = input("CHOICE >> ")
		except ValueError:
			print("{0} is not an integer!".format(choice))
			print("Forgive me, but you have not entered a valid integer option...")
			print("Closing game, sorry bro")

		print ("")
		
		#Choose attack - Autoattack, skill1, skill2, item
		player_damage = self.damage
		quick_attack_1 = self.attack * .75
		quick_attack_1qa2 = self.attack * .50
		es = self.attack + self.level

		if choice == 1:
			if pDamage <= 0:
				print("[PLAYER] >> [Basic Attack] deals 0 physical damage.")
			else:
				enemy.hp -= pDamage
				print("[PLAYER] >> [Basic Attack] deals ({0}) physical damage.".format(pDamage))
		elif int(choice) == 2:
			if pDamage <= 0:
				print("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
				print("[PLAYER] >> [Quick Attack] deals 0 physical damage.")
			else:
				enemy.hp -= qa1
				enemy.hp -= qa2
				print("[PLAYER] >> [Quick Attack] deals ({0}) physical damage.".format(qa1))
				print("[PLAYER] >> [Quick Attack] deals ({0}) physical damage.".format(qa2))
		elif int(choice) == 3:
			enemy.hp -= es
			print("[PLAYER] >> [Ethereal Strike] deals ({0}) ethereal damage.".format(es))
		elif int(choice) == 4:
			print("[PLAYER] >> {0} uses [Random Potion]!".format(self.name))
		elif int(choice) == 5:
			print("Resetting Game")
			#reset()
		else:
			print("Invalid Entry - Please selet an option.")
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
		print("You are now level {0}! You have gained 3 hp, 1 attack, and 1 defence.\n".format(self.level))

		""" Stats for Acolyte && ez mode level up """
		self.maxhp += 3
		self.hp = self.maxhp
		self.attack += 1
		self.defence += 1

"""
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
		pDamage = self.attack - enemy.defence
		enemy.hp -= pDamage
		if pDamage <= 0:
			print ("Your attack deals no damage.")
		else:
			self.rage += pDamage
			if self.rage > self.maxRage:
				self.rage = self.maxRage
			print ("You attack {} for {} and now have {}/{} rage, it has {} hp remaining." % (enemy.name, pDamage, self.rage, self.maxRage, enemy.hp))
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
"""
if __name__ == "__main__":
	#(self, hp, max_hp, strength, affinity, precision, level, exp, max_exp, name, is_alive):
	dead_player = Player(0, 10, 1, 1, 1, 1, 1, 10, "Medell", True)
	alive_player = Player(100, 123, 5, 5, 10, 4, 299, 300, "Althea", True)
	glitch_player = Player(999, 998, 99, 99, 99, 23, 10, 25, "Reulan", True)
	
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