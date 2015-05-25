"""
game_information.py - Contains information that is used across the game.

Author: mpmsimo
Created: 5/25/15
"""

# A dictionary containing a soulgem, which is represented by a name, archetype, ability, passive, hp, and stat values.
# Additionally, the ability, and passives are dictionaries which contain additional information about the skill.
souls = {"althea": ["Althea", "Ethereal Warden", "Strength", 400, 6, 4, 2, \
          {"ability": {"name": "Crushing Strike", "description": "A crushing attack, strikes up to two targets.", "damage": "(str * level) + damage", "type": "skill", "range": "melee"}}, \
          {"passive": {"name": "Enchanted Rage", "description": "Intelligence is added to Strength.", "damage": None, "type": "passive", "range": "self"}}],
        "wargen": ["Wargen", "Human Warrior", "Strength", 600, 8, 4, 0, \
          {"ability": {"name": "Charge", "description": "Charges the enemy, stunning the target for 2 turns.", "damage": "stun2", "type": "skill", "range": "medium"}}, \
          {"passive": {"name": "Well equipped", "description": "You always seem to have the right weapon for the fight.", "damage": None, "type": "passive", "range": "self"}}],
        "obsydia": ["Obsydia", "Ravenblade", "Dexterity", 350, 2, 10, 0, \
          {"ability": {"name": "Pistol Shot", "description": "Deals a high amount of damage to a single target.", "damage": "((1 * level) + .5(dex)) + damage", "type": "skill", "range": "short"}}, \
          {"passive": {"name": "Swashbuckler", "description": "+4 strength and dexterity while wielding a sword", "damage": None, "type": "passive", "range": "self"}}],
        "malathak": ["Malathak", "Master of Gems", "Intelligence", 100, 0, 0, 12, \
          {"ability": {"name": "Prismatic Barrage", "description": "Fires a barrage of prismatic missiles, one barrage per spellgem equipped. ", "damage": "int * spellgem_amount", "type": "skill", "range": "long"}}, \
          {"passive": {"name": "Jewelcrafter", "description": "+1 to sockets on all weapons.", "damage": None, "type": "passive", "range": "self"}}]}