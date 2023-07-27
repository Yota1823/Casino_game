import random
import sys


SUITS = ['hearts', 'spades', 'clubs', 'diamonds']
RANKS = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

class Card:
    def __init__(self, rank, suit):
        if rank not in RANKS:
            raise ValueError('Invalid card rank.')
        if suit not in SUITS:
            raise ValueError('Invalid card suit.')
        self._rank = rank
        self._suit = suit
        self._value = self._rank if self._rank in range(2, 10) else 1 if self._rank == 'ace' else 0

    @property
    def value(self):
        return self._value

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f'{self._rank} of {self._suit}'

class Shoe:
    def __init__(self, num_decks):
        if not isinstance(num_decks, int):
            raise TypeError('Number of decks must be an integer.')
        elif num_decks < 1:
            raise ValueError('Number of decks must be positive.')
        self._num_decks = num_decks
        self._cards = []
        self.add_decks()

    def add_decks(self, num_decks=None):
        if not num_decks:
            num_decks = self._num_decks

        for i in range(num_decks):
            for suit in SUITS:
                for rank in RANKS:
                    self._cards.append(Card(rank, suit))
        random.shuffle(self._cards)

    def draw_cards(self, num_cards):
        cards_drawn = []
        for i in range(num_cards):
            if len(self._cards) > 0:
                cards_drawn.append(self._cards.pop())
        return cards_drawn

class Hand:
    def __init__(self, cards):
        self._cards = cards

    @property
    def value(self):
        total_value = sum(card.value for card in self._cards) % 10
        return total_value

    def __str__(self):
        return ', '.join(str(card) for card in self._cards)

