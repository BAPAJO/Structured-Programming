# modules
import random

# menu prompt
print("HANGMAN")
print("Type 1 to play")
menu = int(input())
if menu == 1:
    # theme menu
    print("1. Animals")
    print("2. Countries")
    print("Type the corresponding number to choose the theme")
    theme = input(int())
    # Animals theme
    if theme == 1:
        print("""
    +---+
    |   |
        |
        |
        |
        |
    =========
        """)
        # open file
        animal_file = open("AnimalList", "r")
        word1 = animal_file.readlines()
        A_word = random.choice(word1)
        
        

# note: make the hangman drawing a txt file
