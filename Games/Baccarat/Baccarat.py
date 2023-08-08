import random
import sys
import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath("main.py"))
db_path = os.path.join(BASE_DIR, "Casino.db")
con = sqlite3.connect(db_path)
cur = con.cursor()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

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
        self.shoe = Shoe(6)  # Create a shoe with 6 decks

    def option(self):
        print('''
Options:
1: Status
2: Place bets
3: Deal cards
4: Change shoe
0: Quit''')

    def status(self):

        print(f'Player username: {self.pUserName}')
        print(f'Player Name: {self.pLastName} {self.pFirstName}')
        print(f"Money: {self.userMoney}")
        print(f"Total Money Made: {self.pMoneyMade}")
        print(f"Total Money Lost: {self.pMoneyLost}")
        print(f"Total Games Won: {self.pWin}")
        print(f"Total Games Lost: {self.pLost}")
        print(f"Current Game: {self.currGame}")

    def place_bets(self):

        print(f"New bet for {self.pUserName}. Press <s> to skip.")
        bet_hand = input("The hand to bet. <p> player, <b> banker, <t> tie: ")

        if bet_hand in ['p', 'b', 't']:
            try:
                bet_amount = int(input("The amount to bet: "))
                if bet_amount <= 0:
                    print("Invalid bet amount. Bet amount must be greater than 0.")
                    return
                if bet_amount > self.userMoney:
                    print("Insufficient balance. Bet amount exceeds your available credit.")
                    return
                self.bet_hand = bet_hand
                self.bet_amount = bet_amount
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
            self.bet_result = "win" if self.bet_hand == 'p' else "lose"
        elif player_value < banker_value:
            print("Banker win.")
            self.bet_result = "win" if self.bet_hand == 'b' else "lose"
        else:
            print("Tie.")
            self.bet_result = "win" if self.bet_hand == 't' else "lose"

        # Show the bet result
        print(f"\nChecking bets...")
        bet_amount = self.bet_amount
        if self.bet_result == "win":
            print(f"{self.pUserName} win. Balance: {self.userMoney + bet_amount}.")
            self.userMoney += bet_amount
            self.pMoneyMade += bet_amount
            self.pWin += 1
        else:
            print(f"{self.pUserName} lose. Balance: {self.userMoney - bet_amount}.")
            self.userMoney -= bet_amount
            self.pMoneyLost += bet_amount
            self.pLost += 1

        input("\nBets are open.\n\nPress <enter> to continue...")

    def change_shoe(self,num_decks):
        self.shoe = Shoe(num_decks)
        print (f"Changed to a new shoe with {num_decks} decks.")

    def run(self):
        while self.userMoney > 0:
            self.option()
            choice = int(input("Your selection: "))
            if choice == 1:
                self.status()
            elif choice == 2:
                self.place_bets()
            elif choice == 3:
                self.deal_cards()
            elif choice == 4:
                decks = int(input("Enter the number of decks for the new shoe: "))
                self.change_shoe(decks)
            elif choice == 0:
                '''Update Player table and Insert data to statistics table'''
                cur.execute("INSERT INTO Statistics VALUES (?, ?, ?, ?, ?, ?, ?);", (self.pUserName, self.currGame, self.pMoneyMade, self.pMoneyLost, self.pWin, self.pLost, current_time))
                cur.execute(f"UPDATE Player SET playerUserName = ?, playerFirstName = ?, playerLastName = ?, pCredit = ?, pMoneyMade = ?, pMoneyLost = ?,  currGame = ?, pWIn = ?, pLoss = ? WHERE playerUserName= ? ;", 
                        (self.pUserName, self.pFirstName, self.pLastName, self.userMoney, self.pMoneyMade, self.pMoneyLost, self.currGame, self.pWin, self.pLost, self.pUserName))
                con.commit()
                print("Quitting the game.")
                break  # Exit the script with a successful status code (0)
            else:
                print("Invalid choice. Please try again.")
            
    '''
    def update_credit(self, cur):
        cur.execute(f"UPDATE Player SET pCredit = ? WHERE playerUserName= ? ;", (self.userMoney, self.pUserName))

    def update_player(self,cur):
        cur.execute(f"UPDATE Player SET playerUserName = ?, playerFirstName = ?, playerLastName = ?, pCredit = ?, pMoneyMade = ?, pMoneyLost = ?,  currGame = ?, pWIn = ?, pLoss = ? WHERE playerUserName= ? ;", 
                    (self.pUserName, self.pFirstName, self.pLastName, self.userMoney, self.pMoneyMade, self.pMoneyLost, self.currGame, self.pWin, self.pLost, self.pUserName))
        '''
        
# Run the Baccarat game
'''
baccarat = Baccarat(100, "Bob", "Bob", "bob1", 0, 0, 0, 0)
print("Welcome to Baccarat")
baccarat.run()
'''

