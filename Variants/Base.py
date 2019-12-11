import random

class Base():
    """
    This class represents the base variation of the game upon which other variations can be 
    built, utilizing the functionalities of this class.
    If the superclass does not override all of these functions in this class, an error is
    thrown.
    """
    def __init__(self, players):
        raise NotImplementedError

    def play_a_round(self, players=None):
        """
        Override this function in the superclass implementing a round of the game with players
        and deck
        """
        raise NotImplementedError

    def end_game_reached(self):
        """
        Override this function in the superclass to define the condition which states that the
        game is over and the winner is declared
        """
        raise NotImplementedError

    def get_winner(self):
        """
        Override this function in the superclass to return the winner of the game when called
        """
        raise NotImplementedError

    def remove_players_lost(self):
        """
        Override this function in the superclass to cleanup the players who lose the game either
        by losing all the cards or the losing condition defined in the variation
        """
        raise NotImplementedError