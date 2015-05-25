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
    print("Welcome to the Spellblade: Legacy!")
    player_name = name_character()
    choose_affinity()
    soulgem = choose_soulgem()

def name_character():
    """Renames the player"""
    player_name = raw_input("Please choose a name for your character: ")
    return player_name
    #return str(player_name)

def choose_affinity():
    """Option to see str/dex/int heroes."""
    affinities = ["Strength", "Dexterity", "Intelligence"]
    for i in range(len(affinities)):
        print("Index: {0}\nElement: {1}".format(affinities[i], i))

def choose_soulgem():
    """Soulgem choice"""
    count = 1
    souls = gi.souls
    for hero in souls:
        print("\n{0}.".format(count))
        sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
        sg.print_soulgem()
        count+=1
    choice = raw_input("Select a member of the Order of the Spellblade you would like to embody.")

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