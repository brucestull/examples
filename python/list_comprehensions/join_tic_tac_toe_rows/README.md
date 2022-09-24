# Join the Rows of an N by M Tic-Tac-Toe Board

## Resources:
* https://www.w3schools.com/python/python_ref_string.asp
* https://www.w3schools.com/python/python_lists_comprehension.asp
* https://www.w3schools.com/python/ref_func_len.asp

## The Code:
* [`join_tic_tac_toe_rows.py`](./join_tic_tac_toe_rows.py)
## Process:

1. Note current board state:
    * An M by N matrix:
        * List of length M
        * Sub-lists of length N
        ```
        the_board_state = [['X', ' ', ' ', ' '], [' ', 'X', ' ', ' '], [' ', ' ', 'X', ' '], [' ', ' ', ' ', 'X']]

        ```

1. Create a pipe constant `THE_PIPE`:
    ```
    THE_PIPE = '|'
    ```

1. Use list comprehension to join the elements of each of the rows (sub-lists in `the_board_state` list) to themselves:
    ```
    the_row_list = ['|'.join(row) for row in the_board_state]
    ```

1. Create a variable for the length of the same-length sub-lists:
    ```
    n = len(the_board_state[0])
    ```

1. Create a list of `-` (dashes). One dash for each element of the sub-lists. These will be used as spacers between the rows:
    ```
    n_length_dashes_list = ['-' for _ in range(n)]
    ```

1. Create a constant `A_SPACE` to hold the thing which will be between the dashes:
    ```
    A_SPACE = ' '
    ```

1. Add spaces (A_SPACE) between the dashes since those spaces will be occupied by pipes in the above and below rows:
    ```
    n_length_dashes_list_with_spaces = A_SPACE.join(n_length_dashes_list)
    ```

1. Create a `the_spacer_line` string out of `n_length_dashes_list` by joining with `A_SPACE`s:
    ```
    the_spacer_line = A_SPACE.join(n_length_dashes_list)
    ```

1. Define a line break constant `A_LINE_BREAK`:
    ```
    A_LINE_BREAK = '\n'
    ```

1. Build the separator line by putting line breaks `A_LINE_BREAK`s on each side of the string `the_spacer_line`:
    ```
    the_spacer_line_with_line_breaks = A_LINE_BREAK + the_spacer_line + A_LINE_BREAK
    ```

1. Create the board string `the_board_string_we_display` by joining the `the_row_list` list with `the_spacer_line_with_line_breaks` strings:
    ```
    the_board_string_we_display = the_spacer_line_with_line_breaks.join(the_row_list)
    ```

1. Sample output:
    ```
    X| | | 
    - - - -
     |X| |
    - - - -
     | |X|
    - - - -
     | | |X
    ```