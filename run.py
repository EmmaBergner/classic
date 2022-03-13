

def user_input():
    """
    Ask user for a letter, prints out letter from user.
    Repeats for 8 times. 
    """
    failed = ""
    for i in range(3):
        new_letter = input("Type a letter: ")
        failed = failed + "[ " + new_letter + " ]"
        correct = "_ _ _ a _"
        padding = make_padding(failed, correct)
        print(failed + padding + correct + "\n") 


def make_padding(failed, correct):
    """
    Create a string that can be used as padding. The sum of the 
    length of this string and the length of the two
    parameter strings will be 30.
    Example: make_padding("[d]", "_a_") returns 24 spaces 
    """
    padding = ""
    length = 30 - len(failed) - len(correct)
    for i in range(length):
        padding = padding + " "
    return padding


def main():
    """Run all program function"""
    user_input()


""" Program starts here """
print("Welcome to Classic! \n ")
print("What is the meal of the day? ")
print("You have 8 try's, have fun.\n ")
main()