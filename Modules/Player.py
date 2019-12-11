class Player():
    """
    This player class initializes a player with a unique ID and exposes
    functions to play a card and assign/add cards to the player's deck
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.player_deck = []

    def assign_cards(self, cards):
        """
        This function adds the cards to the players hand/deck.
        Usage: useful during the beginning of the game where
        each user is assigned cards and also to add the cards that are won 
        during a round to the hand/deck. 
        """
        try:
            if len(cards) < 1:
                raise ValueError("Please assign at least one card to the player")
            self.player_deck += cards
        except ValueError as error:
            print(error)
            exit()

    def is_deck_empty(self):
        """
        This function returns true if the player does not possess any card
        Usage: useful to eliminate the player from the game
        """
        return len(self.player_deck) == 0
    
    def play_a_card(self):
        try:
            if len(self.player_deck) == 0:
                raise ValueError("This player does not have any cards or is not playing")
            return self.player_deckpop(0)
        except ValueError as error:
            print(error)
            exit()