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
    def __init__(self, name, category, subclass, damage, stats):
        """Constructs the base weapon with a category and a subclass."""
        self.name = name
        self.category = category
        self.subclass = subclass
        self.damage = damage
        self.stats = {"strength": stats["strength"],
                    "affinity": stats["affinity"],
                    "dexterity": stats["dexterity"]}

    def print_stats(self):
        """Prints weapon statistics."""
        weapon_stats = (("=========================\n"
                        "{0} - [{1}, {2}]\n"
                        "  Damage: {3}\n"
                        "\t* Strength: {4}\n"
                        "\t* Affinity: {5}\n"
                        "\t* Dexterity: {6}\n"
                        "=========================").format(self.name, self.category, \
                                                            self.subclass, self.damage, \
                                                            self.stats["strength"], self.stats["affinity"], self.stats["dexterity"]))
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
        self.stats["affinity"] = new_stats["affinity"]
        self.stats["dexterity"] = new_stats["dexterity"]
