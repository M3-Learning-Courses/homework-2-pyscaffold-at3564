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
        self.assertFalse(game.take_input(10))  # Attempting to take an invalid position
        self.assertFalse(game.take_input('X'))  # Attempting to take a non-integer position
        self.assertFalse(game.take_input(3.5))  # Attempting to take a float position
        self.assertFalse(game.take_input(0))  # Position 0 is out of range
        self.assertFalse(game.take_input(10))  # Position 10 is out of range

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

        game.board = [['X', 'X', 'O'],
                      ['O', 'O', 'X'],
                      ['X', 'O', 'X']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'O'],
                      ['O', 'X', 'X'],
                      ['X', 'X', 'O']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'O', 'X'],
                      ['X', 'X', 'O']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'X']]
        self.assertTrue(game.check_winner())

        game.board = [['X', 'O', 'O'],
                      ['O', 'O', 'X'],
                      ['X', 'X', 'O']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'X'],
                      ['O', 'X', 'O']]
        self.assertFalse(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['X', 'O', 'O']]
        self.assertTrue(game.check_winner())

        game.board = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'O', 'X']]
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
            "Welcome to Tic-Tac-Toe!",
            " | | ",
            "-----",
            " | | ",
            "-----",
            " | | ",
            "-----",
            " | | ",
            "-----",
            " |X| ",
            "-----",
            " | | ",
            "-----",
            " |O| ",
            "-----",
            " |X| ",
            "-----",
            " | | ",
            "-----",
            "X|O| ",
            "-----",
            " |X| ",
            "-----",
            " | | ",
            "-----",
            "X|O| ",
            "-----",
            " |X| ",
            "-----",
            " | |O",
            "-----",
            "X|O| ",
            "-----",
            " |X|X",
            "-----",
            " | |O",
            "-----",
            "X|O| ",
            "-----",
            "O|X|X",
            "-----",
            " | |O",
            "-----",
            "X|O|X",
            "-----",
            "O|X|X",
            "-----",
            " | |O",
            "-----",
            "X|O|X",
            "-----",
            "O|X|X",
            "-----",
            "O| |O",
            "-----",
            "Exiting the game."
        ]

        output = mock_output.getvalue()
        output_lines = output.split('\n')
        for item in expected_output:
            self.assertIn(item, output_lines)
            
    def test_switch_player(self):
        game = TicTacToe()
        self.assertEqual(game.current_player, 'X')  # Initial current player is 'X'
        game.switch_player()  # Switching player to 'O'
        self.assertEqual(game.current_player, 'O')  # Current player should be 'O'
        game.switch_player()  # Switching player back to 'X'
        self.assertEqual(game.current_player, 'X')  # Current player should be 'X'



if __name__ == '__main__':
    unittest.main()
