import random


def make_up_word():
    """
    Pick one random word from list in word.txt-file.
    """
    with open('word.txt') as f:
        list_of_words = f.readlines()
    return random.choice(list_of_words).upper().strip()


def correct_underscore(size):
    """
    Match correct_underscore lines with size of the random word.
    Exampel: correct_underscore(6) returns "_ _ _ _ _ _".
    """
    result = "_"
    for i in range(size-1):
        result = result + " _"
    return result


def make_padding(failed, correct):
    """
    Create a string that is used as padding. The length of this string
    and the length of the two parameter strings will be the sum 60.
    Example: make_padding("[D]", "_ A _ _ _") returns 59 spaces.
    """
    padding = " "
    length = 65 - len(failed) - len(correct)
    for i in range(length):
        padding = padding + " "
    return padding


def character_position(string, letter_from_user):
    """
    Check if letter_from_user is in string.
    Return a list of the positions (might be empty).
    Example: character_position("SOUP", "O") returns  "_ O _ _"
    """
    result = []
    for i in range(len(string)):
        if string[i] == letter_from_user:
            result.append(i)
    return result


def correct_hits(word, correct, letter_from_user):
    """ Place letter_from_user from correct in correct place in list.
    Example: correct_hits("PIZZA", "_ _ _ _ _", "Z") returns "_ _ Z Z _"
    """
    hits = (character_position(word, letter_from_user))
    for hit in range(len(hits)):
        index = hits[hit] * 2
        correct = correct[:index] + letter_from_user + correct[index + 1:]
    return correct


def error_handling(letter_from_user, failed, correct):
    """ Checks if letter_from_user is:
    More then one letter, a number, existing in failed and correct list.
    Prints out error-message to user.
    Exampel: error_handling("E", ["E"], "E") return 
    """
    if not letter_from_user.isalpha():
        print("Ops, you entered a number ")
        return False
    if letter_from_user in failed + correct:
        print("Ops, you already entered this letter ")
        return False
    if not len(letter_from_user) == 1:
        print("Ops, you entered more the one letter ")
        return False
    return True


def input_from_user(failed, correct):
    """
    Print out "Type a letter". Convert letters to capitalize.
    Exampel: input_from_user(["A"], "A")
    """
    done = False
    while not done:
        letter_from_user = input("Type a letter: ").capitalize()
        done = error_handling(letter_from_user, failed, correct)
    return letter_from_user


def main():
    """ Run the program """
    word = make_up_word()
    failed = ""
    correct = correct_underscore(len(word))
    for round in range(10):
        print("Round " + str(round+1) + " of 10 ")
        letter_from_user = input_from_user(failed, correct)
        if letter_from_user not in word:
            failed = failed + "[ " + letter_from_user + " ]"
        correct = correct_hits(word, correct, letter_from_user)
        padding = make_padding(failed, correct)
        print(failed + padding + correct + "\n")
        if "_" not in correct:
            print("Congrats! ")
            print("Well done!! ")
            break
    print("The meal of the day is: " + word + " \n ")


""" Program starts here """
print("\nWelcome to Classic! \n ")
print("What is the meal of the day? ")
print("You have 10 tries to guess the correct word.")
print("Have fun!\n ")

main()