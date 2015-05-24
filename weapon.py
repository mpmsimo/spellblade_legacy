"""
weapon.py - Creating a weapon/item template that characters can equip.

Author: mpmsimo
Created: 1/10/15
Updated: 5/19/15

Creates a weapon object, with a damage value, weapon type and stats. 
"""

import random
import sys

import getpass

class Weapon(object):
    def __init__(self, name, item_slot, weapon_type, damage, stats, spellgems):
        """Constructs the base weapon with a item_slot and a weapon_type."""
        self.name = name
        self.item_slot = item_slot
        self.weapon_type = weapon_type
        self.damage = damage
        self.stats = {"strength": stats["strength"],
                    "intelligence": stats["intelligence"],
                    "dexterity": stats["dexterity"]}
        self.spellgems = {"sg1": None,
                            "sg2": None,
                            "sg3": None}
    def print_stats(self):
        """Prints weapon statistics."""
        weapon_stats = (("=========================\n"
                        "{0} - [{1}, {2}]\n"
                        "  Damage: {3}\n"
                        "\t* Strength: {4}\n"
                        "\t* Intelligence: {5}\n"
                        "\t* Dexterity: {6}\n"
                        "\n  Spellgems\n"
                        #"\t* Spellgem 1: {7}\n"
                        #"\t* Spellgem 2: {8}"\n"
                        #"\t* Spellgem 3: {9}"\n"
                        "=========================").format(self.name, self.item_slot, \
                                                            self.weapon_type, self.damage, \
                                                            self.stats["strength"],self.stats["intelligence"], self.stats["dexterity"])) #\
                                                            #self.spellgems["sg1"], self.spellgems["sg2"], self.spellgems["sg3"]))
        print(weapon_stats)

    def get_damage(self):
        """Returns weapon damage"""
        return(self.damage)

    def set_damage(self, damage):
        """Sets weapon damage"""
        new_damage = damage

    def get_stats(self):
        """Returns the weapon object"""
        return self.stats

    def set_stats(self, new_stats):
        """Returns weapons stats if they exist"""
        self.stats["strength"] = new_stats["strength"]
        self.stats["intelligence"] = new_stats["intelligence"]
        self.stats["dexterity"] = new_stats["dexterity"]

'''
class Sword(Weapon):
    def __init__(self, name, item_slot, weapon_type="Sword", damage, stats, spellgems):
'''
