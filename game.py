word = "Soup"


def make_padding(failed, correct):
    """
    Create a string that is used as padding. The length of this string 
    and the length of the two parameter strings will be the sum 60.
    Example: make_padding("[d]", "_ a _ _ _") returns 54 spaces. 
    """
    padding = " "
    length = 60 - len(failed) - len(correct)
    for i in range(length):
        padding = padding + " "
    return padding


def character_position(string, letter_from_user):
    """
    Returns right position for character
    """
    result = []
    for i in range(len(string)):
        if string[i] == letter_from_user:
            result.append(i)
    return result


def wrong_letter(string, letter_from_user):
    """
   Retuns wrong letter at right position 
    """
    result = []
    for i in range(len(string)):
        if string[i] != letter_from_user:
            result.append(string[i])
            print(string[i])
    return result


def user_input():
    """Create a input field for user to enter a letter.
    Repeats for 8 times.
    """
    failed = ""
    letter_in_word = "_ _ _ _ "
    for i in range(3):
        letter_from_user = input("Type a letter: ")
        failed = failed + "[ " + letter_from_user + " ]"
        correct = correct_hits(letter_in_word, letter_from_user)
        wrong = wrong_letter(word, letter_from_user)
        padding = make_padding(wrong, correct) 
        print(failed + padding + correct + "\n")
        letter_in_word = correct


def correct_hits(correct, letter_from_user):
    """ Place the letter in correct place """
    hits = (character_position(word, letter_from_user))
    for hit in range(len(hits)):
        index = hits[hit] * 2
        correct = correct[:index] + letter_from_user + correct[index + 1:]
    return correct


def main():
    """ Run all program function """
    user_input()


""" Program starts here """
print("Welcome to Classic! \n ")
print("What is the meal of the day? ")
print("You have 8 try's, have fun.\n ")

main()