from gameparts import TicTacToe
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = TicTacToe()
    # Первыми ходят крестики.
    current_player = 'X'
    # Флаг, что игра запущена.
    running = True
    game.display()
    # Тут пользователь вводит координаты ячейки.
    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print('Пожалуйста, введите значения для строки '
                      'и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Пожалуйста, введите значения для строки '
                      'и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки '
                      'и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        # В метод make_move передаются те координаты,
        # которые ввёл пользователь.
        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            print(f'Победили {current_player}')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
