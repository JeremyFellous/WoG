import random


def generate_number(diff):
    print("Welcome to GuessGame, in this game you need to guess the random number we choose.\n"
          "The chosen number will be between 1 to the difficulty level you selected + 2.\n"
          "For example: if you selected difficulty level 2, the number could be between 1 to 4 etc..\n")
    secret_number = random.randint(1, diff + 2)
    return secret_number


def get_guess_from_user(diff):
    print(f'You chose difficulty level #{diff},\n'
          f'so the number we chose is between 1 and {diff + 2}.\n')
    ok = False
    num = 0
    while not ok:
        num = input('please enter your guess: \n')
        x = num.isnumeric()
        if not x:
            print("You must guess a number, please try again...")
        elif int(num) not in range(1, diff + 3):
            print(f'You must guess a number in range: between 1 to {diff + 2}, please try again...')
        else:
            ok = True
    return num


def compare_result(a, b):
    return int(b) == a


def play(game, diff):
    if int(game) == 2:
        generated = generate_number(diff)
        guess = get_guess_from_user(diff)
        solution = compare_result(generated, guess)
        if solution:
            print("You WON!!")
        else:
            print(f'You Lost\nThe number was: {generated}')
