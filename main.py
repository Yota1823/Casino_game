from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess

import sys
import os
import sqlite3 
import os.path
import Games


import subprocess
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Casino.db")
con = sqlite3.connect(db_path)
cur = con.cursor()
#cur.execute("INSERT INTO STUDENT VALUES(101,'Kaleb','Pelletier','COMP_ENG','pelletierk3@wit.edu',2024);")
class User:
    def __init__(self,fName,lName,uName):
        self.name = fName
        self.last = lName
        self.user = uName

    def getFirst(self):
        return self.name
    def getLast(self):
        return self.last
    def getUser(self):
        return self.user
    

    # def __del__(self):
    #     print(self.name + " is deleted")
        #del obj

class Player(User):
    
    def __init__(self,uName,fName,lName,pCredit,pMoneyMade,pMoneyLost,currGame,pWin,pLoss):
        User.__init__(self,fName,lName,uName)
        
        self.creditAmount = pCredit
        self.moneyMade = pMoneyMade
        self.moneyLost = pMoneyLost
        self.currentGame = currGame
        self.winCount = pWin
        self.lossCount = pLoss
        self.uName = uName


    def createPlayer(self):
        cur.execute("INSERT INTO Player VALUES('"+self.user+"','"+self.name+"','"+self.last+"',"+
                self.creditAmount+","+self.moneyMade+","+self.moneyLost+",'"+self.currentGame+"',"+self.winCount+","+
                self.lossCount+");")#","+self.creditAmount+");")


    def refillMoney(self):
        self.creditAmount = self.creditAmount + 500
        cur.execute("UPDATE PLayer SET pCredit = ? WHERE playerUserName = ?;", (self.creditAmount, self.uName))
        # Refill Gives Player more money, still needs to add the money to the casino profits
        print("refill")
    def getMoneyMade(self):
        return self.moneyMade
    def getMoneyLost(self):
        return self.moneyLost
    def getCurrGame(self):
        return self.currentGame
    def getpWin(self):
        return self.winCount
    def getpLoss(self):
        return self.lossCount
    def getCredit(self):
        return self.creditAmount
    
    
class Manager(User):
    def __init__(self,manUserN,pUserN,pMoneyMade,pMoneyLost,totalCasinoMoney,
                 totalPlayerMoney,currGame,hitListStatus):
        self.manUN = manUserN
        self.pUN = pUserN
        self.pMM = pMoneyMade
        self.pML = pMoneyLost
        self.totalCasinoM = totalCasinoMoney
        self.totalPlayerM = totalPlayerMoney
        self.currGame = currGame
        self.hitLS = hitListStatus
    def removePlayer(self, userName):
        cur.execute("DELETE FROM Player WHERE playerUserName='"+userName+"';")
        con.commit()

    def getPlayerTable(self):
        cur.execute("SELECT * FROM Player")
        playerTable = cur.fetchall()
        return playerTable

    def getStatTable(self):
        cur.execute("SELECT * FROM Statistics")
        statTable = cur.fetchall()
        return statTable



my_w = tk.Tk()
my_w.geometry("250x250")  # Size of the window
my_w.title("WIT CASINO")  # Adding a title

# create one lebel
my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str )
l1.grid(row=1,column=1)
my_str.set("Welcome to the WIT Casino")
tk.Label(my_w, text="Username").grid(row=2, column=2)



input1 = tk.Entry(my_w)

input1.grid(row=2, column=1)


# add one button
b1 = tk.Button(my_w, text='Create New User',
               command=lambda:my_open())
b1.grid(row=5,column=1)

b2 = tk.Button(my_w, text='Login',
               command=lambda:my_login(input1.get()))
b2.grid(row=4,column=1)

#window = Tk()
#mainWindow = Tk()
# mainWindow.withdraw()

# input1= tk.Entry(window)
# input2 = tk.Entry(window)

def stats():
    stat_win = Toplevel(my_w)
    stat_win.geometry("1700x800")
    stat_win.title("Casino Statistics")

    tree = ttk.Treeview(stat_win,columns=("c1","c2","c3","c4","c5","c6","c7",), show='headings')
    tree.column("#1",anchor=tk.CENTER)
    tree.heading("#1",text="playerUserName")

    tree.column("#2",anchor=tk.CENTER)
    tree.heading("#2",text="currGame")

    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="pMoneyMade")

    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="pMoneyLost")

    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="pWin")

    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="pLost")

    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="timeStamp")

    tree.pack()


    cur.execute(f"SELECT * FROM Statistics;")
    all_stats = cur.fetchall()

    for stats in all_stats:
        print(stats)
        tree.insert("",tk.END,values=stats)

    con.commit()


def my_login(first):
    print("doing the login ")

    statement = f"SELECT managerUserName from Manager WHERE managerUserName='{first}';"
    output = cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
         
         statement = f"SELECT playerUserName from Player WHERE playerUserName='{first}';"
         cur.execute(statement)
         if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
         else:
            print("Welcome")

            cur.execute(f"SELECT * from Player WHERE playerUserName='{first}';")
            playerData = cur.fetchall()
            p = Player(playerData[0][0],playerData[0][1],playerData[0][2],playerData[0][3],
                   playerData[0][4],playerData[0][5],playerData[0][6],playerData[0][7],playerData[0][8])
        
        
            gameScreen(p,'N')
         
    else:
        print("Welcome Manager")
        cur.execute(f"SELECT * from Manager WHERE managerUserName='{first}';")
        managerData = cur.fetchall()
        m = Manager(managerData[0][0],managerData[0][1],managerData[0][2],managerData[0][3],managerData[0][4],
                    managerData[0][5],managerData[0][6],managerData[0][7])
        gameScreen(m,'Y')

    

