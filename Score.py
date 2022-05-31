from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(diff):
    point_of_winning = (int(diff) * 3) + 5
    print(f'\nYour score is: {point_of_winning}')


