from Board import Board
from Solver import Solver
from Game import Game


print("For solver demo enter 1 for game demo enter 0")
option = input()
if option == '1':
    initial_values_1 = [
        [0, 2, 0, 4, 5, 6, 7, 8, 9],
        [4, 5, 7, 0, 8, 0, 2, 3, 6],
        [6, 8, 9, 2, 3, 7, 0, 4, 0],
        [0, 0, 5, 3, 6, 2, 9, 7, 4],
        [2, 7, 4, 0, 9, 0, 6, 5, 3],
        [3, 9, 6, 5, 7, 4, 8, 0, 0],
        [0, 4, 0, 6, 1, 8, 3, 9, 7],
        [7, 6, 1, 0, 4, 0, 5, 2, 8],
        [9, 3, 8, 7, 2, 5, 0, 6, 0]
    ]

    board_1 = Board(initial_values_1)
    board_1.print_board_to_console()

    solver = Solver(board_1)

    solver.solve_sudoku(show_algorithm_steps=True)

elif option == '0':
    initial_values_2 = [
        [8, 7, 5, 9, 0, 0, 0, 4, 6],
        [0, 6, 0, 7, 5, 4, 8, 9, 0],
        [0, 4, 9, 8, 6, 0, 7, 0, 5],
        [5, 8, 0, 6, 9, 7, 0, 0, 0],
        [7, 0, 3, 0, 0, 8, 6, 2, 9],
        [9, 0, 6, 1, 0, 5, 0, 8, 7],
        [6, 9, 7, 0, 0, 0, 5, 0, 8],
        [0, 5, 8, 0, 7, 9, 0, 6, 0],
        [0, 0, 0, 5, 8, 0, 9, 7, 0]
    ]

    initial_values_3 = [
        [0, 7, 5, 9, 2, 1, 3, 4, 6],
        [3, 6, 1, 7, 5, 4, 8, 9, 2],
        [2, 4, 9, 8, 6, 3, 7, 1, 5],
        [5, 8, 4, 6, 9, 7, 1, 2, 3],
        [7, 1, 3, 2, 4, 8, 6, 5, 9],
        [9, 2, 6, 1, 3, 5, 4, 8, 7],
        [6, 9, 7, 4, 1, 2, 5, 3, 8],
        [1, 5, 8, 3, 7, 9, 2, 6, 4],
        [4, 3, 2, 5, 8, 6, 9, 7, 0]
    ]

    board_2 = Board(initial_values_2)
    board_3 = Board(initial_values_3)
    game = Game(board_3)
    game.play()
else:
    print('Invalid input run demo again')