def create(first,last,user):
    print("database creating things")
    statement = f"SELECT playerUserName from Player WHERE playerUserName='{user}';"
    cur.execute(statement)
    if cur.fetchone():  # An empty result evaluates to False.
        print("User Name Taken")
        
    else:
        print("Welcome")
        p = Player(first,last,user,"500","0","0","0","0","0")
        p.createPlayer()
        con.commit()
    
def gameScreen(player,status): #Pass player
    game_window = Toplevel(my_w)
    game_window.geometry("250x250")
    game_window.title("Main Game Menu")

    b1 = tk.Button(game_window, text=' Blackjack ',command= lambda:blackJack()).grid(row=0,column=0)
    b3 = tk.Button(game_window, text=' Baccarat ',command= lambda:baccarat()).grid(row=2,column=0)
    b2 = tk.Button(game_window, text=' Roulette ',command= lambda:Roulette(player)).grid(row=1,column=0)
    b3 = tk.Button(game_window, text=' Baccarat ',command= 0).grid(row=2,column=0)
    b4 = tk.Button(game_window, text=' Slots ',command= lambda:slots()).grid(row=3,column=0)
    b5 = tk.Button(game_window, text=' Solitaire ',command= lambda:solitaire()).grid(row=4,column=0)
    b6 = tk.Button(game_window, text=' Refill ',command= lambda:player.refillMoney()).grid(row=1,column=20)

    if status == 'Y':
        b7 =tk.Button(game_window, text=' Statistics ',command= lambda:stats()).grid(row=5,column=0)
        b8 = tk.Button(game_window,text=' Remove Player ',command= lambda:removePlayer(player)).grid(row=6,column=0)

    else:
        balance = tk.Label(game_window, text = str(player.getCredit())).grid(row=0,column=5) #GET THIS WORKING

    # b9 = tk.Button(game_window, text=' Refill ',command= 0).grid(row=1,column=20)

def removePlayer(manager):
    remplayer_win = Toplevel(my_w)
    remplayer_win.geometry("700x500")
    remplayer_win.title("Remove Player")
    # inputTxt = tk.Text(remplayer_win,height=20,width=80).grid(row=1,column=2)

    # text = tk.Label(remplayer_win ,manager.getPlayerTable()).grid()
    print(manager.getPlayerTable())
    print(len(manager.getPlayerTable()))
    for x in range(len(manager.getPlayerTable())):
        print(manager.getPlayerTable()[x])
        print(type(manager.getPlayerTable()[x]))
        name = str(manager.getPlayerTable()[x][0])
        label = tk.Label(remplayer_win, text=str(manager.getPlayerTable()[x])).grid(row = x, column = 0)
        button = tk.Button(remplayer_win, text="Remove " + name, command=lambda:manager.removePlayer(str(manager.getPlayerTable()[x][0]))).grid(row=x, column=1)
        print((manager.getPlayerTable()[x][0]))



def blackJack():

    from Games.blackjack import main
    main()


def slots():
    

    # Import the specific functions or classes from the blackjack module
    inputTxt = tk.Text(slots,height=20,width=80).grid(row=1,column=2)
    from peruzzislots import my_mainloop
    my_mainloop()

def baccarat():
    #print(os.path.abspath(__file__))
    #blackjack_dir = os.path.join(BASE_DIR, "Games/Baccarat/Casino_project_Baccarat_game.py")
    #game_dir = os.path.join(blackjack_dir, 'Games/Baccarat')
    #sys.path.append(game_dir)

    subprocess.run(["python", "Games/Baccarat/Casino_project_Baccarat_game.py"])
    from Games.Baccarat.Casino_project_Baccarat_game import Cli
    Cli.run()


def solitaire():
    dir = os.path.join(BASE_DIR, "Games/Solitair/solitair.py")
    game_dir = os.path.join(dir, 'Games/Solitair')
    sys.path.append(game_dir)

    subprocess.run(["python", "Games/Solitair/game.py"])

def Roulette(player):
    my_w.destroy()
    from Games.Roulette_UI.roulette import Roulette
    p1 = Roulette(player.getCredit(),player.getLast(),player.getFirst(),
                  player.getUser(),player.getMoneyMade(),player.getMoneyLost(),player.getpLoss(),player.getpWin(),1000)
    
    p1.mainloop()
    main()


def my_open():
    my_w_child=Toplevel(my_w) # Child window
    my_w_child.geometry("250x250")  # Size of the window
    my_w_child.title("New User Screen")

    inFirstName = tk.Entry(my_w_child)
    inLastName = tk.Entry(my_w_child)
    inUserName = tk.Entry(my_w_child)

    inFirstName.grid(row=1, column=1)
    inLastName.grid(row=2, column=1)
    inUserName.grid(row=3, column=1)

    # firstN = inFirstName.get()  # Input for create new
    # lastN = inLastName.get()
    # userN = inUserName.get()
    
    my_str1 = tk.StringVar()

    l1 = tk.Label(my_w_child,  textvariable=my_str1 )
    l1.grid(row=1,column=2)
    my_str1.set("User Name")
    l2 = tk.Label(my_w_child, text="First Name")
    my_str1.set("Username")
    l2 = tk.Label(my_w_child, text="Firstname")
    l2.grid(row=2,column=2)
    l3 = tk.Label(my_w_child, text= "User Name")
    l3.grid(row=3,column=2)
    b3 = tk.Button(my_w_child, text=' Create ',
                   command= lambda:[create(inFirstName.get(),inLastName.get(),inUserName.get()),my_w_child.destroy()])
    b3.grid(row=4,column=1)



def main():
    my_w.mainloop()
    


if __name__ == "__main__":
    main()