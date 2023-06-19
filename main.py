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
    def __init__(self,)



window = Tk()
mainWindow = Tk()
mainWindow.withdraw()

input1= tk.Entry(window)
input2 = tk.Entry(window)


def createAndDestory():
    #Check data base for existing 
    print(firstN)
    print(lastN)
    print(userN)
    mainWindow.destroy()
     


def createNew():
    #mainWindow = Tk()
    mainWindow.geometry("500x500")
    tk.Label(mainWindow, text="Create New User").grid(row=0)
    tk.Label(mainWindow, text="First Name").grid(row=1)
    tk.Label(mainWindow, text="Last Name").grid(row=2)
    tk.Label(mainWindow,text= "UserName").grid(row = 3)

    inFirstName = tk.Entry(mainWindow)
    inLastName = tk.Entry(mainWindow)
    inUserName = tk.Entry(mainWindow)
    mainWindow.deiconify()

    inFirstName.grid(row=1,column=1)
    inLastName.grid(row=2,column=1)
    inUserName.grid(row=3,column=1)

    firstN = inFirstName.get() #Input for create new 
    lastN = inLastName.get()
    userN = inUserName.get()

    exit_button = Button(mainWindow, text="Create", command=createAndDestory)
    exit_button.grid(row=4,column=1)

    




def getLoginInfo():
    mainWindow = Tk()
    mainWindow.geometry("800x800")

    #loop through the data tables to check if they exist 
    userN = input1.get()
    if(userN == "1"):
        mainWindow.title("Player")
    if(userN == "2"):
        mainWindow.title("Manager")
    
    userN = ""
    
    


def main():
    window.title("WIT Casino")
    window.geometry("500x500")

    tk.Label(window, text="WIT Casino").grid(row=0)
    tk.Label(window, text="Username").grid(row=1)
    tk.Label(window, text="Password").grid(row=2)

    Loginbtn = Button(window,text="Log In",command = getLoginInfo)
    createNewUser = Button(window,text ="Create New",command = createNew)

    

    

    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    Loginbtn.grid(row=3)
    createNewUser.grid(row=3,column=1)
    window.mainloop()

    con.commit()
    con.close()

    


if __name__ == "__main__":
    
    main()