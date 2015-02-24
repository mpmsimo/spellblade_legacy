"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon, player

def main():
	#player = p.Player(100, 123, 5, 5, 10, 4, 299, 300, "Althea", True)
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

if __name__ == "__main__":
	main()  