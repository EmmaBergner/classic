word = "SOUP"


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
    Check if letter_from_user is in string.
    Return a list of the positions (might be empty). 
    Example: string = "Soup", letter_from_user = "o" returns on position 2.
    """
    result = []
    for i in range(len(string)):
        if string[i] == letter_from_user:
            result.append(i)
    return result


def correct_hits(correct, letter_from_user):
    """ Place letter_from_user from letter_in_word in correct place in list.
    Example: _ _ _ _ , "o" 
    """
    hits = (character_position(word, letter_from_user))
    for hit in range(len(hits)):
        index = hits[hit] * 2
        correct = correct[:index] + letter_from_user + correct[index + 1:]
    return correct


def main():
    """ Run the program """
    failed = ""
    letter_in_word = "_ _ _ _ "
    for i in range(6):
        letter_from_user = input("Type a letter: ")
        letter_from_user = letter_from_user.capitalize()
        if letter_from_user not in word:
            failed = failed + "[ " + letter_from_user + " ]"
        correct = correct_hits(letter_in_word, letter_from_user)
        padding = make_padding(failed, correct) 
        print(failed + padding + correct + "\n")
        letter_in_word = correct
        if "_" not in word: 
            break
    print("The meal of the day is " + word.lower())


""" Program starts here """
print("Welcome to Classic! \n ")
print("What is the meal of the day? ")
print("You have 8 try's, have fun.\n ")

main()