class Game:
    def __init__(self, board):
        self.board = board
        self.board_values = board.get_all_board_values()
        self.mapped_board_constant = list()

        for row in range(9):
            for col in range(9):
                if self.board_values[row][col] == 0:
                    self.mapped_board_constant.append([row, col])

    def play(self):
        self.board.print_board_to_console()
        run_game = True
        while run_game:
            print("Please enter row number(1-9): ")
            try:
                row_number = int(input()) - 1
                print("Please enter column number(1-9): ")
                col_number = int(input()) - 1
                print("Please enter value: ")
                value = int(input())
                if value > 9:
                    print("Only values from range 1 to 9 are allowed :)")
                    continue
            except ValueError as e:
                print("Invalid input try again")
                continue

            if [row_number, col_number] not in self.mapped_board_constant:
                print("This value is constant try again")
                continue

            self.board.insert_value(row_number, col_number, value)
            self.board.print_board_to_console()
            if self.board.check_if_value_pass_rules(row_number, col_number):
                if self.check_if_all_spots_are_filled():
                    run_game = False
                    print("Congratulation you won!!!")

    def check_if_all_spots_are_filled(self):
        board_values = self.board.get_all_board_values()
        for row in board_values:
            for cell in row:
                if cell == 0:
                    return False

        return True
