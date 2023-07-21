import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
import time
import os
import sqlite3 
import os.path




odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
black = [2, 6, 4, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]
green = [0]
bet_money = 0
bet_option = ""
user_balance = 100
curr_game = "Roulette"
p_username = "huyp1"
p_fname = "Huy"
p_lname = "Phan"
p_money_made = 0
p_money_lost = 0
pWin = 0;
pLost = 0;
casino_balance = 1000


roulette_ui = Tk()
roulette_ui.configure(background="gray")
roulette_ui.title("Roulette Game")
roulette_ui.geometry("1500x450"), roulette_ui.resizable(width=False, height=False)
roulette_ui.title("Roulette Game")
roulette_ui.resizable(width=False, height=False)

roulette_ui.photo = PhotoImage(file="Games/Roulette_UI/table.png")
Label(image=roulette_ui.photo).place(relx=1, rely=1, anchor=SE)


def start():
    global bet_money
    global user_balance
    global bet_money
    global pWin, pLost, p_money_lost, p_money_made
    # get random number for roll number
    roll_result = random.randint(0, 36)
    #roll_result = 1
    # print(roll_result)
    # display the roll number on UI
    rand_num.configure(text=roll_result)
    
    user_balance -= bet_money

    if bet_option == "1st 12" and 1 <= roll_result <= 12:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
        # print(user_balance)
    elif bet_option == "2nd 12" and 13 <= roll_result <= 24:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "3rd 12" and 25 <= roll_result <= 36:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "1-18" and 1 <= roll_result <= 18:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "19-36" and 19 <= roll_result <= 36:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "Red" and roll_result in red:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "Black" and roll_result in black:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "Even" and roll_result in even:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "Odd" and roll_result in odd:
        user_balance += bet_money * 2
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 2) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_option == "":
        tkinter.messagebox.showwarning("Warning", "Please choose one bet option")
    elif bet_option == str(roll_result):
        user_balance += bet_money * 35
        pWin += 1
        p_money_made += bet_money
        tkinter.messagebox.showinfo("Result", "You won $" + str(bet_money * 35) +
                                        "\nNew balance: $" + str(user_balance))
    elif bet_money == 0:
        tkinter.messagebox.showwarning("Warning", "Please enter your bet money!")
    else:
        pLost += 1
        p_money_lost += bet_money
        tkinter.messagebox.showinfo("Result", "You Lost $" + str(bet_money) +
                                        "\nNew balance: $" + str(user_balance))


def get_bet(bet_opt):
    global bet_option
    bet_option = str(bet_opt)
    bet_entry.configure(text="You are betting on " + bet_option)


def clear():
    global bet_option
    bet_option = ""
    bet_entry.configure(text=bet_option)


def get_betAmount(bet_amt):
    global bet_money
    if (bet_money + bet_amt) <= user_balance:
        bet_money += bet_amt
    else:
        tkinter.messagebox.showwarning("Warning", "Not enough fund")
    bet_amount.configure(text=bet_money)


def clear_betAmount():
    global bet_money
    bet_money = 0
    bet_amount.configure(text=bet_money)