class Baccarat:
    def __init__(self):
        self.players = {
            "Player 1": BaccaratPlayer(500, "", "", "Player 1", 300, 100, 1, 1)
        }
        self.currPlayer = None
        self.shoe = Shoe(6)  # Create a shoe with 6 decks
        self._quit = False

    def option(self):
        print('''
Options:
1: Status
2: Place bets
3: Deal cards
4: Change shoe
0: Quit''')
        choice = int(input("Your selection: "))
        if choice == 1:
            self.status()
        elif choice == 2:
            self.select_player()
            self.place_bets()
        elif choice == 3:
            self.deal_cards()
        elif choice == 4:
            decks = int(input("Enter the number of decks for the new shoe: "))
            self.change_shoe(decks)
        elif choice == 0:
            self.quit()
        else:
            print("Invalid choice. Please try again.")

    def quit(self):
        quit_input = input('Do you really wish to quit? <y/n>: ')
        if quit_input.lower() in ['y', 'yes']:
            self._quit = True
            print("Quitting the game.")
            sys.exit(0)  # Exit the script with a successful status code (0)
        elif quit_input.lower() in ['n', 'no']:
            return
        else:
            print('Invalid input.')
            self.quit()

    def select_player(self):
        if not self.players:
            print("No players found. Please add a player first.")
            return

        print("Select a player:")
        for i, player in enumerate(self.players.keys(), 1):
            print(f"{i}: {player}")
        selection = int(input("Enter player number: "))

        if selection not in range(1, len(self.players) + 1):
            print("Invalid player selection. Please try again.")
            return

        player_names = list(self.players.keys())
        self.currPlayer = self.players[player_names[selection - 1]]


    def status(self):
        if self.currPlayer is None:
            print("No player selected. Please select a player first.")
            return

        print(f"Player Name: {self.currPlayer.pUserName}")
        print(f"Money: {self.currPlayer.userMoney}")
        print(f"Total Money Made: {self.currPlayer.pMoneyMade}")
        print(f"Total Money Lost: {self.currPlayer.pMoneyLost}")
        print(f"Total Games Won: {self.currPlayer.pWin}")
        print(f"Total Games Lost: {self.currPlayer.pLost}")
        print(f"Current Game: {self.currPlayer.currGame}")

    def place_bets(self):
        if self.currPlayer is None:
            print("No player selected. Please select a player first.")
            return

        print(f"New bet for {self.currPlayer.pUserName}. Press <s> to skip.")
        bet_hand = input("The hand to bet. <p> player, <b> banker, <t> tie: ")

        if bet_hand in ['p', 'b', 't']:
            try:
                bet_amount = int(input("The amount to bet: "))
                if bet_amount <= 0:
                    print("Invalid bet amount. Bet amount must be greater than 0.")
                    return
                if bet_amount > self.currPlayer.userMoney:
                    print("Insufficient balance. Bet amount exceeds your available credit.")
                    return
                self.currPlayer.bet_hand = bet_hand
                self.currPlayer.bet_amount = bet_amount
                self.currPlayer.userMoney -= bet_amount
                print("Bet placed successfully.")
            except ValueError:
                print("Invalid input. Bet amount must be a positive integer.")
                return
        else:
            print("Invalid hand selection. Please choose <p>, <b>, or <t>.")

    def deal_cards(self):
        print("Dealing hands...")
        player_hand = self.shoe.draw_cards(2)
        banker_hand = self.shoe.draw_cards(2)

        # Calculate and display the total value of player and banker hands
        player_value = sum(card.value for card in player_hand) % 10
        banker_value = sum(card.value for card in banker_hand) % 10

        print(f"Player's hand: {', '.join(str(card) for card in player_hand)}.")
        print(f"Cards values: {', '.join(str(card.value) for card in player_hand)}.")
        print(f"Total hand value: value: {player_value}.")
        print(f"Banker's hand: {', '.join(str(card) for card in banker_hand)}.")
        print(f"Cards values: {', '.join(str(card.value) for card in banker_hand)}.")
        print(f"Total hand value: value: {banker_value}.")

        # Check if player needs to draw a third card
        if player_value >= 8 or banker_value >= 8:
            pass  # Both player and banker stand with 8 or 9
        elif player_value <= 5:
            player_third_card = self.shoe.draw_cards(1)[0]
            player_hand.append(player_third_card)
            player_value = sum(card.value for card in player_hand) % 10
            print("\nDrawing third cards...")
            print(f"Player draws third card, {player_third_card}.")

        # Check if banker needs to draw a third card
        if banker_value <= 5 and player_value <= 7:
            banker_third_card = self.shoe.draw_cards(1)[0]
            banker_hand.append(banker_third_card)
            banker_value = sum(card.value for card in banker_hand) % 10
            print(f"Banker draws third card, {banker_third_card}.")

        print(f"\nPlayer's hand: {', '.join(str(card) for card in player_hand)}.")
        print(f"Cards values: {', '.join(str(card.value) for card in player_hand)}.")
        print(f"Total hand value: value: {player_value}.")
        print(f"Banker's hand: {', '.join(str(card) for card in banker_hand)}.")
        print(f"Cards values: {', '.join(str(card.value) for card in banker_hand)}.")
        print(f"Total hand value: value: {banker_value}.")

        # Determine the winner
        if player_value > banker_value:
            print("Player win.")
            self.currPlayer.bet_result = "win" if self.currPlayer.bet_hand == 'p' else "lose"
        elif player_value < banker_value:
            print("Banker win.")
            self.currPlayer.bet_result = "win" if self.currPlayer.bet_hand == 'b' else "lose"
        else:
            print("Tie.")
            self.currPlayer.bet_result = "win" if self.currPlayer.bet_hand == 't' else "lose"

        # Show the bet result
        print(f"\nChecking bets...")
        bet_amount = self.currPlayer.bet_amount
        if self.currPlayer.bet_result == "win":
            print(f"{self.currPlayer.pUserName} win. Balance: {self.currPlayer.userMoney + bet_amount}.")
            self.currPlayer.userMoney += bet_amount
            self.currPlayer.pMoneyMade += bet_amount
            self.currPlayer.pWin += 1
        else:
            print(f"{self.currPlayer.pUserName} lose. Balance: {self.currPlayer.userMoney - bet_amount}.")
            self.currPlayer.userMoney -= bet_amount
            self.currPlayer.pMoneyLost += bet_amount
            self.currPlayer.pLost += 1

        input("\nBets are open.\n\nPress <enter> to continue...")


class BaccaratPlayer:
    def __init__(self, userMoney, pLastName, pFirstName, pUserName, pMoneyMade, pMoneyLost, pLost, pWin):
        self.userMoney = userMoney
        self.pLastName = pLastName
        self.pFirstName = pFirstName
        self.pUserName = pUserName
        self.pMoneyMade = pMoneyMade
        self.pMoneyLost = pMoneyLost
        self.pLost = pLost
        self.pWin = pWin
        self.currGame = 'Baccarat'
        self.bet_hand = None
        self.bet_amount = 0
        self.bet_result = None

# Run the Baccarat game
baccarat = Baccarat()
print("Welcome to Baccarat")

while True:
    baccarat.option()
    if baccarat.option == 0:
        break