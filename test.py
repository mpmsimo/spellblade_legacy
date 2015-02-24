"""
game.py - This is where objects are created and the game is played.
msimo - 1/11/2015

Python 3.3.6
"""
import weapon as w, player as p

player = p.Player(100, 123, 5, 5, 10, 4, 299, 300, "Althea", True)
category = "Spellblade"
attack = 170
stats = {'strength': 1, 'affinity': 33, 'precision': 7}
weapon = w.Weapon(category, attack, stats)
print("variable assignment complete")

if __name__ == "__main__":
	print("=========================")
	player.print_stats()
	player.check_hp()  
	player.basic_attack()
	print("=========================")
	weapon.print_stats()
	player.equip_weapon(weapon)
	print("Weapon equipped.")
	player.print_stats()
	print("test")