import random


def generate_word(max_length_of_the_word):
    """ method to generate random words using lowercase english characters...
        - the method takes an input, integer number that refers to maximum length of the generated word !
     """

    letters_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    word = ""
    for i in range(random.randint(2, int(max_length_of_the_word))):
        word = word + random.choice(letters_list)
    return word


def hangman():
    """ hangman method that takes the generated word "generated by generate_word()"
        and waits for yor guesses to match the saved word.
    """

    # the next two lines are optional to test the logic of the method...
    # word = random.choice(
    #     ["word1", "word 2", "word_3", "word4"])

    word = generate_word(input("Enter maximum length of the word to be guessed !\n"))
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


def main():
    name = input("Enter your name\n")
    print("Welcomeو ", name)
    print("-------------------")
    print("try to guess the word in less than 10 attempts\n")
    hangman()
    print()


main()
