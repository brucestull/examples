# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://www.w3schools.com/python/ref_random_choice.asp


import pprint
import random

# Current board state:
the_board_state = [
    ['X', ' ', ' ', ' '],
    [' ', 'X', ' ', ' '],
    [' ', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X']
]

# pprint.pprint(the_board_state)
"""
[['X', ' ', ' ', ' '],
 [' ', 'X', ' ', ' '],
 [' ', ' ', 'X', ' '],
 [' ', ' ', ' ', 'X']]
"""



"""
N = 4
a_row = [index for index in range(N)]
print(a_row)
"""
# [0, 1, 2, 3]



"""
N = 4
token = 'X'
a_row = [token for _ in range(N)]
print(a_row)
"""
# ['X', 'X', 'X', 'X']



"""
N = 4

def token():
    token = random.choice(' ', 'X')
    return token

a_row = [token for _ in range(N)]
print(a_row)
pprint.pprint(a_row)
"""
# [<function token at 0x000002E4B8CA4040>,
#  <function token at 0x000002E4B8CA4040>,
#  <function token at 0x000002E4B8CA4040>,
#  <function token at 0x000002E4B8CA4040>]



"""
N = 4
def token():
    token = random.choice(' ', 'X')
    return token

a_row = [token() for _ in range(N)]
print(a_row)
"""
# PS C:\Users\Bruce\Programming\examples\python\list_comprehensions\join_tic_tac_toe_rows> python .\build_the_board.py
# Traceback (most recent call last):
#   File "C:\Users\Bruce\Programming\examples\python\list_comprehensions\join_tic_tac_toe_rows\build_the_board.py", line 54, in <module>
#     a_row = [token() for _ in range(N)]
#   File "C:\Users\Bruce\Programming\examples\python\list_comprehensions\join_tic_tac_toe_rows\build_the_board.py", line 54, in <listcomp>
#     a_row = [token() for _ in range(N)]
#   File "C:\Users\Bruce\Programming\examples\python\list_comprehensions\join_tic_tac_toe_rows\build_the_board.py", line 42, in token
#     token = random.choice(' ', 'X')
# TypeError: Random.choice() takes 2 positional arguments but 3 were given
# PS C:\Users\Bruce\Programming\examples\python\list_comprehensions\join_tic_tac_toe_rows>



'''
N = 4

def return_token_or_space():
    """
    Returns a random single-character token from the list [' ', 'X'].
    """
    random_string = random.choice([' ', 'X'])
    return random_string

a_row = [return_token_or_space() for _ in range(N)]
print(a_row)
'''
# [' ', ' ', 'X', ' ']
# [' ', ' ', ' ', 'X']
# [' ', ' ', ' ', ' ']
# ['X', ' ', ' ', 'X']
# ['X', ' ', 'X', ' ']
# ['X', 'X', ' ', 'X']



n = 4
m = 6

SINGLE_SPACE = ' '
ASTERISK = '*'
user_token = 'R'


def return_token_or_space(empty_space_char, token):
    """
    Returns a random single-character token from the list [empty_space_char, token].
    """
    random_string = random.choice([empty_space_char, token])
    return random_string


def build_a_row(row_length):
    the_row = [return_token_or_space(SINGLE_SPACE, user_token) for _ in range(row_length)]
    return the_row


def build_a_board(row_length, column_length):
    board = [build_a_row(row_length) for _ in range(column_length)]
    return board


the_actual_board = build_a_board(n, m)
pprint.pprint(the_actual_board)
# [[' ', 'R', ' ', ' '],
#  ['R', 'R', ' ', ' '],
#  [' ', ' ', 'R', 'R'],
#  ['R', ' ', ' ', 'R'],
#  [' ', 'R', ' ', 'R'],
#  ['R', 'R', 'R', ' ']]