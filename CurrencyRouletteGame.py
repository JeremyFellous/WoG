import random
from currency_converter import CurrencyConverter


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_money_interval():
    number = random.randint(1, 100)
    print(number)
    c = CurrencyConverter()
    num_converted = c.convert(number, 'USD', 'ILS')
    return num_converted


def get_guess_from_user():
    print("What do you think is the value of the generated number from USD to ILS?")
    ok = False
    num = 0
    while not ok:
        user_number = input('Enter Your answer: ')
        if not is_number(user_number):
            print("You must guess a number, please try again...")
        else:
            ok = True
    return user_number


def play3(diff):
    print("Welcome to the Currency Roulette Game.\n"
          "In this game the computer will generate an amount of USD between 1 to 100.\n"
          "You need to enter the value of this generated amount in ILS.")
    num_converted = get_money_interval()
    user_number = float(get_guess_from_user())
    if (num_converted - (5 - diff)) < user_number < (num_converted + (5 - diff)):
        print(f'You WON! \nThe number is: {num_converted}')
        return True
    else:
        print(f' You Lost.\nThe number is: {num_converted}')
        return False
