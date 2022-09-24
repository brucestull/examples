# Resources:
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_lists_comprehension.asp


# Trying to join:
# Assuming the board state is represented by a list of three sub-lists. The sub-lists are lists of three strings.
the_board_state = [['X', ' ', ' ', ' '], [' ', 'X', ' ', ' '], [' ', ' ', 'X', ' '], [' ', ' ', ' ', 'X']]

# How to stringinfy a list of three things?
# List comprehensions are essentially a for loop:
    # We can loop over `the_board_state` and join the individual elements of sub-lists with pipes.
    # We now have a list of three strings.
the_row_list = ['|'.join(row) for row in the_board_state]
# print('the_row_list: ', the_row_list)
# the_row_list:  ['X| | ', ' |X| ', ' | |X']

# TODO: How to build `the_spacer_line` programmatically?
    # It should depend on the size of the sub-lists.
    # 1. Create N-length list of `-` strings.
    # 2. Join that list with ` `.

n = len(the_board_state[0])
n_length_dashes_list = ['-' for _ in range(n) ]
# print('n_length_dashes_list: ', n_length_dashes_list)
# n_length_dashes_list:  ['-', '-', '-']

n_length_dashes_list_with_spaces = ' '.join(n_length_dashes_list)
# print('n_length_dashes_list_with_spaces: ', n_length_dashes_list_with_spaces)
# n_length_dashes_list_with_spaces:  - - -

# the_spacer_line = '- - -'
the_spacer_line = ' '.join(n_length_dashes_list)
a_line_break = '\n'


the_spacer_line_with_line_breaks = a_line_break + the_spacer_line + a_line_break


the_board_string_we_display = the_spacer_line_with_line_breaks.join(the_row_list)
print('the_board_string_we_display: ')
print(the_board_string_we_display)
# the_board_string_we_display: 
# X| | | 
# - - -
#  |X| |
# - - -
#  | |X|
# - - -
#  | | |X
