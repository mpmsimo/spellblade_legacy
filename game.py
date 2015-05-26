#!/usr/bin/env python
"""
game.py - This is where objects are created and the game is played.

Author: mpmsimo
Created: 2/21/2015
"""

import tabulate

import weapon
import player
import soulgem
import game_information as gi

def character_creation():
    """Choose a character name"""
    print("Welcome to the Spellblade: Legacy!\n")
    #player_name = name_character()
    affinity = choose_affinity()
    soulgem = choose_soulgem(affinity)

def name_character():
    """Renames the player"""
    player_name = raw_input("Please choose a name for your character: ")
    return player_name
    #return str(player_name)

def choose_affinity():
    """Option to see str/dex/int heroes."""
    affinities = ["Strength", "Dexterity", "Intelligence"]
    for i in range(len(affinities)):
        print("{0}. {1}".format(i+1, affinities[i]))
    choice = int(raw_input("Show aligned souls for affinity: "))
    if choice in range(1, len(affinities)+1):
        print("You chose {0}.\n".format(affinities[choice-1]))
    else:
        print(range(1, len(affinities)+1))
        print("You have entered an incorrect value, please try again.\n")
        choose_affinity()
    return affinities[choice-1]

def choose_soulgem(affinity):
    """Soulgem choice"""
    count = 1
    souls = gi.souls
    for hero in souls:
        sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
        if affinity == sg.affinity:
            print("\n{0}. {1}".format(count, sg.name))
            sg.print_soulgem()
            count+=1
    choice = int(raw_input("\nSelect a member of the Order of the Spellblade you would like to embody: "))

def main():
    character_creation()
    althea = player.Player(100, "Althea", 10, 1337, 2048, 0, 0, 0)
    althea.print_stats()
    longsword = weapon.Weapon("Longsword", "Main Hand", "Sword", 10, 1, "Sweeping Strike")
    longsword.print_weapon()
    #althea.equip_weapon(longsword)
    althea.print_stats()

if __name__ == "__main__":
    main()
