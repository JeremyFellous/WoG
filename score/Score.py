from WoG.Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from genericpath import exists
import os
# from MainScores import


def get_score():
    exist = os.path.isfile(SCORES_FILE_NAME)
    if exist:
        with open(SCORES_FILE_NAME, 'r') as f:
            return f.read()
    else:
        return BAD_RETURN_CODE


def add_score(diff):
    point_of_winning = (int(diff) * 3) + 5
    print(f'\nYour score from this game is: {point_of_winning}')
    my_score = get_score()
    if my_score == BAD_RETURN_CODE:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(point_of_winning))
            print(f'\nYour total score is {point_of_winning}')
    else:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(point_of_winning + int(my_score)))
            print(f'\nYour total score is: {point_of_winning + int(my_score)}')

