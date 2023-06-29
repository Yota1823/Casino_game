import random


class Roulette:
    red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    green = [0]

    def __init__(self, userMoney, pLastName, pFirstName, pUserName, pMoneyMade, pMoneyLost, pLost, pWin):
        self.userMoney = userMoney
        self.pLastName = pLastName
        self.pFirstName = pFirstName
        self.pUserName = pUserName
        self.pMoneyMade = pMoneyMade
        self.pMoneyLost = pMoneyLost
        self.pLost = pLost
        self.pWin = pWin

    # get roll number for number and lower/higher bet type
    @staticmethod
    def get_numb():
        roll_result = random.randint(0, 36)
        # print(roll_result)
        return roll_result

    # get color for color bet type
    @staticmethod
    def get_color(Red=red, Black=black, Green=green):
        roll = random.randint(0, 36)
        if roll in Red:
            roll_result = "Red"
            return roll_result
        elif roll in Black:
            roll_result = "Black"
            return roll_result
        elif roll in Green:
            roll_result = "Green"
            return roll_result

    # display bet type option
    def display_option(self):
        print("Select one of the options:")
        print("----------------------")
        print("1 - Number Bet")
        print("2 - Color Bet")
        print("3 - Lower/Higher Bet")
        print("----------------------")

    # display number and color
    def display_number(self, Red=red, Black=black, Green=green):
        print(f'Red:\t {Red}')
        print(f'Black:\t {Black}')
        print(f'Green:\t {Green}')

    # get bet amount from user
    def get_betAmount(self):
        bet_amount = int(input("How much do you want to bet: "))
        while bet_amount > self.userMoney:
            print("Invalid amount")
            print(f'You currently have ${self.userMoney}')
            bet_amount = int(input("Enter another bet amount: "))
        return bet_amount

    # user end game
    def endgame(self):
        print(f'Player username: {self.pUserName}')
        print(f'Player Name: {self.pLastName} {self.pFirstName}')
        print(f'Player Money: ${self.userMoney}')
        print(f'Player Made: ${self.pMoneyMade}')
        print(f'Player Lost: ${self.pMoneyLost}')
        print(f'Player Total Win: {self.pWin}')
        print(f'Player Total Lost: {self.pLost}')

    # play
    def run(self):
        print("Welcome to Roulette Game")
        self.display_number()
        while self.userMoney > 0:
            self.display_option()
            user_opt = int(input("Enter Bet Type: "))
            betAmount = self.get_betAmount()

            if user_opt == 1:
                rand_num = self.get_numb()
                # print(rand_num)
                user_numb = int(input("Enter a Number: "))
                if user_numb == rand_num:
                    print(f'You won ${betAmount * 35}')
                    self.userMoney += betAmount * 35
                    # print(self.userMoney)
                    self.pMoneyMade += betAmount * 35 - betAmount
                    self.pWin += 1
                else:
                    print(f'You Lost ${betAmount}')
                    self.userMoney -= betAmount
                    self.pMoneyLost += betAmount
                    self.pLost += 1
                if input("Continue? (y/n) ").strip().upper() != 'Y':
                    self.endgame()
                    break

            elif user_opt == 2:
                rand_color = self.get_color()
                # print(rand_color)
                user_color = input("Enter Color: ")
                if user_color == 'Red' and rand_color == 'Red':
                    print(f'You won ${betAmount * 2}')
                    self.userMoney += betAmount * 2
                    self.pMoneyMade += betAmount
                    self.pWin += 1
                elif user_color == 'Black' and rand_color == 'Black':
                    print(f'You won ${betAmount * 2}')
                    self.userMoney += betAmount * 2
                    self.pMoneyMade += betAmount
                    self.pWin += 1
                elif user_color == 'Green' and rand_color == 'Green':
                    print(f'You won ${betAmount * 35}')
                    self.userMoney += betAmount * 35
                    self.pMoneyMade += betAmount + 35 - betAmount
                    self.pWin += 1
                else:
                    print(f'You Lost ${betAmount}')
                    self.userMoney -= betAmount
                    self.pMoneyLost += betAmount
                    self.pLost += 1
                if input("Continue? (y/n) ").strip().upper() != 'Y':
                    self.endgame()
                    break

            elif user_opt == 3:
                rand_num = self.get_numb()
                # print(rand_num)
                user_input = input("Select lower/higher/0: ")
                if user_input == 'lower' and (0 < rand_num <= 18):
                    print(f'You win ${betAmount * 2}')
                    self.userMoney += betAmount * 2
                    self.pMoneyMade += betAmount
                    self.pWin += 1
                elif user_input == 'higher' and (18 < rand_num <= 36):
                    print(f'You win ${betAmount * 2}')
                    self.userMoney += betAmount * 2
                    self.pMoneyMade += betAmount
                    self.pWin += 1
                elif user_input == '0' and rand_num == 0:
                    print(f'You win ${betAmount * 2}')
                    self.userMoney += betAmount * 2
                    self.pMoneyMade += betAmount
                    self.pWin += 1
                else:
                    print(f'You Lost ${betAmount}')
                    self.userMoney -= betAmount
                    self.pMoneyLost += betAmount
                    self.pLost += 1

                if input("Continue? (y/n) ").strip().upper() != 'Y':
                    self.endgame()
                    break


# test
p1 = Roulette(100, "Jone", "Mike", "mikej", 0, 0, 0, 0)
p1.run()
