"""Модуль для игры в крестики нолики."""


class TicTacToe:
    """Класс, который описывает игровое поле."""

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.field_size = 3

    def make_move(self, row, col, move):
        self.board[row][col] = move
        print('Ход сделан!')

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print(' ')
