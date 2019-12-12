import unittest
import sys
sys.path.append("..")
from Variants.Classic import Classic
from Modules.Deck import Deck
from Modules.Player import Player
  
class ClassicTest(unittest.TestCase): 

    test_deck = Deck(1)
    test_player1 = Player(1)
    test_player2 = Player(2)
    test_classic = Classic([test_player1, test_player2], test_deck)
    
    def test_end_game_reached(self):
        self.test_deck.assign_cards_to_players([self.test_player1, self.test_player2])
        self.assertFalse(self.test_classic.end_game_reached())
    
    def test_get_winners(self):
        self.assertEqual(self.test_classic.get_winners(), [self.test_player1, self.test_player2])

    def test_remove_players_lost(self):
        self.test_player1.player_deck = []
        self.test_classic.remove_players_lost()
        self.assertEqual(len(self.test_classic.active_players), 1)

    def test_play_a_round(self):
        while True:
            test_player1_card = self.test_player1.player_deck[0]
            test_player2_card = self.test_player2.player_deck[0]
            if test_player1_card > test_player2_card:
                self.assertEqual(self.test_classic.play_a_round(), 1)
                break
            elif test_player1_card < test_player2_card:
                self.assertEqual(self.test_classic.play_a_round(), 2)
                break
            else:
                continue

if __name__ == '__main__':
    unittest.main()