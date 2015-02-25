"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon, player

def main():
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
	hero.check_hp()
	#hero.equip_weapon(player_weapon)

if __name__ == "__main__":
	main()  