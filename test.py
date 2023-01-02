import unittest
import logic


class Tests(unittest.TestCase):
    # o winner
    def test_get_winner_X(self):
        board = [
            [None, None, 'X'],
            ['O', 'O', 'O'],
            [None, 'X', None],
        ]

        self.assertEqual(logic._check_winners(board, 'X'), 'X')
    
    # Test a case where there is stalemate
    def test_draw(self):
        board = [
            ['O', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
        ]
        
        self.assertEqual(logic._check_winners(board, 'X'), None)

if __name__ == '__main__':
    unittest.main()