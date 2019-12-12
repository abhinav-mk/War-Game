import random

class Deck():
    """
    The Deck class handles the initialization of the deck which comprises
    of 52 cards, 13 different cards with 4 each.
    """
    card_mapping = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10", "11": "J", "12": "Q", "13": "K", "14": "A"}

    def __init__(self, deck_count):
        """
        This constructor creates a set of cards by taking in the number of decks
        to be used for this game 
        """
        self.cards = []
        self.total_cards = deck_count * 52
        for index in range(deck_count):
            for i in range(4):
                for card_number in range(2, 15):
                    self.cards.append(card_number)
        random.shuffle(self.cards)

    def assign_cards_to_players(self, players):
        """
        This functions divides the cards in the deck to the players during the beginning of the game
        """
        try:
            players_count = len(players)
            if players_count < 2:
                raise ValueError('There should be at least two players the cards should be distributed to')
            cards_count_per_player = int(self.total_cards / players_count)
            for player in players:
                player.assign_cards(self.get_cards_from_deck(cards_count_per_player))
        except ValueError as error:
            print(error)
            exit()

    def get_cards_from_deck(self, cards_count):
        """
        This is a helper function which retrieves the cards unused from the deck and returns it.
        Uses: Can be used to lend cards to the player who runs out of the cards in some variants of the game
        """
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
        """
        returns the number of cards present in the deck unused
        """
        return len(self.cards)
    
    def get_cards_mapped_from_numbers(self, cards):
        return list(map(lambda x : self.card_mapping[str(x)], cards))