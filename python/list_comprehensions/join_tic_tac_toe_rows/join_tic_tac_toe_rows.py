
the_board_state = [
    ['X', ' ', ' ', ' '],
    [' ', 'X', ' ', ' '],
    [' ', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X']
]

THE_PIPE = '|'

the_list_of_row_strings = [THE_PIPE.join(row) for row in the_board_state]

n = len(the_board_state[0])

THE_DASH = '-'

n_length_dashes_list = [THE_DASH for _ in range(n)]

A_SPACE = ' '

n_length_dashes_list_with_spaces = A_SPACE.join(n_length_dashes_list)

the_spacer_line = A_SPACE.join(n_length_dashes_list)

A_LINE_BREAK = '\n'

the_spacer_line_with_line_breaks = A_LINE_BREAK + the_spacer_line + A_LINE_BREAK


the_board_string_we_display = the_spacer_line_with_line_breaks.join(the_list_of_row_strings)
print('the_board_string_we_display: ')
print(the_board_string_we_display)
