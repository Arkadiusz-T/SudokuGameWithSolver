import time


class Solver:
    def __init__(self, board, show_algorithm_steps = False):
        self.board = board
        self.board_values = board.get_all_board_values()
        self.number_of_spots_to_fill = 0

    def fill_spot(self, list_of_spots, current_spot_id=0, value=1, show_algorithm_steps=False):

        spot_row = list_of_spots[current_spot_id][0]
        spot_col = list_of_spots[current_spot_id][1]
        self.board.insert_value(spot_row, spot_col, value)
        if show_algorithm_steps:
            time.sleep(1)
            self.board.print_board_to_console()
            print('\n')
        is_value_correct = self.board.check_if_value_pass_rules(spot_row, spot_col)

        if is_value_correct and (current_spot_id + 1) == self.number_of_spots_to_fill:
            if not show_algorithm_steps:
                self.board.print_board_to_console()
                print("This is the solution")

            else:
                print("This is the solution")

        elif is_value_correct:
            self.fill_spot(list_of_spots, current_spot_id=current_spot_id+1, value=1, show_algorithm_steps=show_algorithm_steps)

        elif (not is_value_correct) and value == 9:
            while value == 9:
                self.board.insert_value(spot_row, spot_col, 0)
                if show_algorithm_steps:
                    self.board.print_board_to_console()
                current_spot_id -= 1
                spot_row = list_of_spots[current_spot_id][0]
                spot_col = list_of_spots[current_spot_id][1]
                value = self.board_values[spot_row][spot_col]

            self.fill_spot(list_of_spots, current_spot_id=current_spot_id, value=value+1, show_algorithm_steps=show_algorithm_steps)

        elif not is_value_correct:
            self.fill_spot(list_of_spots, current_spot_id=current_spot_id, value=value + 1, show_algorithm_steps=show_algorithm_steps)

    def solve_sudoku(self, show_algorithm_steps=False):
        # create list of coordinates that must be filled
        mapped_board_constant = list()

        for row in range(9):
            for col in range(9):
                if self.board_values[row][col] == 0:
                    mapped_board_constant.append([row, col])

        self.number_of_spots_to_fill = len(mapped_board_constant)

        # bruteforce values into the board until it is finished
        self.fill_spot(mapped_board_constant, show_algorithm_steps=show_algorithm_steps)

