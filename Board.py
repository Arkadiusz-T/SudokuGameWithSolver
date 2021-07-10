class Board:
    def __init__(self, list_of_values):
        self.__playing_board = list_of_values

    def insert_value(self, row, col, val):
        try:
            self.__playing_board[row][col] = val

        except IndexError as e:
            print('Could not insert the value, \n'
                  'check if coordinates for the insert are correct')

    def check_if_value_pass_rules(self, row_nr, col_nr):
        row = [x for x in self.__playing_board[row_nr] if x != 0]
        if len(row) != len(set(row)):
            return False

        col = [x[col_nr] for x in self.__playing_board if x[col_nr] != 0]
        if len(col) != len(set(col)):
            return False

        if row_nr < 3:
            box_rows = [0, 1, 2]

        elif 2 < row_nr < 6:
            box_rows = [3, 4, 5]

        else:
            box_rows = [6, 7, 8]

        if col_nr < 3:
            box_cols = [0, 1, 2]

        elif 2 < col_nr < 6:
            box_cols = [3, 4, 5]

        else:
            box_cols = [6, 7, 8]

        box_numbers = list()
        for row in box_rows:
            for col in box_cols:
                box_numbers.append(self.__playing_board[row][col])

        box_numbers = [x for x in box_numbers if x != 0]
        if len(box_numbers) != len(set(box_numbers)):
            return False

        return True

    def get_all_board_values(self):
        return self.__playing_board

    def print_board_to_console(self):
        i = 0
        for row in self.__playing_board:
            i += 1
            print('{} {} {} | {} {} {} | {} {} {}'.format(
                  row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            if i == 3 or i == 6:
                print('---------------------')

        print('\n')
