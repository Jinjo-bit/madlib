import random as r


def madlib_game():
    noun1 = input("a type of animal: ")
    verb1 = input("Give me verb: ")
    adjective1 = input("give me an adjective: ")
    noun2 = input("give me a verb: ")
    verb2 = input("Give me a verb: ")

    madlib1 = (
        f"Madlib 1 story... {noun1}, {verb1}, {adjective1}, {noun2}, {verb2}")
    madlib2 = (
        f"Madlib 1 story... {noun1}, {verb1}, {adjective1}, {noun2}, {verb2}")
    madlib3 = (
        f"Madlib 1 story... {noun1}, {verb1}, {adjective1}, {noun2}, {verb2}")

    randomNumber = r.randint(1, 3)

    print(randomNumber)

    if randomNumber <= 1:
        print(madlib1)
    elif randomNumber <= 2:
        print(madlib2)
    else:
        print(madlib3)

madlib_game
