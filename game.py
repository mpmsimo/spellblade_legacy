"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon
import sword
import player

def character_creation():
    """Choose a character name"""
    print("Welcome to the Spellblade: Legacy!")
    player_name = name_character()
    soulgem = choose_soulgem()

def name_character():
    """Renames the player"""
    player_name = input("Please choose a name for your character: ")
    return player_name
    #return str(player_name)

def choose_soulgem():
    """Soulgem choice"""
    print("Select a member of the Order of the Spellblade you would like to embody.")
    print("1. Althea [Fighter, Strength]\n"
            "Ability: Crushing Strike\n"
            "Passive: Intelligence is added to strength for damage rolls\n"
            "400 HP, 6 STR, 4 DEX, 2 INT")
    return "Althea"

def main():
    character_creation()
    #def __init__(self, max_hp, name, level, exp, max_exp, strength, dexterity, magic):
    althea = player.Player(100, "Althea", 10, 1337, 2048, 0, 0, 0)
    althea.print_stats()
    #longsword = sword.Sword("Longsword", "Main Hand", "Strength", 10, {"strength": 10, "dexterity": 4, "intelligence":1}, {"sg1": "Pierce", "sg2": "Power", "sg3": "Lament")
    #longsword = weapon.Weapon("Longsword", "Main Hand", "Strength", 10, {"strength": 10, "dexterity": 4, "intelligence":1}, {"sg1": "Pierce", "sg2": "Power", "sg3": "Lament"})
    longsword = weapon.Weapon("Longsword", "Main Hand", "Sword", 10, 1, "Sweeping Strike")
    longsword.print_weapon()
    #althea.equip_weapon(longsword)

    althea.print_stats()

if __name__ == "__main__":
    main()
