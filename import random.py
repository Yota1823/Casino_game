import random

print( "Hi there user, welcome to the amazing poker machine simulator.")
print( "Your opening account has in it $1000.")
print( "To win a jackpot, three leprachauns must be in a row.")
print( "Enter yes or no when prompted to finish or continue the program.")

balance = 1000

Symbols = ["Leprachaun", "Goldbar", "Pyramid", "Blackcat"]

# Subroutines:  Checking the Bet input and amount
def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount == int(betamount)
        rightbet = True
    else:
        rightbet = False
        print( "Please enter a whole number, no decimals and a bet on or below the balance.")
    return rightbet

# Limiting the bet
def betlimit(betamount):
    if betamount > balance:
        goodlimit = balance
        print( "That bet is too high! - bet adjusted to ", goodlimit)
    else:
        goodlimit = betamount
    return goodlimit

# Checking the 'Ask' input to play the machine.
def askinputcheck(answerinput):
    if answerinput.lower().startswith('y') or answerinput.lower().startswith("n"):
        rightanswerinput = True
    else:
        rightanswerinput = False
        print( "This is an incorrect input, please type an appropriate answer in.")
    return rightanswerinput

# print(ing and sorting symbols.
def spinning(reels, betamount):
    reelone, reeltwo, reelthree = reels[0], reels[1], reels[2]
    global balance
    winnings = 0
    if reelone[0] == "Leprachaun" and reeltwo[0] == "Leprachaun" and reelthree[0] == "Leprachaun":
        winnings = int(betamount) * 10 + int(balance)
        print( "You won the jackpot! Congragulations! This is how much your account contains $", winnings)
    elif reelone[0] == "Goldbar" and reeltwo[0] == "Goldbar" and reelthree[0] == "Goldbar":
        winnings = int(betamount) *5 + int(balance)
        print( "You won a considerable return! Awesome! Your balance and wins are $", winnings)
    elif reelone[0] == "Pyramid" and reeltwo[0] == "Pyramid" and reelthree[0] == "Pyramid":
        winnings = int(betamount) *2 + int(balance)
        print( "You won a good return! Its a conspiracy! This is all of your money total $", winnings)
    elif reelone[0] == "Blackcat" and reeltwo[0] == "Blackcat" and reelthree[0] == "Blackcat":
        winnings = int(balance) - int(betamount)
        print( "Unfortunately you didn't win anything, bad luck! You rewards are $", winnings)
    else:
        winnings = int(balance) - int(betamount)
        print( "Bad luck! Maybe next time you'll win! Your remaining cash is $", winnings)
    balance = winnings
    return reels

# If you have no money
def rebalance(startagain):
    global balance
    if balance < 1 and startagain == True:
        unbalance = True
        balance = 1000
        print( "You ran out of money, here is $1000")
    else:
        unbalance = False
        print( "You still have money.")
    return unbalance

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
            reelone = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)
            reeltwo = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)
            reelthree = random.sample(["Leprachaun", "Goldbar", "Goldbar", "Pyramid", "Pyramid", "Pyramid", "Blackcat", "Blackcat", "Blackcat", "Blackcat"],1)

            reels = [reelone, reeltwo, reelthree]
            print( "\n",reels,"\n")
            slotspin = spinning(reels, betamount)


        # Leads to Ask input check. (At the bottom due to program order)
        validask = False
        while validask == False:
            answerinput = input("\nWould you like to play again?: ")
            validask = askinputcheck(answerinput)

        if answerinput.lower().startswith("y"):
            startagain = True
            print( "You have $", balance)
        elif answerinput.lower().startswith("n"):
            startagain = False
            print( "You ended the game with", balance)
            break
        else:
            print( "This is an incorrect input, please answer yes or no.")

            # Leads to rebalance
        if answerinput.lower().startswith("y") and balance < 1:
            rebalance(startagain)

if __name__ == "__main__":
    my_mainloop()