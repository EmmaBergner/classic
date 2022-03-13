space = "_ _ _ _"
word = "Emma"


def charposition(string, letter_from_user):
    """
    Returns right position of a character from a string
    """
    result = []
    for i in range(len(string)):
        if string[i] == letter_from_user:
            result.append(i)
    return result


for round in range(3):
    letter_from_user = input("Type a letter: ")
    hits = (charposition(word, letter_from_user))
    for hit in range(len(hits)):
        index = charposition(word, letter_from_user)[hit] * 2
        space = space[:index] + letter_from_user + space[index + 1:]
    print(space)
    print(str(round) + "/8 rounds ")

