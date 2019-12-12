import Modules.Player as player
import Modules.Deck as deck
import Variants.Classic as classic

class Game():
    """
    Game class initializes Players, Game variant and the Deck.
    This class also handles the gameplay and decides the outcome.
    """
    def __init__(self):
        """
        This constructor initializes a new game
        """
        self.players = []
        self.variant = None
        self.decks = None
        self.initialize_players()
        self.initialize_deck()
        self.initialize_game()

    def initialize_players(self):
        """
        This function initializes new players based on the user input
        """
        while True:
            try:
                player_count = int(input("Please enter the number of players. Enter in the range of 2 and 10 : "))
                if player_count < 2:
                    raise ValueError("This game needs at least 2 players to play")
                elif player_count > 10:
                    raise ValueError("Please enter the number of players less than 11")
            except ValueError as error:
                print(error)
                continue
            else:
                break
        self.players = [player.Player(player_id) for player_id in range(1, player_count + 1)]
        print(f"Players created for this game are {[player_id for player_id in range(1, player_count + 1)]}")

    def initialize_deck(self):
        """
        This function initializes the number of cards to be used in the game 
        """
        players_count = len(self.players)
        minimum_decks_required = int(players_count / 52) + 1
        while True:
            try:
                deck_count = int(input(f"Please enter the number of card decks you want to use. Enter in the range of {minimum_decks_required} and {minimum_decks_required + 4} : "))
                if deck_count < minimum_decks_required:
                    raise ValueError(f"This game needs at least {minimum_decks_required} number of card decks")
                elif deck_count > (minimum_decks_required + 4):
                    raise ValueError(f"Please enter the decks needed less than {minimum_decks_required + 5}")
            except ValueError as error:
                print(error)
                continue
            else:
                break
        self.decks = deck.Deck(deck_count)

    def initialize_game(self):
        """
        This initializes the variation of choice and runs the whole game until one player wins the game
        TODO: explain the rules of the variants
        """
        while True:
            try:
                variation = int(input("Please choose the variation of the game. Enter 1 for Classic (Currently this game supports only one variation): "))
                if variation != 1:
                    raise ValueError("Please enter 1 to choose the variation of the game of choice")
            except ValueError as error:
                print(error)
                continue
            else:
                break
        if variation == 1:
            self.variant = classic.Classic(self.players, self.decks)
        self.decks.assign_cards_to_players(self.players)
        round_count = 0
        while not self.variant.end_game_reached():
            print(f"----------------- Round {round_count + 1} -----------------")
            round_winner = self.variant.play_a_round()
            print(f"Round {round_count + 1} winner: Player {round_winner}")
            print("------------------------------------------------------------")
            round_count += 1
        winners = self.variant.get_winners()
        if len(winners) > 1:
            print(f"THE WINNERS OF THE GAME ARE PLAYERS {[winner.player_id for winner in winners]}")
        else:
            print(f"THE WINNER OF THE GAME IS PLAYER {winners[0].player_id}")
        exit()