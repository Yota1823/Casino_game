import time
from rules import Table, GameError  # Import necessary modules
import os
import sqlite3
import os.path

# Define the path to the SQLite database
BASE_DIR = os.path.dirname(os.path.abspath("main.py"))
db_path = os.path.join(BASE_DIR, "Casino.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

# Retrieve player data from the database
cur.execute("SELECT * FROM Player")
player = cur.fetchall()


class Cli:
    """Command line interface of the game. Only interacts with Table object in
    order to receive input from the game logic.
    """
    def __init__(self):
        # Initialize the Cli object with a Table instance for the game and other variables
        self._game = Table()
        self._quit = False
        self._options = {
            '1': self.status,      # Map user input to corresponding methods
            '2': self.add_player,
            '3': self.place_bets,
            '4': self.deal_hands,
            '5': self.create_shoe,
            '0': self.quit
        }

    def run(self):
        """Main menu of the game. Displays options and takes user input."""
        print('Welcome to Baccarat')
        while not self._quit:
            print('''
Options:
1: Status
2: Add player
3: Place bets
4: Deal cards
5: Change shoe
0: Quit''')
            print()
            selection = input('Your selection: ')
            print()
            if selection and selection in self._options:
                # Call the corresponding function based on the user's input
                self._options.get(self._options[selection])()
            else:
                print('Selection not recognized.')

    def status(self):
        """Option 1: Prints the players' status and other in-game information."""
        # Display the current shoe's details and available players with their balances
        print(f'Shoe with {self._game.num_decks} deck(s).')
        if self._game.available_players:
            print(f'{len(self._game.available_players)} player(s) in game:')
            for player in self._game.available_players:
                print(self._game[player])
        else:
            print('No players present on the table.')
        input('Press <enter> to continue...')

    def add_player(self):
        """Option 2: Adds a new player to the game."""
        # Ask the user to enter the initial balance for the new player
        balance_input = input('Initial balance for the new player or <c> to cancel: ')
        if balance_input.lower() in ['c', 'cancel']:
            return
        try:
            # Try to convert the input to an integer (player's initial balance)
            balance_input = int(balance_input)
            self._game.add_player(balance_input)  # Add the new player to the game
            print()
            print(f'Player added with {balance_input} balance.')
            input('Press <enter> to continue...')
        except (ValueError, TypeError) as error:
            # If the input is not a valid integer, prompt the user again
            print()
            print(error)
            self.add_player()

    def place_bets(self):
        """Option 3: Loops through all the available players to place individual bets."""
        if self._game.available_players:
            for player_i in self._game.available_players:
                self.bet(player_i)  # Place a bet for each player
            print('All bets placed.')
        else:
            print('No players to place bets.')
        input('Press <enter> to continue...')

    def bet(self, player_i):
        """Places an individual bet for player_i."""
        # Define the available betting options and their corresponding input values
        hands = {
            'p': 'player',
            'player': 'player',
            'b': 'banker',
            'banker': 'banker',
            't': 'tie',
            'tie': 'tie'
        }
        action = 'Replacing' if player_i in self._game.valid_bets else 'New'
        print(f'{action} bet for Player {player_i + 1}. Press <s> to skip.')
        hand_input = input('The hand to bet. <p> player, <b> banker, <t> tie: ')
        if hand_input.lower() in ['s', 'skip']:
            print()
            return
        amount_input = input('The amount to bet: ')
        if amount_input.lower() in ['s', 'skip']:
            print()
            return
        try:
            # Try to convert the amount input to an integer (bet amount)
            amount_input = int(amount_input)
            self._game.bet(player_i, hands.get(hand_input.lower()), amount_input)
            print()
        except (ValueError, TypeError, GameError) as error:
            # If the input is not a valid integer or there is a game error, prompt the user again
            print()
            print(error)
            self.bet(player_i)

    def deal_hands(self):
        """Option 4: Deals both punto and banco hands and proceeds with the game."""
        # Inner functions to display game results and player hands
        def result_str():
            """Returns a string with the game result to be printed as output."""
            if self._game.game_result() != 'tie':
                return self._game.game_result().title() + ' win'
            else:
                return self._game.game_result().title()

        def print_hands():
            print(f'Player hand: {self._game.punto_cards}.')
            punto_values = ', '.join([str(value) for value in self._game.punto_values])
            print(f'Cards values: {punto_values}.')
            print(f'Total hand value: value: {self._game.punto_value}.')
            time.sleep(0.5)
            print(f'Banker hand: {self._game.banco_cards}.')
            banco_values = ', '.join([str(value) for value in self._game.banco_values])
            print(f'Cards values: {banco_values}.')
            print(f'Total hand value: value: {self._game.banco_value}.')

        print('Dealing hands...')
        time.sleep(1)
        self._game.deal_hands()  # Deal punto and banco hands
        print_hands()  # Display player hands and card values
        print()
        if self._game.is_natural():
            time.sleep(0.5)
            print(f'{result_str()}. Natural.')
        else:
            print('Drawing third cards...')
            time.sleep(1)
            third_draws = self._game.draw_thirds()
            for third_draw in third_draws:
                print(f'{third_draw[0].title()} draw third card, {third_draw[1]}.')
                time.sleep(0.5)
            print()
            print_hands()
            time.sleep(0.5)
            print(f'{result_str()}.')
        print()
        input('Press <enter> to continue...')
        print()
        print('Checking bets...')
        time.sleep(1)
        if self._game.valid_bets:
            for player_i in self._game.valid_bets:
                bet_result = self._game.bet_result(player_i)
                print(f'Player {player_i + 1} {bet_result[0]}. Balance: {bet_result[1]}.')
                time.sleep(0.5)
        else:
            print('No bets on the table.')
        if self._game.open_bets():
            print('Bets are open.')
        print()
        input('Press <enter> to continue...')

    def create_shoe(self):
        """Option 5: Creates a new shoe with a specified number of decks."""
        shoe_input = input('The number of decks for the new shoe or <c> to cancel: ')
        if shoe_input.lower() in ['c', 'cancel']:
            return
        try:
            # Try to convert the input to an integer (number of decks in the new shoe)
            shoe_input = int(shoe_input)
            self._game.create_shoe(shoe_input)  # Create a new shoe with the specified number of decks
            print()
            print(f'A new shoe with {int(shoe_input)} deck(s) will be used in the game.')
            input('Press <enter> to continue...')
        except (ValueError, TypeError) as error:
            # If the input is not a valid integer, prompt the user again
            print()
            print(error)
            self.create_shoe()

    def quit(self):
        """Option 0: Quits the game upon confirmation from the user."""
        quit_input = input('Do you really wish to quit? <y/n>: ')
        if quit_input.lower() in ['y', 'yes']:
            self._quit = True
        elif quit_input.lower() in ['n', 'no']:
            return
        else:
            print('Invalid input.')
            self.quit()


if __name__ == '__main__':
    # Create a Cli object and start the game by calling the run() method
    Cli().run()
