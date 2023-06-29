import sqlite3
import random
import sys


balance = 1000
balance == int(balance)
winnings = 0
winnings == int(winnings)

Symbols = ["Leopard", "wit shield", "W lines", "Big W", "7"]

# Subroutines:  Checking the Bet input and amount
def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount == int(betamount)
        rightbet = True
    else: 
        rightbet = False
        "Please enter a whole number, no decimals and a bet on or below the balance."
    return rightbet

# Limiting the bet
def betlimit(betamount):
    if betamount > balance == False:
        goodlimit = False
        "That bet is too high!"
    else:
        goodlimit = True
    return goodlimit

# Checking the 'Ask' input to play the machine.
def askinputcheck(answerinput):
    if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" or answerinput == "No" or answerinput == "no" or answerinput == "n":
        rightanswerinput = True
    else:
        rightanswerinput = False
        "This is an incorrect input, please type an appropriate answer in."
    return rightanswerinput

# Printing and sorting symbols.
def spinning(reels):
    global balance
    if reelone == "Leopard" and reeltwo == "Leopard" and reelthree == "Leopard":
        winnings = int(betamount) + int(balance) * 100
        "You won the jackpot! Congragulations! This is how much your account contains $", winnings
    elif reelone == "Goldbar" and reeltwo == "Goldbar" and reelthree == "Goldbar":
        winnings = int(betamount) + int(balance) * 500
        "You won a considerable return! Awesome! Your balance and wins are $", winnings
    elif reelone == "Pyramid" and reeltwo == "Pyramid" and reelthree == "Pyramid":
        winnings = int(betamount) + int(balance) * 250
        "You won a good return! Its a conspiracy! This is all of your money total $", winnings
    elif reelone == "Blackcat" and reeltwo == "Blackcat" and reelthree == "Blackcat":
        winnings = int(balance) - int(betamount)
        "Unfortunately you didn't win anything, bad luck! You rewards are $", winnings
    else:
        winnings = int(balance) - int(betamount)
        "Bad luck! Maybe next time you'll win! Your remaining cash is $", winnings
        winnings
    return reels

# If you have no money
def rebalance(balance):        
    while balance == 0 == True and startagain == True:
        unbalance = True
        balance = 1000
        "You ran out of money, here is $1000"
    else:
        unbalance = False
        "You still have money."
        return unbalance

# Leads to Bet input check. 
Validbet = False
while Validbet == False:
    betamount = input("Please enter amount you wish to bet: ")
    Validbet = betcheck(betamount)

betamount == int(betamount)

# Leads to betlimit
appropriatelimit = betlimit(betamount)

# RandomSymbolGen + 3 reels
reelone = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)
reeltwo = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)
reelthree = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)

reels = [reelone, reeltwo, reelthree]

slotspin = spinning(reels)

reels

# Leads to Ask input check. (At the bottom due to program order)
validask = False
while validask == False:
    answerinput = raw_input("Would you like to play again?: ")
    validask = askinputcheck(answerinput)

# Leads to restart    
startagain = False
while startagain == False:
    startagain = answerinput

while True: 
    if answerinput == "Yes" or answerinput == "yes" or answerinput == "y":
        startagain = True
        balance = int(winnings) + int(balance)
        "You have $", balance
        pass
    elif answerinput == "No" or answerinput == "no" or answerinput == "n":
        startagain = False
        balance = winnings
        "You ended the game with", balance
        break
    else:
        "This is an incorrect input, please answer yes or no."


# Leads to rebalance
if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" and balance == 0:
    balance = rebalance(balance)




    