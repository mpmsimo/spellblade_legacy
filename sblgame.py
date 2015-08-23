#!/usr/bin/env python
"""
sblgame.py - This is where objects are created and the game is played.

Author: mpmsimo
Created: 2/21/2015
"""

import sys
import random

import weapon
import player
import soulgem
import game_information as gi

border = ('=' * 80)
souls = gi.souls
weapons = gi.weapons
enemies = gi.enemies
affinity = None

def character_creation():
    """Choose a character name"""
    player_name = name_character()
    affinity = choose_affinity()
    soulgem = choose_soulgem(affinity)
    weapon = choose_weapon()
    player = generate_player(player_name, soulgem, weapon)
    return player

def name_character():
    """Renames the player"""
    player_name = raw_input("Please choose a name for your character: ")
    return player_name

def choose_affinity():
    """Option to see str/dex/int heroes."""
    affinities = ["Strength", "Dexterity", "Intelligence"]
    for i in range(len(affinities)):
        print("{0}. {1}".format(i+1, affinities[i]))
    print("")
    choice = int(raw_input("Show aligned souls for affinity (0 to start over): "))
    if choice in range(1, len(affinities)+1):
        print("\nYou chose {0}.\n".format(affinities[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print(range(1, len(affinities)+1))
        print("You have entered an incorrect choice, please try again.\n")
        choose_affinity()
    return affinities[choice-1]

def choose_soulgem(affinity):
    """Soulgem choice"""
    count = 1
    soul_list = []
    for hero in souls:
        sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
        if affinity == sg.affinity:
            soul_list.append(hero)
            print("{0}\n{1}. {2}".format(border, count, sg.name))
            sg.print_soulgem()
            count+=1
        elif affinity == None:
            soul_list.append(hero)
            print("{0}\n{1}. {2}".format(border, count, sg.name))
            sg.print_soulgem()
            count+=1
    print(border)
    choice = int(raw_input("\nChoose the soul you would like to control (0 to start over): "))
    if choice in range(1, len(soul_list)+1):
        print("\nYou chose {0}.\n".format(soul_list[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print("You have entered an incorrect choice, please try again.\n")
        choose_soulgem(affinity)
    return soul_list[choice-1]

def choose_weapon():
    """Weapon choice"""
    count = 1
    weapon_list = []
    for wep in weapons:
        item = weapon.Weapon(weapons[wep][0], weapons[wep][1], weapons[wep][2], weapons[wep][3], weapons[wep][4], weapons[wep][5])
        weapon_list.append(wep)
        print("{0}\n{1}. {2}".format(border, count, item.name))
        item.print_weapon()
        count+=1
    print(border)
    choice = int(raw_input("\nChoose the weapon you would like to use (0 to start over): "))
    if choice in range(1, len(weapon_list)+1):
        print("\nYou chose {0}.\n".format(weapon_list[choice-1]))
    elif choice == 0:
        character_creation()
    else:
        print("You have entered an incorrect choice, please try again.\n")
        choose_weapon()
    return weapon_list[choice-1]

def generate_player(name, selected_soulgem, selected_weapon):
    for hero in souls:
        if hero == selected_soulgem:
            sg = soulgem.Soulgem(souls[hero][0], souls[hero][1], souls[hero][2], souls[hero][3], souls[hero][4], souls[hero][5], souls[hero][6], souls[hero][7], souls[hero][8])
            sblplayer = player.Player(name, 1, 0, 50, 1, 0, 0, 0)
            sblplayer.equip_soulgem(sg)
    for wep in weapons:
        if wep == selected_weapon:
            item = weapon.Weapon(weapons[wep][0], weapons[wep][1], weapons[wep][2], weapons[wep][3], weapons[wep][4], weapons[wep][5])
            sblplayer.equip_weapon(item)
            break
    return sblplayer

def generate_enemy(enemy_type):
    for enemy in enemies:
        if enemy == enemy_type:
            e = player.Enemy(enemies[enemy][0], enemies[enemy][1], enemies[enemy][2], enemies[enemy][3], enemies[enemy][4], enemies[enemy][5], enemies[enemy][6])
            return e

def hero_death():
    print("Player has been slain!")
    sys.exit(1)

def combat(player, enemy, event="Random Battle", turn_count=1, combat_round=1, turn="p"):
    """While the enemy is alive the player will be engaged in combat."""
    while enemy.hp >= 1:
        if player.hp <= 0:
            hero_death()
        elif enemy.hp >= 1:
            hp = player.get_combat()
            ehp = enemy.get_combat()
            # By default, it is the players turn.
            if turn == "p":
                # Start of turn, prints the round and event type.
                intro = ("{0}\n"
                        "\t\tEvent: {1} || Turn: {2} || Combat Round: {8}\n"
                        "{3}\n"
                        "\t{4}\t\t\t{5}\n"
                        "\t{6}\t\tvs.\t{7}\n").format(border, event, combat_round, border, hp[0], ehp[0], hp[1], ehp[1], combat_round)
                if enemy.hp >= 0:
                    player.attack_menu(enemy, intro)
                    turn = "e"
                    turn_count += 1
                    combat_round += 1
                else:
                    break
            elif turn == "e": # Otherwise its the enemies turn.
                enemy.attack(player)
                turn_count += 1
                turn = "p"
            else:
                print("You just got crit by an error!\nError hits you for 9999 damage!\nYou have died...")
                sys.exit(1)
        elif enemy.hp <= 0:
            #print("{} has been slain!".format(enemy.name))
            loot(player, enemy, event)

def gauntlet(player):
    """The player will have to face a number of enemies in a row without a break."""
    eg = generate_enemy("goblin")
    eo = generate_enemy("orc")
    et = generate_enemy("thug")
    enemy_list = [eg, eo, et]
    count = 1
    for enemy in enemy_list:
        combat(player, enemy, "Gauntlet")
        count += 1

def wander(player, setting="desert"):
    """The player wanders aimlessly, what will be found?"""
    options = [{"q": "quest"}, {"w": "wander"}, {"e": "inventory"}, {"r": "rest"}]
    print("Zone: {0}\n".format(setting))

def explore(player, setting="forest"):
    """What mischief will the adventurer get into here?"""
    while player.hp >= 1:
        if setting == "forest":
            print("\nForest menu options:\nq - walk along path, w - combat, e - inspect yourself, r - rest\na - shop")
            choice = raw_input("\nWhat does {0} do? >> ".format(player.name))
            if choice == "q":
                print("You continue to walk down the forest path. Off in the distance you see various forest creatures running your way!")
                gauntlet(player)
            elif choice == "w":
                combat(player, generate_enemy("goblin"))
            elif choice == "e":
                player.print_advanced()
                player.show_abilities()
                print("Your pack is empty, you look at your weapon and mumble to yourself.")
            elif choice == "r":
                hp_healed = random.randint(player.level, (player.level + player.intelligence))
                print("You rest, and heal {0} hp!".format(hp_healed))
            elif choice == "a":
                shop(player)

def shop(player, setting="kingdom"):
    """Add a shop."""
    print("What do you want to buy?!!/n1. Marbled Spellgem\n2.Nykez Shoes")
    item = ""
    choice = raw_input("\nCHOICE >> ")
    if choice == 2 or choice == "2":
        item  = "shoes"
    print("You bought {}.".format(item))

def loot(player, enemy, event):
    """Based on the enemy loot drops!"""
    gold = 1
    print("\n"+border)
    print("\t\t\t\t  Loot")
    print("{0} drops {1} {2}.".format(enemy.name, gold, gi.loot["currency"][0]))
    print(border)
    player.gold += gold

def main():
    print("Welcome to the Spellblade: Legacy!")
    sblplayer = character_creation()
    #sblplayer.print_advanced()
    #sblplayer.show_abilities()
    #ed = generate_enemy("dragon")
    aa = generate_enemy("mystic")
    combat(sblplayer, aa)
    explore(sblplayer, "forest")

if __name__ == "__main__":
    main()
