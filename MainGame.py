from live import load_game, welcome
from GuessGame import play
from MemoryGame import play2
from CurrencyRouletteGame import play3

welcome()
game, diff = load_game()
play(game, diff)
play2(game, diff)
play3(game, diff)
