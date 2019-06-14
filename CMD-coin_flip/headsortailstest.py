import Coin_action
import unittest

class TestCoin(unittest.TestCase):
######Coin.flip
    def test_flip(self):
        result = Coin_action.Coin.flip(self)
        self.assertIn(result, ['Heads', 'Tails'])
#########action
    def test_action(self):
        text = 'Heads'
        result = Coin_action.action(text)
        self.assertEqual(result, 'Heads')

    def test_action2(self):
        text = 't'
        result = Coin_action.action(text)
        self.assertEqual(result, 'Tails')

    def test_action3(self):
        text = 'xeads'
        result = Coin_action.action(text)
        self.assertNotEqual(result, 'Heads' or 'Tails')
######play_again
    def test_play_again(self):
        result = Coin_action.play_again('Y')
        self.assertTrue(result)

    def test_play_again2(self):
        result = Coin_action.play_again('NO')
        self.assertFalse(result)

    def test_play_again3(self):
        result = Coin_action.play_again('Y')
        self.assertNotEqual(result, 'Y' or 'N')


if __name__ == '__main__':
    unittest.main()
