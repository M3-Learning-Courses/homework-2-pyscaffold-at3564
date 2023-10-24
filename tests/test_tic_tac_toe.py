# This code was generated using ChatGPT GPT-3.5

import unittest
from unittest.mock import patch
from io import StringIO
from tic_tac_toe.tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_take_input(self):
        game = TicTacToe()
        self.assertTrue(game.take_input(5))
        self.assertFalse(game.take_input(5))  # Attempting to take the same position twice

    def test_check_winner(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['X', ' ', 'O']]
        self.assertTrue(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'O']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'O', 'X']]
        self.assertTrue(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertTrue(game.check_winner())

    def test_is_board_full(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'],
                      ['O', ' ', 'O'],
                      ['O', 'X', 'X']]
        self.assertFalse(game.is_board_full())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertTrue(game.is_board_full())
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['5', '2', '1', '9', '6', '4', '3', '7', 'exit'])
    def test_play_game(self, mock_input, mock_output):
        game = TicTacToe()
        game.play_game()

        expected_output = [
            "Welcome to Tic-Tac-Toe!\n",
            "Player X, enter the position (1-9) or 'exit' to quit:\n",
            "Player O, enter the position (1-9) or 'exit' to quit:\n",
            "Player X, enter the position (1-9) or 'exit' to quit:\n",
            "Player O, enter the position (1-9) or 'exit' to quit:\n",
            "Player X, enter the position (1-9) or 'exit' to quit:\n",
            "Player O, enter the position (1-9) or 'exit' to quit:\n",
            "Player X, enter the position (1-9) or 'exit' to quit:\n",
            "Player O, enter the position (1-9) or 'exit' to quit:\n",
            "Exiting the game.\n"
        ]
        
        output = mock_output.getvalue()
        for item in expected_output:
            self.assertIn(item, output)


if __name__ == '__main__':
    unittest.main()
