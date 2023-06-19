from tkinter import *
import tkinter as tk

import sqlite3 
con = sqlite3.connect("Casino.db")
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
    

    def __del__(self):
        print(self.name + " is deleted")
        #del obj

class Player(User):
    def __init__(self,pMoneyMade,pMoneyLost,currGame,pWin,pLoss,pCredit):
        self.moneyMade = pMoneyMade
        self.moneyLost = pMoneyLost
        self.currentGame = currGame
        self.winCount = pWin
        self.lossCount = pLoss
        self.creditAmount = pCredit
        cur.execute("INSERT INTO Player VALUES('"+self.user+"','"+self.name+"','"+self.last+"',"+
                    self.moneyMade+","+self.moneyLost+",'"+self.currentGame+"',"+self.winCount+","+
                    self.lossCount+","+self.creditAmount+");")



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
    def __init__(self):
        pass
    def removePlayer(userName):
        cur.execute("DELETE FROM Player WHERE playerUserName='"+userName+"';")

    def getPlayerTable():
        cur.execute("SELECT * FROM Player")
        playerTable = cur.fetchall()
        return playerTable

    def getStatTable():
        cur.execute("SELECT * FROM Statistics")
        statTable = cur.fetchall()
        return statTable



my_w = tk.Tk()
my_w.geometry("200x200")  # Size of the window
my_w.title("WIT CASINO")  # Adding a title

# create one lebel
my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str )
l1.grid(row=1,column=1)
my_str.set("Welcome to the WIT Casino")
tk.Label(my_w, text="Username").grid(row=2, column=2)
tk.Label(my_w, text="Password").grid(row=3, column=2)


input1 = tk.Entry(my_w)
input2 = tk.Entry(my_w)

input1.grid(row=2, column=1)
input2.grid(row=3, column=1)

# add one button
b1 = tk.Button(my_w, text='Create New User',
               command=lambda:my_open())
b1.grid(row=4,column=1)

b2 = tk.Button(my_w, text='Login',
               command=lambda:my_login())
b2.grid(row=5,column=1)

window = Tk()
mainWindow = Tk()
mainWindow.withdraw()

input1= tk.Entry(window)
input2 = tk.Entry(window)

def my_login():
    print("doing the login stuff")

def create(first,last,user):
    print("database creating things")
    print(first)
    print(last)
    print(user)
def my_open():
    my_w_child=Toplevel(my_w) # Child window
    my_w_child.geometry("200x200")  # Size of the window
    my_w_child.title("www.plus2net.com")

    inFirstName = tk.Entry(my_w_child)
    inLastName = tk.Entry(my_w_child)
    inUserName = tk.Entry(my_w_child)

    inFirstName.grid(row=1, column=1)
    inLastName.grid(row=2, column=1)
    inUserName.grid(row=3, column=1)

    firstN = inFirstName.get()  # Input for create new
    lastN = inLastName.get()
    userN = inUserName.get()
    my_str1 = tk.StringVar()

    l1 = tk.Label(my_w_child,  textvariable=my_str1 )
    l1.grid(row=1,column=2)
    my_str1.set("USERNAME")
    l2 = tk.Label(my_w_child, text="PASSWORD")
    l2.grid(row=2,column=2)
    l3 = tk.Label(my_w_child, text= "USERNAME")
    l3.grid(row=3,column=2)
    b3 = tk.Button(my_w_child, text=' Create ',
                   command= lambda:[my_w_child.destroy(),create(firstN,lastN,userN)])
    b3.grid(row=4,column=1)






def main():
    my_w.mainloop()

    


if __name__ == "__main__":
    
    main()