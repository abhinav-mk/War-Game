import Variants.Base as base
import random

class Classic(base.Base):
    """
    The rules of the Classic variant is as follows:
    * The player with the highest card played takes all the cards played by the players
    * The cards won goes to the bottom of the deck of the player who won the round
    * If two or more of the players end up playing the card of same number and its the maximum played in the round,
      then there is a tie.
    * Players in the tie will start a war among themselves and whoever wins takes all the cards played
    * If a player runs out of the cards he loses and the last player with the cards wins the game
    * The game is played for the maximum of 100 rounds and then the player with the maximum number of cards wins the
      game 
    * Edge-case: If a player ends up with a tie and runs out of cards to play, then the cards played on the table will be
      shuffled and distributed to the players involved in the tie.
    """
    def __init__(self, players):
        """
        This class initializes the active players for the current game, and a list to store all
        the cards being played on the table for a given round.
        """
        self.cards_played_on_table = []
        self.active_players = players
        self.max_rounds = 100
        self.round_count = 0

    def play_a_round(self, players=None):
        """
        This function plays a round for all the active players and assigns the cards won by the
        player to the end of his deck. This also takes care breaking the tie between opponents by
        repeatedly making them play using their deck. 
        * There can be an edge case where a player might end up in a tie and runs out of cards
        In this case, the cards on the table are shuffled and distributed back to the players who
        ended up in a tie.
        Return value: This function returns the player_id of the winner or -1 if the cards are distributed
        due to a tie with a player running out of cards.
        """
        try:
            if players == None and len(self.active_players) < 2:
                raise ValueError("There are incorrect number of players playing the game")
            if players is None:
                players = self.active_players
                self.round_count += 1
            cards_played = [(player, player.play_a_card()) for player in players]
            max_value_card = cards_played[0]
            for card in cards_played[1 : ]:
                if card[1] > max_value_card[1]:
                    max_value_card = card
            round_winners = [card[0] for card in cards_played if card[1] == max_value_card[1]]
            winners_count = len(round_winners)
            if winners_count == 1:
                cards_won = [card[1] for card in cards_played]
                round_winners[0].assign_cards(cards_won)
                self.remove_players_lost()
                if len(self.cards_played_on_table) > 0:
                    round_winners[0].assign_cards(self.cards_played_on_table)
                    self.cards_played_on_table = []
                return round_winners[0].player_id
            else:
                tie_with_deck_empty = False
                for winner in round_winners:
                    if winner.is_deck_empty():
                        tie_with_deck_empty = True
                        break
                # This is the edge-case mentioned in the above comment
                if tie_with_deck_empty:
                    cards_in_tie = [card[1] for card in cards_played]
                    if len(self.cards_played_on_table) > 0:
                        cards_in_tie += self.cards_played_on_table
                        self.cards_played_on_table = []
                    random.shuffle(cards_in_tie)
                    cards_per_winner = int(len(cards_in_tie) / winners_count)
                    for index in range(winners_count):
                        round_winners[index].assign_cards(cards_in_tie[index * cards_per_winner : (index + 1) * cards_per_winner])
                    self.remove_players_lost()
                    return -1
                else:
                    self.cards_played_on_table += [card[1] for card in cards_played]
                    return self.play_a_round(round_winners)
        except ValueError as error:
            print(error)
            exit()

    def end_game_reached(self):
        """
        The game is ended when there is only one active player left in the game.
        """
        return len(self.active_players) == 1 or (self.round_count == self.max_rounds)

    def get_winners(self):
        """
        This function returns the winner who is the only active player in the game
        """
        if len(self.active_players) > 1:
            max_card_count = len(self.active_players[0].player_deck)
            for player in self.active_players[1 : ]:
                if len(player.player_deck) > max_card_count:
                    max_card_count = len(player.player_deck)
            return [player for player in self.active_players if len(player.player_deck) == max_card_count]
        else:
            return [self.active_players[0]]

    def remove_players_lost(self):
        """
        This is a cleanup function which removes players who have lost the game after every round
        """
        self.active_players = [player for player in self.active_players if not player.is_deck_empty()]