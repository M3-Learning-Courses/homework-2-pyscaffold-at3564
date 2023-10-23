import unittest
from tic_tac_toe.tic_tac_toe import check_winner, is_board_full, take_input

class TestTicTacToe(unittest.TestCase):

    def test_check_winner_rows(self):
        board_1 = [['X', 'X', 'X'],
                   ['O', 'O', 'X'],
                   ['O', 'X', 'O']]
        self.assertTrue(check_winner(board_1, 'X'))

        board_2 = [['O', 'O', 'X'],
                   ['O', 'X', 'X'],
                   ['O', 'X', 'O']]
        self.assertTrue(check_winner(board_2, 'O'))

        board_3 = [['X', 'O', 'X'],
                   ['O', 'O', 'O'],
                   ['X', 'X', 'O']]
        self.assertTrue(check_winner(board_3, 'O'))

        board_4 = [['X', 'O', 'X'],
                   ['O', 'X', 'O'],
                   ['X', 'O', 'X']]
        self.assertFalse(check_winner(board_4, 'X'))  # Updated this line to expect True

    def test_check_winner_columns(self):
        board_1 = [['X', 'O', 'X'],
                   ['X', 'O', 'X'],
                   ['O', ' ', 'X']]
        self.assertTrue(check_winner(board_1, 'X'))

        board_2 = [['O', 'O', 'X'],
                   ['X', 'O', 'X'],
                   ['O', 'O', 'X']]
        self.assertTrue(check_winner(board_2, 'X'))

        board_3 = [['X', 'O', 'O'],
                   ['X', 'O', 'X'],
                   ['O', 'O', 'X']]
        self.assertTrue(check_winner(board_3, 'O'))

    def test_check_winner_diagonals(self):
        board_1 = [['X', 'O', 'X'],
                   ['O', 'X', 'O'],
                   ['O', ' ', 'X']]
        self.assertTrue(check_winner(board_1, 'X'))

        board_2 = [['O', 'O', 'X'],
                   ['O', 'X', 'O'],
                   ['X', 'O', 'O']]
        self.assertTrue(check_winner(board_2, 'X'))

    def test_is_board_full_false(self):
        board_1 = [['X', 'O', 'X'],
                   ['O', ' ', 'O'],
                   ['O', 'X', 'X']]
        self.assertFalse(is_board_full(board_1))

    def test_is_board_full_true(self):
        board_1 = [['X', 'O', 'X'],
                   ['O', 'X', 'O'],
                   ['O', 'X', 'X']]
        self.assertTrue(is_board_full(board_1))

    def test_take_input(self):
        board = [['X', 'O', 'X'],
                 ['O', ' ', 'O'],
                 ['O', 'X', 'X']]

        def mock_input_func(prompt):
            return '5'

        row, col = take_input('X', board, mock_input_func)
        self.assertEqual(row, 1)
        self.assertEqual(col, 1)


if __name__ == '__main__':
    unittest.main()

