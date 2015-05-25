#!/usr/bin/env python
"""
weapon.py - Creating a weapon/item template that characters can equip.

Author: mpmsimo
Created: 1/10/15

Creates a weapon object, with a damage value, weapon type and sockets. 
"""

class Weapon(object):
    def __init__(self, name, item_slot, weapon_type, damage, sockets, ability):
        """Constructs the base weapon with a item_slot and a weapon_type."""
        self.name = name
        self.item_slot = item_slot
        self.weapon_type = weapon_type
        self.damage = damage
        self.sockets = sockets
        self.ability = ability

    def print_weapon(self):
        """Prints weapon statistics."""
        weapon_sockets = (("=========================\n"
                        "{0} - [{1}, {2}]\n"
                        "  Damage: {3}\n"
                        "\t* Sockets: {4}\n"
                        "\t* Ability: {5}\n"
                        "=========================").format(self.name, self.item_slot, \
                                                            self.weapon_type, self.damage, \
                                                            self.sockets, self.ability))
        print(weapon_sockets)

    def get_damage(self):
        """Returns weapon damage"""
        return(self.damage)

    def set_damage(self, damage):
        """Sets weapon damage"""
        new_damage = damage

    def get_sockets(self):
        """Returns the weapon object"""
        return self.sockets