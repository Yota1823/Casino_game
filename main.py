from tkinter import *
import tkinter as tk

import sqlite3 
#con = sqlite3.connect("assignment3.db")
#cur = con.cursor()
#cur.execute("INSERT INTO STUDENT VALUES(101,'Kaleb','Pelletier','COMP_ENG','pelletierk3@wit.edu',2024);")
#con.commit()
#con.close()


window = Tk()

#mainWindow = Toplevel()
#mainWindow.withdraw() #Hides window

input1= tk.Entry(window)
input2 = tk.Entry(window)

def createNew():
    mainWindow = Toplevel()
    mainWindow.geometry("500x500")
    tk.Label(mainWindow, text="Create New User").grid(row=0)
    tk.Label(mainWindow, text="First Name").grid(row=1)
    tk.Label(mainWindow, text="Last Name").grid(row=2)
    tk.Label(mainWindow,text= "UserName").grid(row = 3)


def getLoginInfo():
    mainWindow = Toplevel()
    mainWindow.geometry("800x800")

    #loop through the data tables to check if they exist 
    userN = input1.get()
    if(userN == "1"):
        mainWindow.title("Player")
    if(userN == "2"):
        mainWindow.title("Manager")
    
    userN = ""
    mainWindow.deiconify() #Shows window
    #mainWindow.mainloop()
    


    #tk.Label(window, text=userN).grid(row=4)
    


def main():
    window.title("WIT Casino")
    window.geometry("500x500")

    tk.Label(window, text="WIT Casino").grid(row=0)
    tk.Label(window, text="Username").grid(row=1)
    tk.Label(window, text="Password").grid(row=2)

    Loginbtn = Button(window,text="Log In",command = getLoginInfo)
    createNewUser = Button(window,text ="Create New",command = createNew)

    

    # username = input1.get()
    # password = input2.get()
    # if(username != "" ):
    #     mainWindow = Tk()

    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    Loginbtn.grid(row=3)
    createNewUser.grid(row=3,column=1)
    window.mainloop()

    


if __name__ == "__main__":
    
    main()