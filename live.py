from games.GuessGame import play2
from games.MemoryGame import play
from games.CurrencyRouletteGame import play3
from WoG.score.Score import add_score


def welcome():
    name = str(input('Enter your name:'))
    print(f'\nHello {name} and welcome to the World of Game (WoG).\n Here you can find many cool games to play.')


def load_game():
    game = 0
    diff = 0
    print('Please choose a game to play:\n'
          '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
          '2. Guess Game - guess a number and see if you chose like the computer\n'
          '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    ok = False
    while not ok:
        game = input('Enter the game number you want to play: ')
        x = game.isnumeric()
        if not x:
            print('\nYou must choose a number, please try again...')
        elif int(game) not in range(1, 4):
            print('\nGame number is not in range, please try again...')
        else:
            ok = True
    ok = False
    while not ok:
        diff = input('Please choose game difficulty from 1 to 5:')
        x = diff.isnumeric()
        if not x:
            print('\nYou must choose a number, please try again...')
        elif int(diff) not in range(1, 6):
            print('\nGame number is not in range, please try again...')
        else:
            ok = True
    if int(game) == 1:
        score = play(int(diff))
    elif int(game) == 2:
        score = play2(int(diff))
    elif int(game) == 3:
        score = play3(int(diff))
    if score:
        add_score(diff)
