class Player():
    """
    This player class initializes a player with a unique ID and exposes
    functions to play a card and assign/add cards to the player's deck
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.player_deck = []

    def assign_cards(self, cards):
        try:
            if len(cards) < 1:
                raise ValueError("Please assign at least one card to the player")
            self.player_deck = cards
        except ValueError as error:
            print(error)
            exit()

    def add_cards(self, cards):
        self.player_deck + cards

    def is_deck_empty(self):
        return len(self.player_deck) == 0