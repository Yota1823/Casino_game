import sqlite3
import random
import sys


balance = int(1000)
winnings = int(0)

Symbols = ["Leopard", "wit shield", "W lines", "Big W", "7"]

# Subroutines:  Checking the Bet input and amount
def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount = int(betamount)
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
        winnings = int(betamount) + int(balance) * 10
        "You won 10 times your money! Congragulations! This is how much your account contains $", winnings
    elif reelone == "wit shield" and reeltwo == "wit shield" and reelthree == "wit shield":
        winnings = int(betamount) + int(balance) * 25
        "You won 25 times your money! Awesome! Your balance and wins are $", winnings
    elif reelone == "W lines" and reeltwo == "W lines" and reelthree == "W lines":
        winnings = int(betamount) + int(balance) * 50
        "You won 50 times your money! This is all of your money total $", winnings
    elif reelone == "Big W" and reeltwo == "Big W" and reelthree == "Big W":
        winnings = int(balance) + int(betamount) * 75
        "You won 75 times your money! You rewards are $", winnings
    elif reelone == "7" and reeltwo == "7" and reelthree == "7":
        winnings = int(balance) + 100000
        "You  the ulimate Jackpot! You rewards are $", winnings
    elif reelone == "7" and (reeltwo == "7" or reelthree == "7"):
        winnings = int(balance) + int(betamount) * 2
        "You won 2 times your money! You rewards are $", winnings
    elif (reelone == "7" or reeltwo == "7") and reelthree == "7":
        winnings = int(balance) + int(betamount) * 2
        "You won 2 times your money! You rewards are $", winnings
    else:
        winnings = int(balance) - int(betamount)
        "Bad luck! Maybe next time you'll win! Your remaining cash is $", winnings
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

betamount = int(betamount)

# Leads to betlimit
appropriatelimit = betlimit(betamount)

# RandomSymbolGen + 3 reels
reelone = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
reeltwo = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
reelthree = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)

reels = [reelone, reeltwo, reelthree]

slotspin = spinning(reels)

reels

# Leads to Ask input check. (At the bottom due to program order)
validask = False
while validask == False:
    answerinput = input("Would you like to play again?: ")
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




    