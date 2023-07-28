import random
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
#import numpy as np
from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
#import randomtimestamp
#from randomtimestamp import random_time
#import names
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


    def refillMoney(self, window):
        window.destroy()
        self.creditAmount = self.creditAmount + 500
        cur.execute("UPDATE Player SET pCredit = ? WHERE playerUserName = ?;", (self.creditAmount, self.uName))
        cur.execute("UPDATE Manager SET totalCasinoMoney = totalCasinoMoney + 500;")
        con.commit()
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


def statGraph():
    statgraph_win = Toplevel(my_w)
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares

    plot1 = fig.add_subplot(111)
    cur.execute("SELECT pMoneyMade FROM Statistics")
    points_mm = cur.fetchall()
    cur.execute("SELECT pMoneyLost FROM Statistics")
    points_ml = cur.fetchall()
    print(type(points_mm[0][0]))

    for i in range(len(points_mm)):
        plot1.scatter(i, points_mm[i][0], color="g")
        plot1.scatter(i, points_ml[i][0], color="r")
    # for i in range(len(points_mm)):
    #     plot1.plot(points_mm[i][0])
    #     plot1.plot(points_ml[i][0])

    # y = [i**2 for i in range(101)]
    # adding the subplot
    # plot1 = fig.add_subplot(111)
    # plotting the graph
    # plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=statgraph_win)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   statgraph_win)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def barGraph():
    statgraph_win = Toplevel(my_w)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # list of squares
    y = [i**2 for i in range(101)]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    #plot1.plot(y)
    cur.execute(f"SELECT SUM(pWin) FROM Statistics")
    winSum = cur.fetchall()
    cur.execute(f"SELECT SUM(pLoss) FROM Statistics")
    lossSum = cur.fetchall()


    fig = Figure(figsize=(5, 5), dpi=100)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = statgraph_win)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   statgraph_win)
    toolbar.update()
    plot1 = fig.add_subplot()
    # placing the toolbar on the Tkinter window
    print(type(lossSum), type(winSum))
    plot1.bar('Losses', lossSum[0])
    plot1.bar('Wins', winSum[0])
    plot1.set_title("Casino Wins Vs Losses")
    plot1.set_ylabel("Amount")


    canvas.get_tk_widget().pack()

     

def generate():
    games = ["Solitaire", "Blackjack", "Baccarat", "Slots", "Roulette"]
    x = 0


    for x in range(100):
        fname = names.get_first_name()
        lname = names.get_last_name()
        uname = fname[0] + lname
        game = games[random.randrange(0,4,1)]
        buyin = random.randrange(10, 2000, 5)
        made = random.randrange(0, 2000, 5)
        lost = random.randrange(0, 2000, 5)
        win = random.randrange(0, 10, 1)
        losses = random.randrange(0, 10, 1)
        time = str(random_time(text=True, pattern='%I:%M'))
        print(type(fname))
        print(type(losses))
        print(type(time))
        print(time)

        cur.execute("INSERT INTO Statistics VALUES ( ?, ?, ?,  ?, ?, ?, ?)",(uname, game,made,lost,win,losses,time) )

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

    if status == 'N':
        b1 = tk.Button(game_window, text=' Blackjack ',command= lambda:blackJack()).grid(row=0,column=0)
        b2 = tk.Button(game_window, text=' Roulette ',command= lambda:Roulette(player)).grid(row=1,column=0)
        b3 = tk.Button(game_window, text=' Baccarat ',command= lambda:baccarat(player)).grid(row=2,column=0)
        b4 = tk.Button(game_window, text=' Slots ',command= lambda:slots(player)).grid(row=3,column=0)
        b5 = tk.Button(game_window, text=' Solitaire ',command= lambda:solitaire()).grid(row=4,column=0)
        b6 = tk.Button(game_window, text=' Refill ',command= lambda:[player.refillMoney(game_window), gameScreen(player,status)]).grid(row=1,column=20)

    if status == 'Y':
        b7 =tk.Button(game_window, text=' Statistics ',command= lambda:stats()).grid(row=5,column=0)
        tk.Button(game_window, text = "Statistics Line Graph", command=lambda:statGraph()).grid(row=9, column=0)
        tk.Button(game_window, text = 'Statistics Bar Graph', command=lambda:barGraph()).grid(row= 8, column=0)
        b8 = tk.Button(game_window,text=' Remove Player ',command= lambda:removePlayer(player)).grid(row=6,column=0)
        b9 = tk.Button(game_window, text=' Generate ', command=lambda: generate()).grid(row=7, column=0)
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


def slots(player):
    

    # Import the specific functions or classes from the blackjack module
    #inputTxt = tk.Text(slots,height=20,width=80).grid(row=1,column=2)

    from peruzzislots import Player
    p = Player(player.getUser(),player.getFirst(),player.getLast(),
                  player.getCredit(),player.getMoneyMade(),player.getMoneyLost(),player.getpWin(),player.getpLoss(),1000)
    
    p.my_mainloop()

def baccarat(player):
    #print(os.path.abspath(__file__))
    #blackjack_dir = os.path.join(BASE_DIR, "Games/Baccarat/Casino_project_Baccarat_game.py")
    #game_dir = os.path.join(blackjack_dir, 'Games/Baccarat')
    #sys.path.append(game_dir)

    #subprocess.run(["python", "Games/Baccarat/Casino_project_Baccarat_game.py"])
    # from Games.Baccarat.Casino_project_Baccarat_game import Cli
    # Cli.run()
    from Games.Baccarat.Baccarat import Baccarat
    p1 = Baccarat(player.getCredit(),player.getLast(),player.getFirst(),
                  player.getUser(),player.getMoneyMade(),player.getMoneyLost(),player.getpLoss(),player.getpWin())
    p1.run()


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
    #insert player stats to db
    #pass in cursor
    p1.insert_stat(cur)
    #update player credit to db
    #p1.update_credit(cur)
    p1.update_player(cur)
    con.commit()
    main()
    my_login(player.getFirst())



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
    my_str1.set("User Name")
    l2 = tk.Label(my_w_child, text="First Name")
    l2.grid(row=2,column=2)
    l3 = tk.Label(my_w_child, text= "Last Name")
    l3.grid(row=3,column=2)
    b3 = tk.Button(my_w_child, text=' Create ',
                   command= lambda:[create(inFirstName.get(),inLastName.get(),inUserName.get()),my_w_child.destroy()])
    b3.grid(row=4,column=1)



def main():
    global my_w
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
    b1.grid(row=4,column=1)

    b2 = tk.Button(my_w, text='Login',
                   command=lambda:my_login(input1.get()))
    b2.grid(row=5,column=1)
    my_w.mainloop()

    


if __name__ == "__main__":
    main()