"""
weapon.py - 
msimo - 1/10/15
"""
import random, sys, getpass

"""
Weapon Class

calc_dps()
Item Level
Rarity

Stats
Damage
+static
+attack%, arp%

Grip
Rune

Restriction
Level Requirement

Flavor Text
"""

class Weapon(object):
        """ __init__(int, int, int)__
                Weapon Type
                Weapon Damage
                Modifiers
                Stat 1
                Stat 2
                Passive
                Active

                Restriction
                Level Requirement
                Item Level
                Rarity
                Flavor Text
     """

        def __init__(self, category, attack, stats):
                """stat only takes dictionary objects, add passive later"""
                self.category = category
                self.attack = attack
                self.stats = stats

        def print_stats(self):
                """Prints player statistics."""
                weapon_stats = (("Category: %s || Attack: %s || Strength: %s || Affinity: %s || Precision: %s") % (self.category, self.attack, self.stats['strength'], self.stats['affinity'], self.stats['precision']))
                print(weapon_stats)

if __name__ == "__main__":
        category = "Spellblade"
        attack = 170
        stats = {'strength': 1, 'affinity': 33, 'precision': 7,}
        weapon = Weapon(category, attack, stats)
        
        print("=========================")
        Weapon.print_stats(weapon)