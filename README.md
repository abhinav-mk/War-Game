War Game
========

Description
-----------
This project is the implementation of the Game "War". The details of the game and few of the variations can be found in the link [here](https://en.wikipedia.org/wiki/War_(card_game)).

This project is built on Python 3.x and uses standard Python libraries. The project currently supports Classic variation of the game and takes the number of players and the number of decks to be used as the input from the user.

Usage
-----
To run the game, run the following command:
'python3 run.py'

Project Structure
-----------------
<pre>
War-Game --> Project root folder
  ├── run.py            # Run this file to initialize the game.
  ├── Game.py           # Handles initialization of the game including players, decks and Variants, and playing the game.
  ├── Modules           # All the Entities in the Game such as Players, Decks is managed independently here. 
        ├── Deck.py     # Initializes the deck based on the user input and manages card distribution to the Players.
        ├── Player.py   # Initializes the Player with a unique ID and handles playing/adding cards to the player's hand/deck.
  ├── Variants          # This is where all the variations of the game are independently defined using the Base subclass as the template.
        ├── Base.py     # This is the subclass to be inherited for defining any new variation of the game and it provides methods to define the rules of the variation.
        ├──Classic.py   # This is a simple variation of the game with simple rules and maximum number of rounds.
  ├── Docs              # This contains the documentation of the functionality, purpose and assumptions for each of the above defined structures.
  ├── tests             # This folder defines tests to make sure the new code does not bring in loopholes and break the functionality.  
  ├── License
</pre>
Game.py
-------
Game class is responsible for running the entire game starting from initializing all the objects(Players, Decks) and the Variants(Classic, etc) and taking the inputs from the user and displaying the results. This class directly interacts with rest of the classes in the project and the entry to the game.

Future Improvements and Assumptions
-----------------------------------
With more time, the following are the improvements that can be done to enhance the experience of this game.
* Have restricted the number of players to 10 and the number of decks that can be used to minimum required plus 4. This constraint is present to keep the output simple since it is limited to command-line at this point.
* Have more test cases with all the edge cases covered to improve the quality of the project and reduce the time for development of new features
* Improve the interaction between user and the game by moving away from command-line interface to a web user interface for better display of results and to read inputs. This can be achieved by using frameworks such as React or Angular, or simple HTML+JS to start with.
* Having one or more variant of the game with outcome depending on the user's interaction with the game and thus making it interesting to play. Currently, Classic variant has a random outcome since users do not involve in any decision while playing.
* Make a package and deploy this application into a Cloud based Platform-as-a-Service offerings provided by Cloud providers such as Amazon Web Service(Elastic BeanStalk), Google Cloud Platform(App Engine) or Microsoft Azure(Cloud Service).