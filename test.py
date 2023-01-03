import unittest
import logic


class Tests(unittest.TestCase):
    # o winner
    def test_get_winner_X(self):
        board = [
            ['X', None, 'O],
            [None, 'O', None
            ['O', 'X', None],
        ]

        self.assertEqual(logic._check_winners(board, 'X'), 'X')
            
if __name__ == '__main__':
    unittest.main()
