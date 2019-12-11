import random

class Base():
    """
    This class represents the base variation of the game upon which other variations can be 
    built, utilizing the functionalities of this class
    The rules of this variant is as follows:
    * All the players play the card on top of their deck
    * the player with the highest card played takes all the cards played by the players
    * The cards won goes to the bottom of the deck of the player who won the round
    * If two or more of the players end up playing the card of same number, then there is a tie
    * Players in the tie will start a war among themselves and whoever wins takes all the cards played
    * If a player runs out of the cards he loses and the last player with cards wins the game
    * If the player
    """
    def __init__(self, players):
        """
        This class initializes the active_players for the current game, and a list to store all
        the cards being played on the table for a given round.
        """
        self.cards_played_on_table = []
        self.active_players = players

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
            if players == None and len(self.active_players < 2):
                raise ValueError("There are incorrect number of players playing the game")
            if players is None:
                players = self.active_players
            cards_played = [(player, player.play_a_card()) for player in players]
            max_value_card = cards_played[0]
            for card in cards_played[1 : ]:
                if card[1] > max_value_card[1]:
                    max_value_card = card
            round_winners = [card[0] for card in cards_played if card[1] == max_value_card]
            winners_count = len(round_winners)
            if winners_count == 1:
                cards_won = [card[1] for card in cards_played]
                round_winners[0].assign_cards(cards_won)
                if len(self.cards_played_on_table) > 0:
                    round_winners[0].assign_cards(self.cards_played_on_table)
                    self.cards_played_on_table = []
                    self.remove_players_lost()
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
                    cards_per_winner = int(cards_in_tie / winners_count)
                    for index in range(winners_count):
                        round_winners[i].assign_cards(cards_in_tie[index * cards_per_winner : (index + 1) * cards_per_winner])
                    self.remove_players_lost()
                    return -1
                else:
                    self.cards_played_on_table += cards_played
                    self.remove_players_lost()
                    return self.play_a_round(round_winners)
        except ValueError as error:
            print(error)
            exit()

    def end_game_reached(self):
        """
        The game is ended when there is only one active player left in the game.
        """
        return len(self.active_players) == 1

    def get_winner(self):
        """
        This function returns the winner who is the only active player in the game
        """
        return self.active_players[0]

    def remove_players_lost(self):
        """
        This is a cleanup function which removes players who have lost the game after every round
        """
        self.active_players = [player for player in self.active_players if not player.is_deck_empty()]