def end():
    global pWin, pLost, p_money_lost, p_money_made, casino_balance
    global p_username, curr_game

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #print(current_time)

    cur.execute("INSERT INTO Statistics VALUES (?, ?, ?, ?, ?, ?, ?)", (p_username, curr_game, p_money_made, p_money_lost, pWin, pLost, current_time))
    
    '''
    insert_stats = "INSERT INTO Statistics (playerUserName, gamePlayed, moneyMade, moneyLost, playerWin, playerLost, timeStamp) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    insert_val = (p_username, curr_game, p_money_made, p_money_lost, pWin, pLost, current_time)
    cur.execute(insert_stats, insert_val)
    '''

    '''
    insert_stats = ("INSERT INTO Statistics (playerUserName, gamePlayed, moneyMade, moneyLost, playerWin, playerLost, timeStamp) VALUES (%(playerUserName)s, %(gamePlayed)s, %(moneyMade)s, %(moneyLost)s, %(playerWin)s, %(playerLost)s, %(timeStamp)s);")
    insert_val = {
        'playerUserName' : p_username,
        'gamePlayer' : curr_game,
        'moneyMade' : p_money_made,
        'moneyLost' : p_money_lost,
        'playerWin' : pWin,
        'playerLost' : pLost,
        'timeStamp' : current_time}
    cur.execute(insert_stats, insert_val)
    '''
    
    casino_balance = casino_balance + p_money_made - p_money_lost
    print(f'Casino Money: ${casino_balance}')
    tkinter.messagebox.showinfo("Player Summary", "Player username: \t" + p_username +
                                    "\n\nPlayer Name: \t" + p_lname + " " + p_fname +
                                    "\n\nCurrent Game: \t" + curr_game +
                                    "\n\nPlayer Balance: \t$" + str(user_balance) +
                                    "\n\nPlayer Made: \t$" + str(p_money_made) +
                                    "\n\nPlayer Lost: \t$" + str(p_money_lost) +
                                    "\n\nPlayer Total Win: \t" + str(pWin) +
                                    "\n\nPlayer Total Lost: \t" + str(pLost))
    roulette_ui.destroy()


bet_amount = Label(roulette_ui, text="", bg="gray", fg="white", font="Times 25 bold")
bet_amount.place(x=110, y=100)

tkinter.Button(master=roulette_ui, text="+ 10", width=4, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(10)).place(x=40, y=170)
tkinter.Button(master=roulette_ui, text="+ 20", width=4, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(20)).place(x=110, y=170)
tkinter.Button(master=roulette_ui, text="+ 30", width=4, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(30)).place(x=180, y=170)
tkinter.Button(master=roulette_ui, text="+ 50", width=4, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(50)).place(x=40, y=230)
tkinter.Button(master=roulette_ui, text="+ 100", width=4, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(100)).place(x=110, y=230)
tkinter.Button(master=roulette_ui, text="+ 1000", width=5, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_betAmount(1000)).place(x=180, y=230)
tkinter.Button(roulette_ui, text="Reset", width=7, height=0, fg="black", bg="light salmon",
               font="Times 12 bold", command=clear_betAmount).place(x=100, y=290)


bet_entry = Label(roulette_ui, bg="gray", text="", font="Times 25 bold")
bet_entry.place(x=665, y=20)
# bet_entry.insert(0, "You are betting on: ")

rand_num = tkinter.Label(roulette_ui, text="", bg="white", font="Times 35 bold")
rand_num.place(x=450, y=230)

# O Button
tkinter.Button(roulette_ui, text="0", width=2, height=4, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(0)).place(x=680, y=165)

