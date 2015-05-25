"""
soulgem.py - Creating a template for soulgems.

Author: mpmsimo
Created: 5/23/15

Creates a soulgem object, with a stat values, an ability and a passive.
Soulgems grant abilities from members of the Order of the Spellblade.
"""
from tabulate import tabulate
import game_information as gi

souls = gi.souls

class Soulgem(object):
    def __init__(self, name, archetype, affinity, max_hp, strength, dexterity, intelligence, ability, passive):
        """Creates the soulgem object."""
        self.name = name
        self.archetype = archetype
        self.affinity = affinity
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.ability = ability
        self.passive = passive

    def print_soulgem(self, sort="all"):
        """Prints the soulgem description"""
        print("{0} the {1} [{2}]\n\tHP: {3}/{4}".format(self.name, self.archetype, self.affinity, self.hp, self.max_hp))
        print("\t* Strength: {0}\n\t* Dexterity: {1}\n\t* Intelligence: {2}\n".format(self.strength, self.dexterity, self.intelligence))
        
        headers = ["Type", "Name", "Description", "Damage"]
        table = [[self.ability["ability"]["type"], self.ability["ability"]["name"], self.ability["ability"]["description"]], \
                        [self.passive["passive"]["type"], self.passive["passive"]["name"], self.passive["passive"]["description"]]]
        print tabulate(table, headers, tablefmt="plain")        

''' Advanced tooltip?
        ability_headers = ["Name", "Type", "Damage", "Range"]
        ability_table = [[self.ability["ability"]["name"], self.ability["ability"]["type"], self.ability["ability"]["damage"],  self.ability["ability"]["range"]],\
                        [self.passive["passive"]["name"], self.passive["passive"]["type"], self.passive["passive"]["damage"],  self.passive["passive"]["range"]]]
        print tabulate(ability_table, ability_headers, tablefmt="plain")
'''