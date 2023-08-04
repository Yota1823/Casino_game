class Baccarat:
    def __init__(self, userMoney, pLastName, pFirstName, pUserName, pMoneyMade, pMoneyLost, pLost, pWin):
        self.userMoney = userMoney
        self.pLastName = pLastName
        self.pFirstName = pFirstName
        self.pUserName = pUserName
        self.pMoneyMade = pMoneyMade
        self.pMoneyLost = pMoneyLost
        self.pLost = pLost
        self.pWin = pWin
        self.currGame = 'Baccarat'

    def option(self):
        print('''
Options:
1: Status
2: Place bets
3: Deal cards
4: Change shoe
0: Quit''')
P1 = Baccarat(100," "," "," ",300,100,1,1)
P1.option()
