"""
game.py - This is where objects are created and the game is played.
msimo - 2/21/2015

Python 3.3.6
"""
import weapon, player

def main():
	#def __init__(self, max_hp, name, level, exp, max_exp, strength, dexterity, magic):
	althea = player.Player(100, "Althea", 10, 1337, 2048, 7, 4, 10)
	althea.print_stats()

if __name__ == "__main__":
    main()
