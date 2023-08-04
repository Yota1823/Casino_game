import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
import time
import os
import sqlite3
from datetime import datetime


# from main import gameScreen
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class Roulette(tk.Tk):
    def __init__(self, userMoney, pLastName, pFirstName, pUserName, pMoneyMade, pMoneyLost, pLost, pWin, casinoMoney):
        self.userMoney = userMoney
        self.pLastName = pLastName
        self.pFirstName = pFirstName
        self.pUserName = pUserName
        self.pMoneyMade = pMoneyMade
        self.pMoneyLost = pMoneyLost
        self.pLost = pLost
        self.pWin = pWin
        self.currGame = 'Roulette'
        self.casinoMoney = casinoMoney
        self.odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
        self.black = [2, 6, 4, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]
        self.green = [0]
        self.bet_option = ""
        self.bet_money = 0

        super().__init__()
        self.configure(background="gray")
        self.title("Roulette Game")
        self.geometry("1500x450")
        self.resizable(width=False, height=False)

        # Table image
        self.photo = PhotoImage(file="Games/Roulette_UI/table.png")
        Label(image=self.photo).place(relx=1, rely=1, anchor=SE)
        # button layout
        self.buttons()
        # display the user bet option
        self.bet_entry = Label(bg="gray", text="", font="Times 25 bold")
        self.bet_entry.place(x=665, y=20)
        # display roll number when user start the game
        self.roll_number = tkinter.Label(width=2, height=4, bg="white", font="Times 35 bold")
        self.roll_number.place(x=450, y=150)
        # display user bet amount
        self.bet_amount = Label(text="0", bg="gray", fg="white", font="Times 25 bold")
        self.bet_amount.place(x=110, y=100)

    # get bet option from user
    def get_bet(self, bet_opt):
        self.bet_option = str(bet_opt)
        # print(self.bet_option)
        # print(type(self.bet_option))
        self.bet_entry.configure(text="You are betting on " + str(bet_opt))

    # clear user bet option
    def clear(self):
        self.bet_option = ""
        self.bet_entry.configure(text=self.bet_option)

    # get bet amount from user
    def get_betAmount(self, bet_amt):
        if (self.bet_money + bet_amt) <= self.userMoney:
            self.bet_money += bet_amt
        else:
            tkinter.messagebox.showwarning("Warning", "Not enough fund")
        self.bet_amount.configure(text=self.bet_money)

    # clear user bet amount
    def clear_betAmount(self):
        self.bet_money = 0
        self.bet_amount.configure(text=self.bet_money)

    # start game
    def start(self):
        roll_result = random.randint(0, 36)
        # roll_result = 1
        self.roll_number.configure(text=roll_result)

        self.userMoney -= self.bet_money

        if self.bet_option == "1st 12" and 1 <= roll_result <= 13:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
            # print(self.userMoney)
        elif self.bet_option == "2nd 12" and 13 <= roll_result <= 24:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "3rd 12" and 25 <= roll_result <= 36:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "1-18" and 1 <= roll_result <= 18:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "19-36" and 19 <= roll_result <= 36:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "Black" and roll_result in self.black:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "Red" and roll_result in self.red:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "Even" and roll_result in self.even:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == "Odd" and roll_result in self.odd:
            self.userMoney += self.bet_money * 2
            self.pWin += 1
            self.pMoneyMade += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 2) +
                                        "\nNew balance: $" + str(self.userMoney))
        elif self.bet_option == str(roll_result):
            self.userMoney += self.bet_money * 35
            self.pWin += 1
            self.pMoneyMade += self.bet_money * 35 - self.bet_money
            tkinter.messagebox.showinfo("Result", "You Won $" + str(self.bet_money * 35) +
                                        "\nNew balance: $" + str(self.userMoney))
            # print(self.userMoney)
        elif self.bet_option == "":
            tkinter.messagebox.showwarning("Warning", "Please choose one bet option")
        else:
            self.pLost += 1
            self.pMoneyLost += self.bet_money
            tkinter.messagebox.showinfo("Result", "You Lost $" + str(self.bet_money) +
                                        "\nNew balance: $" + str(self.userMoney))
    
    def insert_stat(self, cur):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        cur.execute("INSERT INTO Statistics VALUES (?, ?, ?, ?, ?, ?, ?);", (self.pUserName, self.currGame, self.pMoneyMade, self.pMoneyLost, self.pWin, self.pLost, current_time))
    
    '''
    def update_credit(self, cur):
        cur.execute(f"UPDATE Player SET pCredit = ? WHERE playerUserName= ? ;", (self.userMoney, self.pUserName))
        '''

    def update_player(self,cur):
        cur.execute(f"UPDATE Player SET playerUserName = ?, playerFirstName = ?, playerLastName = ?, pCredit = ?, pMoneyMade = ?, pMoneyLost = ?,  currGame = ?, pWIn = ?, pLoss = ? WHERE playerUserName= ? ;", 
                    (self.pUserName, self.pFirstName, self.pLastName, self.userMoney, self.pMoneyMade, self.pMoneyLost, self.currGame, self.pWin, self.pLost, self.pUserName))

    def end(self):
        self.casinoMoney = self.casinoMoney + self.pMoneyLost - self.pMoneyMade
        #print(f'Casino Money: ${self.casinoMoney}')

        tkinter.messagebox.showinfo("Player Summary", "Player username: \t" + self.pUserName +
                                    "\n\nPlayer Name: \t" + self.pLastName + " " + self.pFirstName +
                                    "\n\nCurrent Game: \t" + self.currGame +
                                    "\n\nPlayer Balance: \t$" + str(self.userMoney) +
                                    "\n\nPlayer Made: \t$" + str(self.pMoneyMade) +
                                    "\n\nPlayer Lost: \t$" + str(self.pMoneyLost) +
                                    "\n\nPlayer Total Win: \t" + str(self.pWin) +
                                    "\n\nPlayer Total Lost: \t" + str(self.pLost))
        self.quit()
        self.destroy()
        # gameScreen(self, Y)

    # button layout
    def buttons(self):
        tkinter.Button(text="+ 10", width=4, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(10)).place(x=40, y=170)
        tkinter.Button(text="+ 20", width=4, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(20)).place(x=110, y=170)
        tkinter.Button(text="+ 30", width=4, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(30)).place(x=180, y=170)
        tkinter.Button(text="+ 50", width=4, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(50)).place(x=40, y=230)
        tkinter.Button(text="+ 100", width=4, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(100)).place(x=110, y=230)
        tkinter.Button(text="+ 1000", width=5, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_betAmount(1000)).place(x=180, y=230)
        tkinter.Button(text="Reset", width=7, height=0, fg="black", bg="light salmon",
                       font="Times 12 bold", command=self.clear_betAmount).place(x=100, y=290)
        # O Button
        tkinter.Button(text="0", width=2, height=4, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(0)).place(x=680, y=165)

        # Numbers Buttons
        tkinter.Button(text="1", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(1)).place(x=733, y=270)
        tkinter.Button(text="2", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(2)).place(x=733, y=195)
        tkinter.Button(text="3", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(3)).place(x=733, y=120)
        tkinter.Button(text="4", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(4)).place(x=793, y=270)
        tkinter.Button(text="5", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(5)).place(x=793, y=195)
        tkinter.Button(text="6", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(6)).place(x=793, y=120)
        tkinter.Button(text="7", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(7)).place(x=853, y=270)
        tkinter.Button(text="8", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(8)).place(x=853, y=195)
        tkinter.Button(text="9", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(9)).place(x=853, y=120)
        tkinter.Button(text="10", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(10)).place(x=910, y=270)
        tkinter.Button(text="11", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(11)).place(x=910, y=195)
        tkinter.Button(text="12", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(12)).place(x=910, y=120)
        tkinter.Button(text="13", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(13)).place(x=970, y=270)
        tkinter.Button(text="14", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(14)).place(x=970, y=195)
        tkinter.Button(text="15", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(15)).place(x=970, y=120)
        tkinter.Button(text="16", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(16)).place(x=1030, y=270)
        tkinter.Button(text="17", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(17)).place(x=1030, y=195)
        tkinter.Button(text="18", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(18)).place(x=1030, y=120)
        tkinter.Button(text="19", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(19)).place(x=1087, y=270)
        tkinter.Button(text="20", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(20)).place(x=1087, y=195)
        tkinter.Button(text="21", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(21)).place(x=1087, y=120)
        tkinter.Button(text="22", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(22)).place(x=1144, y=270)
        tkinter.Button(text="23", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(23)).place(x=1144, y=195)
        tkinter.Button(text="24", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(24)).place(x=1144, y=120)
        tkinter.Button(text="25", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(25)).place(x=1202, y=270)
        tkinter.Button(text="26", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(26)).place(x=1202, y=195)
        tkinter.Button(text="27", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(27)).place(x=1202, y=120)
        tkinter.Button(text="28", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(28)).place(x=1260, y=270)
        tkinter.Button(text="29", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(29)).place(x=1260, y=195)
        tkinter.Button(text="30", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(30)).place(x=1260, y=120)
        tkinter.Button(text="31", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(31)).place(x=1320, y=270)
        tkinter.Button(text="32", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(32)).place(x=1320, y=195)
        tkinter.Button(text="33", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(33)).place(x=1320, y=120)
        tkinter.Button(text="34", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(34)).place(x=1380, y=270)
        tkinter.Button(text="35", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(35)).place(x=1380, y=195)
        tkinter.Button(text="36", width=2, height=0, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet(36)).place(x=1380, y=120)

        # Bet on group of number Buttons
        tkinter.Button(text="1st 12", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("1st 12")).place(x=780, y=325)
        tkinter.Button(text="2nd 12", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("2nd 12")).place(x=1020, y=325)
        tkinter.Button(text="3rd 12", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("3rd 12")).place(x=1260, y=325)

        # Lower/Higher Bet
        tkinter.Button(text="1 - 18", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("1-18")).place(x=725, y=368)
        tkinter.Button(text="19 - 36", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("19 - 36")).place(x=1315, y=368)

        # Even/Odd Button
        tkinter.Button(text="Even", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("Even")).place(x=845, y=368)
        tkinter.Button(text="Odd", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("Odd")).place(x=1195, y=368)

        # Red/Black Button
        tkinter.Button(text="Red", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("Red")).place(x=962, y=368)
        tkinter.Button(text="Black", width=10, height=1, fg="black", bg="light blue",
                       font="Times 12 bold", command=lambda: self.get_bet("Black")).place(x=1080, y=368)

        # Start, reset bet option and quit the game button
        tkinter.Button(text="Start", width=10, height=1, fg="black", bg="light salmon",
                       font="Times 12 bold", command=self.start).place(x=980, y=410)
        tkinter.Button(text="Reset", width=10, height=1, fg="black", bg="light salmon",
                       font="Times 12 bold", command=self.clear).place(x=1090, y=410)
        tkinter.Button(text="Quit", width=10, height=1, fg="black", bg="light salmon",
                       font="Times 12 bold", command=self.end).place(x=1200, y=410)




# create player for testing
'''
def main_roulette():
    p1 = Roulette(100, " ", " ", " ", 0, 0, 0, 0, 1000)
    p1.mainloop()
    '''
