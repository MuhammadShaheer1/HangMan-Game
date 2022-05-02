from itertools import count
import random
import time
from typing import Counter

#Initial steps to invite in the game
print("\nWelcome to Hangman Game:\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
    global count 
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play again? Y = Yes, N = No\n")
    while play_game not in ["Y", "N", "y", "n"]:
        play_game = input("Do you want to play again? Y = Yes, N = No\n")
    if play_game == "Y":
        main()
    elif play_game == "N":
        print("Thanks for playing! We expect you back again!")
        exit()

#Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + "Enter Your Guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input! Try a Letter!\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try Another Letter\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("  _____\n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print("_|_ \n")
            print("Wrong Guess. " + str(limit - count) + "Guesses Remaining\n")
        elif count == 2:
            time.sleep(1)
            print("  _____ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print("_|_ \n")
            print("Wrong Guess. " + str(limit - count) + "Guesses Remaining\n")
        elif count == 3:
            time.sleep(1)
            print("  _____ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print("_|_ \n")
            print("Wrong Guess. " + str(limit - count) + "Guesses Remaining\n")
        elif count == 4:
            time.sleep(1)
            print("  _____ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     O\n")
            print(" |      \n")
            print(" |      \n")
            print("_|_ \n")
            print("Wrong Guess. " + str(limit - count) + "Last Guess Remaining\n")
        elif count == 5:
            time.sleep(1)
            print("  _____ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     O\n")
            print(" |    /|\ \n")
            print(" |    / \ \n")
            print("_|_ \n")
            print("Wrong Guess. You are Hanged")
            print("The Word was: ", already_guessed, word)
            play_loop()
    if word == "_" * length:
        print("Congratulations! You have guessed the word correctly")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()



