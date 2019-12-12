import unittest
import sys
sys.path.append("..")
from Modules.Player import Player
  
class PlayerTest(unittest.TestCase): 

    test_player = Player(1)
    cards = [2,3,4,5,6,7]
    
    def test_cards_assign(self):       
        self.test_player.assign_cards(self.cards)
        self.assertEqual(self.cards, self.test_player.player_deck)
    
    def test_is_deck_empty(self):
        self.assertFalse(self.test_player.is_deck_empty())

    def test_play_a_card(self):
        self.assertEqual(self.cards[0], self.test_player.play_a_card())
  
if __name__ == '__main__':
    unittest.main()