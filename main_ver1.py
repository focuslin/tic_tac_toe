def winner(matrix):
    winner_list = []
    winner_patterns = [[matrix[0], matrix[1], matrix[2]],
                       [matrix[3], matrix[4], matrix[5]],
                       [matrix[6], matrix[7], matrix[8]],
                       [matrix[0], matrix[3], matrix[6]],
                       [matrix[1], matrix[4], matrix[7]],
                       [matrix[2], matrix[5], matrix[8]],
                       [matrix[0], matrix[4], matrix[8]],
                       [matrix[2], matrix[4], matrix[6]]]

    # 'X' case
    if ['X', 'X', 'X'] in winner_patterns:
        winner_list.append('x')

    # 'O' case
    if ['O', 'O', 'O'] in winner_patterns:
        winner_list.append('o')

    if len(winner_list) == 2:
        return 'ox'
    else:
        return winner_list


def print_matrix(cell_str):
    print(f"---------\n"
          f"| {cell_str[0]} {cell_str[1]} {cell_str[2]} |\n"
          f"| {cell_str[3]} {cell_str[4]} {cell_str[5]} |\n"
          f"| {cell_str[6]} {cell_str[7]} {cell_str[8]} |\n"
          f"---------")


if __name__ == '__main__':
    # write your code here
    input_str = input("Enter cells: ")
    print_matrix(input_str)

    while True:
        coordinates = input("Enter the coordinates: ")
        illegal_xy = False
        for s_str in coordinates.split():
            if not s_str.isnumeric():
                illegal_xy = True
                break
        if illegal_xy:
            print("You should enter numbers!")
            continue

        x_cell_row, x_cell_col = coordinates.split()
        x_index = (int(x_cell_row) - 1) * 3 + int(x_cell_col) - 1
        if not (0 < int(x_cell_row) <= 3 and 0 < int(x_cell_col) <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if input_str[x_index] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            input_str = input_str[:x_index] + 'X' + input_str[(x_index + 1):]
            print_matrix(input_str)
            break

    count_x = input_str.count('X')
    count_o = input_str.count('O')
    empty_cells = 9 - count_x - count_o
    game_result = winner(input_str)
    if 2 <= abs(count_x - count_o) or game_result == 'ox':
        print("Impossible")
    elif len(game_result) == 0 and not empty_cells:
        print("Draw")
    elif game_result == ['x']:
        print("X wins")
    elif game_result == ['o']:
        print("O wins")
    else:
        print("Game not finished")

