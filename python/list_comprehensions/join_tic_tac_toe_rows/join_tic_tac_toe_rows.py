# Current board state:
the_board_state = [
    ['X', ' ', ' ', ' '],
    [' ', 'X', ' ', ' '],
    [' ', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X']
]

# A constant for the '|':
THE_PIPE = '|'

# Create a list of strings from the board state:
token_row_list = [THE_PIPE.join(row) for row in the_board_state]

# Get the length of sub-lists:
n = len(the_board_state[0])

# A constant for the '-':
THE_DASH = '-'

# Create list of dashes:
n_length_dashes_list = [THE_DASH for _ in range(n)]

# A constant for the ' ':
A_SPACE = ' '

# Create a string of dashes and spaces for between rows:
n_length_spacer_string = A_SPACE.join(n_length_dashes_list)

# A constant for the '\n':
A_LINE_BREAK = '\n'

# Build the string to be placed between token rows:
n_length_spacer_string_with_line_breaks = A_LINE_BREAK + n_length_spacer_string + A_LINE_BREAK

# Build the board from spacer lines and token rows:
the_board_string_we_display = n_length_spacer_string_with_line_breaks.join(token_row_list)
print('the_board_string_we_display: ')
print(the_board_string_we_display)
