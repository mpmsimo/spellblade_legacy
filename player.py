#!/usr/bin/env python
"""
player.py - Default player class

Author: mpmsimo
Created: 1/7/2015

A player object with HP, name, level, exp, and basic stats.

To-do:
 * Rename to character.py and change the imports neeeded.
"""

from tabulate import tabulate

class Character(object):
    def __init__(self, name, level, max_hp, strength, dexterity, intelligence):
        """Creates a character object, containing methods which the player can use."""
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

class Enemy(Character):
    def __init__(self, name, level, max_hp, strength, dexterity, intelligence):
        """Creates an enemy object."""
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def print_basic(self):
        """Prints player statistics."""
        print(("\n========================\n"
            "{0}, Level {1}\n"
            "HP: [{2}/{3}]\n"
            "\t* Strength: {4}\n"
            "\t* Dexterity: {5}\n"
            "\t* Intelligence: {6}\n"
            "=========================").format(self.name, self.level, \
                                                    self.hp, self.max_hp, self.strength, \
                                                    self.dexterity, self.intelligence))

class Player(Character):
    def __init__(self, name, level, exp, max_exp, max_hp, strength, dexterity, intelligence):
        """Creates the player object, and has the methods which the player can use."""
        self.level = level
        self.exp = exp
        self.max_exp = max_exp
        self.max_hp = max_hp
        self.hp = max_hp
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

        self.weapon_name = None
        self.weapon_affinity = None
        self.weapon_damage = None
        self.weapon_item_slot = None
        self.weapon_type = None
        self.weapon_damage = None
        self.weapon_sockets = None
        self.weapon_ability = None

        self.soulgem_name = None
        self.soulgem_max_hp = None
        self.soulgem_hp = None
        self.soulgem_strength = None
        self.soulgem_dexterity = None
        self.soulgem_intelligence = None
        self.soulgem_affinity = None
        self.soulgem_archetype = None
        self.soulgem_ability = None
        self.soulgem_passive = None

    def print_debug(self):
        """Prints debug information."""
        print("Player\nStr: {0}\nDex: {1}\nInt: {2}\n".format(self.strength, self.dexterity, self.intelligence))
        print("Soulgem\nStr: {0}\nDex: {1}\nInt: {2}\n".format(self.soulgem_strength, self.soulgem_dexterity, self.soulgem_intelligence))

    def print_basic(self):
        """Prints player statistics."""
        print(("\n========================\n"
            "{0}, Level {1}\n"
            "XP: [{2}/{3}]\n"
            "HP: [{4}/{5}]\n"
            "\t* Strength: {6}\n"
            "\t* Dexterity: {7}\n"
            "\t* Intelligence: {8}\n"
            "=========================").format(self.name, self.level, self.exp, \
                                                    self.max_exp, self.hp, self.max_hp, self.strength, \
                                                    self.dexterity, self.intelligence))

    def print_advanced(self):
        """Prints player statistics."""
        print(("\n========================\n"
            "{0}, Level {1}\n"
            "XP: [{2}/{3}]\n"
            "HP: [{4}/{5}]\n"
            "\t* Strength: {6}\n"
            "\t* Dexterity: {7}\n"
            "\t* Intelligence: {8}\n"
            "\nWeapon: {9}, {10}\n"
            "\t* Damage: {11}\n"
            "\t* Sockets: {12}\n"
            "=========================").format(self.name, self.level, self.exp, \
                                                    self.max_exp, self.hp, self.max_hp, self.strength, \
                                                    self.dexterity, self.intelligence, self.weapon_name, self.weapon_type, self.weapon_damage, self.weapon_sockets["sockets"]["amount"]))

    def equip_weapon(self, weapon):
        """Equips a weapon"""
        self.weapon_name = weapon.name
        self.weapon_damage = weapon.damage
        self.weapon_sockets = weapon.sockets
        self.weapon_item_slot = weapon.item_slot
        self.weapon_type = weapon.weapon_type
        self.weapon_ability = weapon.ability

    def equip_soulgem(self, soulgem):
        """Equips a soulgem giving the player stats and abilities from a hero."""
        #Soulgem specific stats
        self.soulgem_name = soulgem.name
        self.soulgem_max_hp = soulgem.max_hp

        self.soulgem_strength = soulgem.strength
        self.soulgem_dexterity = soulgem.dexterity
        self.soulgem_intelligence = soulgem.intelligence
        self.soulgem_archetype = soulgem.archetype
        self.soulgem_affinity = soulgem.affinity
        self.soulgem_ability = soulgem.ability
        self.soulgem_passive = soulgem.passive

        # Assigning stats to player
        self.max_hp = self.soulgem_max_hp
        self.hp = self.max_hp
        self.strength += self.soulgem_strength
        self.intelligence += self.soulgem_intelligence
        self.dexterity += self.soulgem_dexterity

    def show_abilities(self):
        print("")
        headers = ["Type", "Name", "Description", "Damage"]
        table = [[self.soulgem_ability["ability"]["type"], self.soulgem_ability["ability"]["name"], self.soulgem_ability["ability"]["description"]], \
                        [self.soulgem_passive["passive"]["type"], self.soulgem_passive["passive"]["name"], self.soulgem_passive["passive"]["description"]], \
                        [self.weapon_ability["ability"]["type"], self.weapon_ability["ability"]["name"], self.weapon_ability["ability"]["description"]]]
        print tabulate(table, headers, tablefmt="plain")

    def use_soulgem_ability(self):
        """Takes in a 'damage' value from an ability and parses the value"""
        print("{0}\n{1} damage\n".format(self.soulgem_ability["ability"]["name"], self.soulgem_ability["ability"]["damage"]))
        if self.soulgem_ability["ability"]["name"] == "Prismatic Barrage":
            for i in range(self.weapon_sockets["sockets"]["amount"]):
                print("A barrage hits for {0}".format(self.intelligence))
        elif self.soulgem_ability["ability"]["name"] == "Charge":
            print("Target has been stunned for {0} turns".format(self.soulgem_ability["ability"]["damage"]))

    def use_weapon_ability(self):
        print("{0} uses a {1}".format(self.name, self.weapon_ability["ability"]["name"]))

    def basic_attack(self):
        """Returns and prints amount of damage a basic attak does"""
        return self.weapon_damage

    def attack_menu(self):
        count = 1
        attacks = ["Basic Attack"]
        try:
            attacks.append(self.soulgem_ability["ability"]["name"])
            attacks.append(self.weapon_ability["ability"]["name"])
        except ValueError:
            pass
        for i in attacks:
            print("{0}. {1}".format(count, attacks[count-1]))
            count += 1
        choice = raw_input("Choose an attack: ")
        if choice == 1:
            print(basic_attack())
        elif int(choice) == 2:
            player.use_soulgem_ability()
        elif int(choice) == 3:
            player.use_weapon_ability()
