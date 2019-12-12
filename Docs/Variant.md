This document explains the what the Variants are, how a new one can be added to the project and the existing ones.

What is a Variant?
-----------------
A variant of a game defines all the rules with which the game is played. It also states the constraints and requirements which are required for it to function. A simple example can be a Classic variant present in this game which says that the game can be played by more than two people and a player wins the game by winning all the cards from other players.

Classic Variant
---------------
This is a simple variant which is played by two or more people with cards divided from the deck. The winner wins the game by winning all the cards from the opponents or by having maximum number of cards when maximum rounds are played. The following are the detailed rules of the game.
* This game requires at least 2 players.
* The player with the highest card played in a round takes all the cards played by the players.
* The cards won goes to the bottom of the deck of the player who won the round.
* If two or more of the players end up playing the card of same number and its the maximum valued card played in the round, then there is a tie.
* Players in the tie will start a war among themselves and whoever wins takes all the cards played.
* If a player runs out of the cards he loses and the last player with the cards wins the game
* The game is played for the maximum of 100 rounds and then the player with the maximum number of cards wins the game. **This constraint of maximum rounds is put in place to avoid the game running between two players for a very long time**
* If a player ends up with a tie and runs out of cards to play, then the cards played on the table will be shuffled and distributed to the players involved in the tie.

Base Variant
------------
This is a Subclass defined so that a new variant can be easily created by inheriting the structure from this. This can also be seen in case of Classic variant doing the same.

Things to do when adding a new variant
--------------------------------------
* make sure to create a superclass of the Base class for a new variant to be created
* Once created, this should only be consumed directly in the Game.py and should not be used anywhere else in the project, to keep it modular.
* All the functions in the Base class needs to be overridden in the new variant class otherwise **NotImplementedError** will be thrown.