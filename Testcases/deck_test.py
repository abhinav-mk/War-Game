import unittest
import sys
sys.path.append("..")
from Modules.Deck import Deck
from Modules.Player import Player
  
class DeckTest(unittest.TestCase): 

    test_deck = Deck(1)
    test_deck2 = Deck(1)
    test_player1 = Player(1)
    test_player2 = Player(2)
    sample_cards = [10, 11, 12, 13, 14]
    sample_cards_mapped = ["10", "J", "Q", "K", "A"]
    
    def test_cards_left_on_deck(self):
        self.assertEqual(len(self.test_deck.cards), self.test_deck.cards_left_on_deck())
    
    def test_assign_cards_to_players(self):
        self.test_deck.assign_cards_to_players([self.test_player1, self.test_player2])
        self.assertEqual(len(self.test_player1.player_deck), 26)

    def test_get_cards_from_deck(self):
        self.assertEqual(len(self.test_deck2.get_cards_from_deck(52)), 52)

    def test_get_cards_mapped_from_numbers(self):
        self.assertEqual(self.test_deck.get_cards_mapped_from_numbers(self.sample_cards), self.sample_cards_mapped)
  
if __name__ == '__main__':
    unittest.main()