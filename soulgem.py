"""
soulgem.py - Creating a template for soulgems.

Author: mpmsimo
Created: 5/23/15
Updated: 5/24/15

Creates a soulgem object, with a stat values, an ability and a passive.
Soulgems grant abilities from members of the Order of the Spellblade.
"""

import random
import sys
import weapon
from tabulate import tabulate

# A dictionary containing a soulgem, which is represented by a name, archetype, ability, passive, hp, and stat values.
# Additionally, the ability, and passives are dictionaries which contain additional information about the skill.
hero_souls = {"althea": ["Althea", "Ethereal Warden", "Strength", \
                {"ability": {"name": "Crushing Strike", "description": "Deals a crushing blow striking up to two targets.", "damage": "(str * level) + damage", "type": "skill", "range": "melee"}}, \
                {"passive": {"name": "Enchanted Rage", "description": "Intelligence is converted to strength.", "damage": None, "type": "passive", "range": "self"}}, \
                400, 6, 4, 2]}

class Soulgem(object):
    def __init__(self, name, archetype, affinity, ability, passive, max_hp, strength, dexterity, intelligence):
        """Creates the soulgem object."""
        self.name = name
        self.archetype = archetype
        self.affinity = affinity
        self.ability = ability
        self.passive = passive
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def print_soulgem(self):
        """Prints the soulgem description"""
        print(80 * "=")
        print("{0} the {1} [{2}]\n\tHP: {3}/{4}".format(self.name, self.archetype, self.affinity, self.hp, self.max_hp))
        print("\t* Strength: {0}\n\t* Dexterity: {1}\n\t* Intelligence: {2}\n".format(self.strength, self.dexterity, self.intelligence))
        ability_headers = ["Name", "Type", "Damage", "Range"]
        ability_table = [[self.ability["ability"]["name"], self.ability["ability"]["type"], self.ability["ability"]["damage"],  self.ability["ability"]["range"]],\
                        [self.passive["passive"]["name"], self.passive["passive"]["type"], self.passive["passive"]["damage"],  self.passive["passive"]["range"]]]
        print tabulate(ability_table, ability_headers, tablefmt="plain")
        print(80 * "=")

    def print_abilities(self):
        """Prints the soulgem abiliteis description"""
        headers = ["Name", "Description", "Damage"]
        table = [[self.ability["ability"]["name"], self.ability["ability"]["description"], self.ability["ability"]["damage"]], \
                        [self.passive["passive"]["name"], self.passive["passive"]["description"], self.passive["passive"]["damage"]]]
        print tabulate(table, headers, tablefmt="plain")

def main():
    hero = "althea"
    soulgem = Soulgem(hero_souls[hero][0], hero_souls[hero][1], hero_souls[hero][2], hero_souls[hero][3], hero_souls[hero][4], hero_souls[hero][5], hero_souls[hero][6], hero_souls[hero][7], hero_souls[hero][8])
    soulgem.print_soulgem()
    soulgem.print_abilities()

if __name__ == "__main__":
    main()