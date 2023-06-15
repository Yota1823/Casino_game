from tkinter import *
import tkinter as tk

import sqlite3 
con = sqlite3.connect("Casino.db")
cur = con.cursor()
#cur.execute("INSERT INTO STUDENT VALUES(101,'Kaleb','Pelletier','COMP_ENG','pelletierk3@wit.edu',2024);")



window = Tk()
mainWindow = Tk()
mainWindow.withdraw()

input1= tk.Entry(window)
input2 = tk.Entry(window)


def createAndDestory():
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

    FirstN = inFirstName.get() #Input for create new 
    LastN = inLastName.get()
    UserN = inUserName.get()




    exit_button = Button(mainWindow, text="Exit", command=createAndDestory)
    exit_button.grid(row=4,column=1)

    #Check data base for existing 




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