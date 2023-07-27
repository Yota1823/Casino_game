import random
import os
import sqlite3 
import os.path
from datetime import datetime
import time

BASE_DIR = os.path.dirname(os.path.abspath("main.py"))
db_path = os.path.join(BASE_DIR, "Casino.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

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
        
        self.bet_amount = 0
        self.card = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self.value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
        self.player_cvalue = 0
        self.banker_cvalue = 0


    def option(self):
        print('''
Options:
1: Status
2: Place bets
3: Deal cards
4: Change shoe''')
    def get_betAmount(self):
        self.bet_amount = int(input("How much do you want to bet: "))
        while self.bet_amount > self.userMoney:
            print("Invalid amount")
            print(f'You currently have ${self.userMoney}')
            self.bet_amount = int(input("Enter another bet amount: "))

    def stats(self):
        print(f'Player username: {self.pUserName}')
        print(f'Player Name: {self.pLastName} {self.pFirstName}')
        print(f'Player Money: ${self.userMoney}')
        print(f'Player Made: ${self.pMoneyMade}')
        print(f'Player Lost: ${self.pMoneyLost}')
        print(f'Player Total Win: {self.pWin}')
        print(f'Player Total Lost: {self.pLost}')

    def get_cards(self):
        #player and banker get 2 random cards
        player_hand = [
            random.choice(self.card),
            random.choice(self.card)
        ]
        casino_hand = [
            random.choice(self.card),
            random.choice(self.card)
        ]
        #ger value of the initial 2 cards
        self.player_cvalue = self.get_score(player_hand)
        self.banker_cvalue = self.get_score(casino_hand)
        #print cards and values
        print('\nPlayer has cards:\t' + player_hand[0] + '\t' + player_hand[1])
        print("Player's cards value:\t" + str(self.player_cvalue))
        time.sleep(1)
        print('\nBanker has cards:\t' + casino_hand[0] + '\t' + casino_hand[1])
        print("Banker's cards value:\t" + str(self.banker_cvalue))

    def get_score(self, hand):
        #Calculate the score of a hand
        total_value = 0
        for card in hand:
            total_value += self.value[self.card.index(card)]
        return total_value % 10

    
    def run(self):
        while self.userMoney > 0:
            self.option()
            user_opt = int(input("Enter Your Option: "))
            if user_opt == 1:
                #print stats of player
                self.stats()
                if input("Continue? (y/n) ").strip().upper() != 'Y':
                    break
            elif user_opt == 2:
                self.get_betAmount()

                if input("Continue? (y/n) ").strip().upper() != 'Y':
                    break
            elif user_opt == 3:
                self.get_cards()

            else:
                print("Option not recognized.")




P1 = Baccarat(100," "," "," ",300,100,1,1)
P1.run()
