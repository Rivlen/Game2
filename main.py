from random import randint


def lotto():
    guess_list = []
    while len(guess_list) < 6:
        number = input("Choose a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Not a number!")
            continue

        if number in guess_list:
            continue

        if number < 0 or number > 49:
            continue

        guess_list.append(number)

    guess_list.sort()
    print("Your numbers:", guess_list)

    rolls = []
    while len(rolls) < 6:
        roll = randint(1, 49)
        if roll not in rolls:
            rolls.append(roll)

    rolls.sort()
    print("Lotto numbers:", rolls)

    guessed = 0
    for item in rolls:
        if item in guess_list:
            guessed += 1

    return f"You hit {guessed} numbers!"


if __name__ == '__main__':
    print(lotto())
