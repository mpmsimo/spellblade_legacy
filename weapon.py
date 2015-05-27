#!/usr/bin/env python
"""
weapon.py - Creating a weapon/item template that characters can equip.

Author: mpmsimo
Created: 1/10/15

Creates a weapon object, with a damage value, weapon type and sockets. 
"""

from tabulate import tabulate

class Weapon(object):
    def __init__(self, name, item_slot, weapon_type, damage, sockets, ability):
        """Constructs the base weapon with a item_slot and a weapon_type."""
        self.name = name
        self.item_slot = item_slot
        self.weapon_type = weapon_type
        self.damage = damage
        self.sockets = sockets
        self.ability = ability

    def get_item_slot(self):
        if self.item_slot == 0:
            return "Main Hand"
        elif self.item_slot == 1:
            return "Off Hand"
        elif self.item_slot == 2:
            return "Two Handed"
        else:
            return "Unknown"

    def print_weapon(self):
        """Prints weapon statistics."""
        item_slot_string = self.get_item_slot()
        weapon = (("{0} - [{1}, {2}]\n"
                    "\tDamage: {3}\n"
                    "\tSockets: {4}\n").format(self.name, item_slot_string, \
                                                self.weapon_type, self.damage, \
                                                self.sockets["sockets"]["amount"]))
        print(weapon)

        headers = ["Type", "Name", "Description", "Damage"]
        table = [[self.ability["ability"]["type"], self.ability["ability"]["name"], self.ability["ability"]["description"]]]
        print tabulate(table, headers, tablefmt="plain")  

    def get_damage(self):
        """Returns weapon damage"""
        return(self.damage)

    def set_damage(self, damage):
        """Sets weapon damage"""
        new_damage = damage

    def get_sockets(self):
        """Returns the weapon object"""
        return self.sockets