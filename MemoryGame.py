import random
import time


def generate_sequence(diff):
    random_list = []
    for i in range(0, diff):
        n = random.randint(1, 101)
        random_list.append(n)
    print(random_list, end="")
    time.sleep(0.7)
    print(end="\r")
    print(" ")
    return random_list


def get_list_from_user(diff):
    print("Enter the numbers the computer has presented in the right order: ")
    numbers = []
    for i in range(0, diff):
        numbers.append(int(input()))
    print(numbers)
    return numbers


def is_list_equal(a, b):
    return a == b


def play2(game, diff):
    if int(game) == 1:
        print("Welcome to the MemoryGame, in this game the computer will show you some numbers for"
              " 0.7 sec\nYou need to memorise them and then write them in the correct order.\n"
              "Are you ready?\nThe numbers is:")
        time.sleep(10)
        random_list = generate_sequence(diff)
        numbers = get_list_from_user(diff)
        solution = is_list_equal(random_list, numbers)
        if solution:
            print("You WON!!")
        else:
            print(f'You Lost\nThe numbers list was: {random_list}')

