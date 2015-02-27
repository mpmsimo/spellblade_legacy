"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon, player

def main():
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

if __name__ == "__main__":
	main()  