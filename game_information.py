#!/usr/bin/env python
"""
game_information.py - Contains information that is used across the game.

Author: mpmsimo
Created: 5/25/15
"""

# A dictionary containing a soulgem, which is represented by a name, archetype, ability, passive, hp, and stat values.
# Additionally, the ability, and passives are dictionaries which contain additional information about the skill.
souls = {"althea": ["Althea", "Ethereal Warden", "Strength", 400, 6, 4, 2, \
          {"ability": {"name": "Crushing Strike", "description": "A crushing attack, strikes up to two targets.", "damage": "(1 * level) + strength + damage", "type": "skill", "range": "melee"}}, \
          {"passive": {"name": "Enchanted Rage", "description": "Intelligence is added to Strength.", "damage": None, "type": "passive", "range": "self"}}],
        "wargen": ["Wargen", "Human Warrior", "Strength", 600, 8, 4, 0, \
          {"ability": {"name": "Charge", "description": "Charges the enemy, stunning the target for 2 turns.", "damage": "stun2", "type": "skill", "range": "medium"}}, \
          {"passive": {"name": "Combat Veteran", "description": "You always seem to have the fighting style against your opponent.", "damage": None, "type": "passive", "range": "self"}}],
        "obsydia": ["Obsydia", "Ravenblade", "Dexterity", 350, 2, 10, 0, \
          {"ability": {"name": "Pistol Shot", "description": "Deals a high amount of damage to a single target.", "damage": "dex + damage", "type": "skill", "range": "short"}}, \
          {"passive": {"name": "Swashbuckler", "description": "+4 strength and dexterity while wielding a sword", "damage": None, "type": "passive", "range": "self"}}],
        "malathak": ["Malathak", "Master of Gems", "Intelligence", 100, 0, 0, 12, \
          {"ability": {"name": "Prismatic Barrage", "description": "Fires a barrage of prismatic missiles, one barrage per spellgem equipped. ", "damage": "int * weapon_sockets", "type": "skill", "range": "long"}}, \
          {"passive": {"name": "Jewelcrafter", "description": "+1 to sockets on all weapons.", "damage": None, "type": "passive", "range": "self"}}]}

# A dictionary of weapons, similar to the list of soulgems.
# Weapon Types: 0 = Main Hand, 1 = Off Hand, 2 = Two Handed
weapons = {"longsword": ["Longsword", 2, "Sword", 10,  \
            {"sockets": {"amount": 2}}, \
            {"ability": {"name": "Heavy Strike", "description": "A powerful two handed swing against a single target.", "damage": "damage + str", "type": "skill", "range": "melee"}}], 
          "sabre": ["Sabre", 0, "Sword", 5,  \
            {"sockets": {"amount": 0}}, \
            {"ability": {"name": "3x strike", "description": "Quickly attack three times in a row", "damage": "damage + .5(dex)", "type": "skill", "range": "melee"}}],
          "blade": ["Blade", 0, "Dagger", 0,  \
            {"sockets": {"amount": 7}}, \
            {"ability": {"name": "Gemglow", "description": "Each gem in this weapon glows, healing you for each gem.", "damage": "gems+.5int", "type": "spell", "target": "ally"}}]}

'''Weapon design
Weapon (Determines what types of skills you can use)
Affinity (Shows what the weapon synergizes with)
Sockets (Allows placement of spellgems to further modify the weapons)
Range (How far away you can attack from)
Damage (How much damage you do)

Ability (A skill unique to the weapon equipped)
 name
 damage
 resource cost
 target
 effect
'''

# A dictonary of enemies
#def __init__(self, name, enemy_type, level, max_hp, strength, dexterity, intelligence):
enemies = {"goblin": ["Goblin", "Humanoid", 2, 50, 4, 1, 0],
            "orc": ["Orc", "Humanoid", 3, 125, 5, 2, 0],
            "thug": ["Thug", "Humanoid", 3, 100, 4, 4, 0],
            "dragon": ["Dragon", "Dragon", 50, 9999, 600, 400, 1000],
            "thug": ["Thug", "Humanoid", 3, 100, 4, 4, 0],
            "mystic": ["Mystic", "Humanoid", 3, 75, 0, 0, 7]}

# A dictionary of loot!!!!
loot = {"currency": ["gold", "gem fragments", "raven RAIN", "crusade MEMORY"]}
