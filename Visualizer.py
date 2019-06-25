# import pygame
import Board


def visualizer(b: Board) -> None:
    """
    Converts the board's list of list to text representation of the board.
    :param board:
    :return:
    """
    # pygame.init()
    #
    # window = pygame.display.set_mode((800, 600))
    # pygame.display.set_caption('TIC-TAC-TOE')
    #
    #
    # pygame.quit()
    board = visualizer_helper(b)

    display = (f'{board[0][0]} | {board[0][1]} | {board[0][2]} \n' +
               '---------\n'
               f'{board[1][0]} | {board[1][1]} | {board[1][2]} \n' +
               '---------\n'
               f'{board[2][0]} | {board[2][1]} | {board[2][2]} \n')

    print(display)


def visualizer_helper(b: Board) -> list:
    board = []
    for row in b.board:
        board_row = []
        for char in row:
            if char is None:
                board_row.append(' ')
            else:
                board_row.append(char)
        board.append(board_row)
    return board
