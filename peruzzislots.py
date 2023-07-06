import sqlite3
import random
import sys


balance = 1000
balance == int(balance)
winnings = 0
winnings == int(winnings)

Symbols = ["Leopard", "wit shield", "W lines", "Big W", "7"]

# Checking the Bet input and amount
def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount = int(betamount)
        rightbet = True
    else: 
        rightbet = False
        print("Please enter a whole number, no decimals and a bet on or below the balance.")
    return rightbet

# Limiting the bet
def betlimit(betamount):
    if betamount > balance:
        goodlimit = balance
        print("That bet is too high! Bet adjusted to ", goodlimit)
    else:
        goodlimit = betamount
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
def spinning(reels, betamount):
    reelone, reeltwo, reelthree = reels[0], reels[1], reels[2]
    global balance
    winnings = 0
    if reelone[0] == "Leopard" and reeltwo[0] == "Leopard" and reelthree[0] == "Leopard":
        winnings = int(balance) + int(betamount) * 10
        print("You won 10 times your money! Congragulations! This is how much your account contains $", winnings)
    elif reelone[0] == "wit shield" and reeltwo[0] == "wit shield" and reelthree[0] == "wit shield":
        winnings = int(balance) + int(betamount) * 25
        print("You won 25 times your money! Awesome! Your balance and wins are $", winnings)
    elif reelone[0] == "W lines" and reeltwo[0] == "W lines" and reelthree[0] == "W lines":
        winnings = int(balance) + int(betamount) * 50
        print("You won 50 times your money! This is all of your money total $", winnings)
    elif reelone[0] == "Big W" and reeltwo[0] == "Big W" and reelthree[0] == "Big W":
        winnings = int(balance) + int(betamount) * 75
        print("You won 75 times your money! You rewards are $", winnings)
    elif reelone[0] == "7" and reeltwo[0] == "7" and reelthree[0] == "7":
        winnings = int(balance) + 1000000
        print("You  the ulimate Jackpot! You rewards are $", winnings)
    elif reelone[0] == "7" and (reeltwo[0] == "7" or reelthree[0] == "7"):
        winnings = int(balance) - int(betamount) * 2
        print("You won 2 times your money! You rewards are $", winnings)
    elif (reelone[0] == "7" or reeltwo[0] == "7") and reelthree[0] == "7":
        winnings = int(balance) - int(betamount) * 2
        print("You won 2 times your money! You rewards are $", winnings)
    else:
        winnings = int(balance) - int(betamount)
        print("Bad luck! Maybe next time you'll win! Your remaining cash is $", winnings)
        print(winnings)
    return reels

# If you have no money
def rebalance(startagain):        
    while balance < 1 and startagain == True:
        unbalance = True
        balance = winnings
        print("You ran out of money, go refill at main screen")
    else:
        unbalance = False
        print("You still have money.")
        return winnings

# Leads to Bet input check. 
def my_mainloop():
    global balance
    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount)

        betamount = int(betamount)

        # Leads to betlimit
        betamount = betlimit(betamount)

        # RandomSymbolGen + 3 reels
        if betamount > 0:
            reelone = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
            reeltwo = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)
            reelthree = random.sample(["7", "Big W", "Big W", "W lines", "W lines", "W lines", "wit shield", "wit shield", "wit sheild", "leopard", "leopard", "leopard"],1)

            reels = [reelone, reeltwo, reelthree]
            print("\n",reels,"\n")
            slotspin = spinning(reels, betamount)


# Leads to Ask input check. (At the bottom due to program order)
        validask = False
        while validask == False:
            answerinput = input("Would you like to play again?: ")
            validask = askinputcheck(answerinput)
        if answerinput == "Yes" or answerinput == "yes" or answerinput == "y":
            startagain = True
            print("You have $", balance)
            pass
        elif answerinput == "No" or answerinput == "no" or answerinput == "n":
            startagain = False
            balance = winnings
            print("You ended the game with", balance)
            break
        else:
            print("This is an incorrect input, please answer yes or no.")

        # Leads to rebalance
        if answerinput == "Yes" or answerinput == "yes" or answerinput == "y" and balance == 0:
            balance = rebalance(startagain)

if __name__ == "__main__":
    my_mainloop()


    