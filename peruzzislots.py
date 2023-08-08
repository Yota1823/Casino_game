import sqlite3
import random
import sys
import os
import os.path
import subprocess
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
#@staticmethod

# def get_player_data():
#     """Static method to retrieve player data from the database"""
#     conn = sqlite3.connect("Casino.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Player")
#     player_data = cur.fetchall()
#     cur.close()
#     conn.close()
#     return player_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Casino.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

class Player:
    def __init__(self, playerUserName, playerFirstName, playerLastName, pCredit, pMadeMoney, pMoneyLost, pWin, pLoss, casinoMoney):
        self.Uname = playerUserName
        self.Fname = playerFirstName
        self.Lname = playerLastName
        self.pCredit = pCredit
        self.pMadeMoney = pMadeMoney
        self.MoneyLost = pMoneyLost 
        self.win = pWin
        self.loss = pLoss
        self.curr = 'Slots'
        self.casinoMoney = casinoMoney
        self.betamount = 0

    def getpCredit(self):
        return self.pCredit
 
        
    # self.pCredit = 1000
    # self.pCredit == int(self.pCredit)
    # pMadeMoney = 0
    # pMadeMoney == int(pMadeMoney)

    Symbols = ["Leopard", "wit shield", "W lines", "Big W", "7"]

    # Checking the Bet input and amount
    def betcheck(self, betamount):
        if betamount.isdigit() == True:
            betamount = int(betamount)
            rightbet = True
        else: 
            rightbet = False
            print("Please enter a whole number, no decimals and a bet on or below the self.pCredit.")
        return rightbet

    # Limiting the bet
    def betlimit(self, betamount):
        if betamount > self.getpCredit():
            goodlimit = self.getpCredit()
            print("That bet is too high! Bet adjusted to ", goodlimit)
        else:
            goodlimit = betamount
        return goodlimit

    # Checking the 'Ask' input to play the machine.
    def askinputcheck(self, answerinput):
        if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" or answerinput == "No" or answerinput == "no" or answerinput == "n":
            rightanswerinput = True
        else:
            rightanswerinput = False
            "This is an incorrect input, please type an appropriate answer in."
        return rightanswerinput

    # Printing and sorting symbols.
    def spinning(self, reels, betamount):
        reelone, reeltwo, reelthree = reels[0], reels[1], reels[2]
        #global self.pCredit
        pMadeMoney = 0
        if reelone[0] == "Leopard" and reeltwo[0] == "Leopard" and reelthree[0] == "Leopard":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount)* 10
            print("You won 10 times your money! Congragulations! This is how much your account contains $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif reelone[0] == "wit shield" and reeltwo[0] == "wit shield" and reelthree[0] == "wit shield":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount) * 25
            print("You won 25 times your money! Awesome! Your self.pCredit and wins are $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif reelone[0] == "W lines" and reeltwo[0] == "W lines" and reelthree[0] == "W lines":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount) * 50
            print("You won 50 times your money! This is all of your money total $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif reelone[0] == "Big W" and reeltwo[0] == "Big W" and reelthree[0] == "Big W":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount) * 75
            print("You won 75 times your money! You rewards are $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif reelone[0] == "7" and reeltwo[0] == "7" and reelthree[0] == "7":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + 1000000
            print("You  the ulimate Jackpot! You rewards are $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif reelone[0] == "7" and (reeltwo[0] == "7" or reelthree[0] == "7"):
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount) * 2
            print("You won 2 times your money! You rewards are $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        elif (reelone[0] == "7" or reeltwo[0] == "7") and reelthree[0] == "7":
            pMadeMoney = (int(self.pCredit) - int(betamount)) + int(betamount) * 2
            print("You won 2 times your money! You rewards are $", pMadeMoney)
            self.win = self.win +1
            self.pMadeMoney = pMadeMoney  - betamount
        else:
            self.loss = self.loss +1
            pMoneyLost = int(self.pCredit) - int(betamount)
            self.MoneyLost =self.MoneyLost + betamount
            print("Bad luck! Maybe next time you'll win! Your remaining cash is $", pMoneyLost)
            print(pMoneyLost)
            self.pCredit = pMoneyLost
        return reels

    # If you have no money
    def repCredit(self, startagain):        
        while self.pCredit < 1 and startagain == True:
            unpCredit = True
            print(self.pMadeMoney)
            print("You ran out of money, go refill at main screen")
        else:
            unpCredit = False
            print("You still have money.")
            return self.pMadeMoney

    # Leads to Bet input check. 
    def my_mainloop(self):
        global pCredit
        
        while True:
            Validbet = False
            while Validbet == False:
                betamount = input("Please enter amount you wish to bet: ")
                Validbet = self.betcheck(betamount)
                #self.pCredit = self.pCredit - Validbet

            betamount = int(betamount)

            # Leads to betlimit
            betamount = self.betlimit(betamount)

            # RandomSymbolGen + 3 reels
            if betamount > 0:
                reelone = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
                reeltwo = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
                reelthree = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)

                reels = [reelone, reeltwo, reelthree]
                print("\n",reels,"\n")
                c_win = self.spinning(reels, betamount)
                slotspin = c_win


    # Leads to Ask input check. (At the bottom due to program order)
            validask = False
            while validask == False:
                answerinput = input("Would you like to play again?: ")
                validask = self.askinputcheck(answerinput)
            if answerinput == "Yes" or answerinput == "yes" or answerinput == "y":
                startagain = True
                print("You have $", c_win)
                pass
            elif answerinput == "No" or answerinput == "no" or answerinput == "n":
                startagain = False
                #self.pCredit = self.pMadeMoney
                print("You ended the game with", c_win)
                cur.execute(f"INSERT INTO Statistics VALUES (?,?,?,?,?,?,?);",(self.Uname,self.curr,self.pMadeMoney,self.MoneyLost,self.win,self.loss,current_time))
                cur.execute(f"UPDATE Player SET pCredit='{self.pCredit}' WHERE playerUserName='{self.Uname}';")
                con.commit()
                cur.close()
                break
            else:
                print("This is an incorrect input, please answer yes or no.")

            # Leads to reself.pCredit
            if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" and self.pCredit <= 0:
                break

def main(): 
    p = Player("scottha", "Scott", "Ha", 1000, 0, 0, 0, 0, 0) 

    p.my_mainloop()

    
if __name__ == "__main__":
        

    main()


    