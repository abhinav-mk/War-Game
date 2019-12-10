import random

class Deck():
    """
    The Deck class handles the initialization of the deck which comprises
    of 52 cards, 13 different cards with 4 each.
    """
    def __init__(self, deck_count):
        self.cards = []
        self.total_cards = deck_count * 52
        for index in range(deck_count):
            for card_number in range(2, 15):
                self.cards.append(card_number)
        random.shuffle(self.cards)

    def assign_cards_to_players(self, players):
        try:
            players_count = len(players)
            if players_count < 2:
                raise ValueError('There should be at least two players the cards should be distributed to')
            cards_count_per_player = int(self.total_cards / players_count)
            for player in players:
                player.assign_cards(get_cards_from_deck(cards_count_per_player))
        except ValueError as error:
            print(error)
            exit()

    def get_cards_from_deck(self, cards_count):
        try:
            if self.cards_left_on_deck() >= cards_count:
                cards_to_distribute = self.cards[ : cards_count]
                self.cards = self.cards[cards_count : ]
                return cards_to_distribute
            else:
                raise ValueError('Cards requested are more than the cards present in the deck')
        except ValueError as error:
            print(error)
            exit()

    def cards_left_on_deck(self):
        return len(self.cards)

