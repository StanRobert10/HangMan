import random
from os import system
from ArtWork import stages, logo
from WordList import word_list

word = random.choice(word_list)
word = list(word)
letters_used = []
censured_word = []
lives = 6

for i in range(0, len(word)):
    censured_word.append('_')

censured_word = ''.join(censured_word)
game_in_progress = True

while game_in_progress:
    if "_" not in censured_word:
        print(logo)
        print("Yow Won! Congratulations!!!")
        break

    print(logo)
    print(stages[lives])
    print(censured_word)
    print(word)
    letter = input("Chose a letter! ")

    if letter in letters_used:
        system("cls")
        print("This letter was already verified!")
        continue

    letters_used.append(letter)
    censured_word = list(censured_word)

    if letter in word:
        for index in range(0, len(word)):
            if letter in word[index]:
                censured_word[index] = word[index]
    else:
        lives -= 1

    if lives:
        system('cls')
    else:
        system('cls')
        print(logo)
        print(stages[lives])
        print("Game Over!")
        game_in_progress = False
    censured_word = ''.join(censured_word)