# Numbers Buttons
tkinter.Button(master=roulette_ui, text="1", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(1)).place(x=733, y=270)
tkinter.Button(master=roulette_ui, text="2", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(2)).place(x=733, y=195)
tkinter.Button(master=roulette_ui, text="3", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(3)).place(x=733, y=120)
tkinter.Button(master=roulette_ui, text="4", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(4)).place(x=793, y=270)
tkinter.Button(master=roulette_ui, text="5", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(5)).place(x=793, y=195)
tkinter.Button(master=roulette_ui, text="6", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(6)).place(x=793, y=120)
tkinter.Button(master=roulette_ui, text="7", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(7)).place(x=853, y=270)
tkinter.Button(master=roulette_ui, text="8", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(8)).place(x=853, y=195)
tkinter.Button(master=roulette_ui, text="9", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(9)).place(x=853, y=120)
tkinter.Button(master=roulette_ui, text="10", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(10)).place(x=910, y=270)
tkinter.Button(master=roulette_ui, text="11", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(11)).place(x=910, y=195)
tkinter.Button(master=roulette_ui, text="12", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(12)).place(x=910, y=120)
tkinter.Button(master=roulette_ui, text="13", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(13)).place(x=970, y=270)
tkinter.Button(master=roulette_ui, text="14", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(14)).place(x=970, y=195)
tkinter.Button(master=roulette_ui, text="15", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(15)).place(x=970, y=120)
tkinter.Button(master=roulette_ui, text="16", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(16)).place(x=1030, y=270)
tkinter.Button(master=roulette_ui, text="17", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(17)).place(x=1030, y=195)
tkinter.Button(master=roulette_ui, text="18", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(18)).place(x=1030, y=120)
tkinter.Button(master=roulette_ui, text="19", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(19)).place(x=1087, y=270)
tkinter.Button(master=roulette_ui, text="20", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(20)).place(x=1087, y=195)
tkinter.Button(master=roulette_ui, text="21", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(21)).place(x=1087, y=120)
tkinter.Button(master=roulette_ui, text="22", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(22)).place(x=1144, y=270)
tkinter.Button(master=roulette_ui, text="23", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(23)).place(x=1144, y=195)
tkinter.Button(master=roulette_ui, text="24", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(24)).place(x=1144, y=120)
tkinter.Button(master=roulette_ui, text="25", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(25)).place(x=1202, y=270)
tkinter.Button(master=roulette_ui, text="26", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(26)).place(x=1202, y=195)
tkinter.Button(master=roulette_ui, text="27", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(27)).place(x=1202, y=120)
tkinter.Button(master=roulette_ui, text="28", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(28)).place(x=1260, y=270)
tkinter.Button(master=roulette_ui, text="29", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(29)).place(x=1260, y=195)
tkinter.Button(master=roulette_ui, text="30", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(30)).place(x=1260, y=120)
tkinter.Button(master=roulette_ui, text="31", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(31)).place(x=1320, y=270)
tkinter.Button(master=roulette_ui, text="32", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(32)).place(x=1320, y=195)
tkinter.Button(master=roulette_ui, text="33", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(33)).place(x=1320, y=120)
tkinter.Button(master=roulette_ui, text="34", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(34)).place(x=1380, y=270)
tkinter.Button(master=roulette_ui, text="35", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(35)).place(x=1380, y=195)
tkinter.Button(master=roulette_ui, text="36", width=2, height=0, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet(36)).place(x=1380, y=120)

# Bet on group of number Buttons
tkinter.Button(master=roulette_ui, text="1st 12", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("1st 12")).place(x=780, y=325)
tkinter.Button(master=roulette_ui, text="2nd 12", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("2nd 12")).place(x=1020, y=325)
tkinter.Button(master=roulette_ui, text="3rd 12", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("3rd 12")).place(x=1260, y=325)

# Lower/Higher Bet
tkinter.Button(master=roulette_ui, text="1 - 18", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("1-18")).place(x=725, y=368)
tkinter.Button(master=roulette_ui, text="19 - 36", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("19 - 36")).place(x=1315, y=368)

# Even/Odd Button
tkinter.Button(master=roulette_ui, text="Even", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("Even")).place(x=845, y=368)
tkinter.Button(master=roulette_ui, text="Odd", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("Odd")).place(x=1195, y=368)

# Red/Black Button
tkinter.Button(master=roulette_ui, text="Red", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("Red")).place(x=962, y=368)
tkinter.Button(master=roulette_ui, text="Black", width=10, height=1, fg="black", bg="light blue",
               font="Times 12 bold", command=lambda: get_bet("Black")).place(x=1080, y=368)

# Start, reset bet option and quit the game button
tkinter.Button(master=roulette_ui, text="Start", width=10, height=1, fg="black", bg="light salmon",
               font="Times 12 bold", command=start).place(x=980, y=410)
tkinter.Button(master=roulette_ui, text="Reset", width=10, height=1, fg="black", bg="light salmon",
               font="Times 12 bold", command=clear).place(x=1090, y=410)
tkinter.Button(master=roulette_ui, text="Quit", width=10, height=1, fg="black", bg="light salmon",
               font="Times 12 bold", command=lambda: end()).place(x=1200, y=410)

def insert_stat():
    global pWin, pLost, p_money_lost, p_money_made
    global p_username, curr_game

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    cur.execute("INSERT INTO Statistics VALUES (?, ?, ?, ?, ?, ?, ?)", (p_username, curr_game, p_money_made, p_money_lost, pWin, pLost, current_time))


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Casino.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    roulette_ui.mainloop()
    print("quit roulette, insert data")
    insert_stat(con)