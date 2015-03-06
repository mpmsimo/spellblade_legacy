"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon, player

def main():
	def __init__(self, max_hp, name, level, exp, max_exp, strength, dexterity, magic):
	althea = player.Player(100, "Althea", 10, 1337, 2048, 7, 4, 10)
	althea.print_stats()
'''
	hero = player.Player(10, 12, 5, 5, 10, 4, 250, 300, "Althea", True)
	#dead_player = Player(0, 10, 1, 1, 1, 1, 1, 10, "Medell", True)
	#alive_player = Player(100, 123, 5, 5, 10, 4, 299, 300, "Althea", True)
	#glitch_player = Player(999, 998, 99, 99, 99, 23, 10, 25, "Reulan", True)
	
	category = "Main-hand"
	subclass = "Spellblade"
	damage = 170

	player_weapon = weapon.Weapon(category, subclass, damage)
	player_weapon.print_stats()
	
	player_weapon.set_damage(171)
	player_weapon.get_damage()

	player_weapon.set_passive("Passive")
	player_weapon.get_passive()

	player_weapon.set_active("Active")
	player_weapon.get_active()

	hero.print_stats()
	#hero.check_hp()
	#hero.equip_weapon(player_weapon)

	########## Stats for testing Weapon ##########
    weapon_name = "Crowlissa"
    weapon_category = "Main-hand"
    weapon_subclass = "Spellblade"
    weapon_damage = 170

    weapon_stats = {"strength": 100,
		            "affinity": 1337,
		            "dexterity": 8}

	########## Stats for testing Player ##########
    equipped_weapon = weapon.Weapon(weapon_name, weapon_category, weapon_subclass, weapon_damage, weapon_stats)

    player_hp = 15
    player_max_hp = 15
    player_name = "Reulan"
    player_stats = {"strength": 33, 
    				"affinity": 144,
    				"dexterity": 170}

    hero = player.Player(player_hp, player_max_hp, player_name, player_stats["strength"], player_stats["affinity"], player_stats["dexterity"])

    ########## Player stat comparison ########## 
    hero.equip_weapon(equipped_weapon)
    hero.print_stats()

 	########## Weapon damage, active and passive ##########   
    equipped_weapon.set_damage(171)
    equipped_weapon.get_damage()
    equipped_weapon.print_stats()
'''

if __name__ == "__main__": main()  