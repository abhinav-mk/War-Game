class Base():
	"""
	This class represents the base variation of the game upon which other variations can be 
	built, utilizing the functionalities of this class
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
        TODO: Implementation of this function
		"""
		pass

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