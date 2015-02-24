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
            Weapon Category
            Weapon Subclass
            Weapon Damage
            Passive
            Active

            Restriction
            Level Requirement
            Item Level
            Rarity
            Flavor Text
    """
    def __init__(self, category, subclass, damage):
        """
        Constructs the base weapon. (Ex. Main-hand - Longsword, Off-hand - Pistol)
        """
        self.category = category
        self.subclass = subclass
        self.damage = damage
        self.passive = None
        self.active = None

    def print_stats(self):
        """
        Prints player statistics.
        """
        #weapon_stats = (("Category: {0} || Attack: {1} || Strength: {2} || Affinity: {3} || Precision: {4}".format(self.category, self.attack, self.stats['strength'], self.stats['affinity'], self.stats['precision'])))
        weapon_stats = ("""=========================
[{0} - {1}]
    * Damage: {2}
    * Active: {3}
    * Passive: {4}
=========================""".format(self.category, self.subclass, self.damage, self.active, self.passive))
        print(weapon_stats)

    def get_damage(self):
        print("damage: {0}".format(self.damage))
        return(self.damage)

    def set_damage(self,  damage):
        new_damage = damage
        print("""setdamage
            Old: damage {0}
            New: new_damage {1}""".format(self.damage, new_damage))
        return new_damage

    def get_passive(self):
        print("passive: {0}".format(self.passive))
        return(self.passive)

    def set_passive(self, passive):
        new_passive = passive
        print("""setpassive
            Old: passive {0}
            New: new_passive {1}""".format(self.passive, new_passive))
        return new_passive

    def get_active(self):
        print("active: {0}".format(self.active))
        return(self.active)

    def set_active(self, active):
        new_active = active
        print("""setactive
            Old: active {0}
            New: new_active {1}""".format(self.active, new_active))
        return new_active


if __name__ == "__main__":
    category = "Main-hand"
    subclass = "Spellblade"
    damage = 170

    weapon = Weapon(category, subclass, damage)

    Weapon.print_stats(weapon)