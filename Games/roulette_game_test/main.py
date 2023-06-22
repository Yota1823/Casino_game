import random

red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
green = [0]

# test
roll_result = ""
user_money = 10
win_streak = 0
pUsername = "mikej"
pLastname = "Jon"
pFirstname = "Mike"
pMoneyMade: int = 0
pMoneyLost: int = 0
currGame = ""
pWin = 0
pLost = 0


def display_option():
    print("Select one of the options:")
    print("----------------------")
    print("1 - Number Bet")
    print("2 - Red/Black/Green Bet")
    print("3 - Lower/Higher Bet")
    print("----------------------")


def display_number():
    print(f'Red:\t {red}')
    print(f'Black:\t {black}')
    print(f'Green:\t {green}')


# get roll number
def roll_number():
    rand_num = random.randint(0, 36)
    global roll_result

    if rand_num in red:
        # print(rand_num)
        roll_result = "Red"
    elif rand_num in black:
        # print(rand_num)
        roll_result = "Black"
    elif rand_num in green:
        # print(rand_num)
        roll_result = "Green"
    # print(roll_result)


# get bet money from user
def get_bet_amount():
    global user_money
    bet_amount = int(input("How much do you want to bet: "))
    while bet_amount > user_money:
        print("Invalid amount")
        print(f'You currently have {user_money}')
        bet_amount = int(input("Enter another bet amount: "))
    return bet_amount


# get result
def get_result(game, bet_money, user_inp):
    global user_money
    global win_streak
    global pWin
    global pLost
    global pMoneyMade
    global pMoneyLost

    rand_num = random.randint(0, 36)

    if game == 1:
        if user_inp == rand_num:
            # print(f'Random number is {rand_num}')
            print("You won")
            pMoneyMade = bet_money * 35 - bet_money
            # user_money += bet_money * 35
            win_streak += 1
            pWin += 1
        else:
            # print(f'Random number is {rand_num}')
            print("You lost")
            pMoneyLost = bet_money
            # user_money -= pMoneyLost
            win_streak = 0
            pLost += 1

    elif game == 2:
        if user_inp == "red" and roll_result == "Red":
            win_streak += 1
            pMoneyMade = bet_money
            # user_money += pMoneyMade * 2
            print("Red, You Win")
            # print(win_streak)
            # print(user_money)
            pWin += 1

        elif user_inp == "black" and roll_result == "Black":
            win_streak += 1
            pMoneyMade = bet_money
            # user_money += pMoneyMade * 2
            print("Black, You Win")
            # print(win_streak)
            # print(user_money)
            pWin += 1

        elif user_inp == "green" and roll_result == "Green":
            win_streak += 1
            pMoneyMade = bet_money * 35 - bet_money
            # user_money += bet_money * 35
            print("Green, You Win")
            # print(win_streak)
            # print(user_money)
            pWin += 1

        else:
            win_streak = 0
            print("You lost")
            pMoneyLost = bet_money
            # user_money -= pMoneyLost
            # print(user_money)
            pLost += 1

    elif game == 3:

        if user_inp == 1 and (0 < rand_num < 18):
            # print(f'Random number is {rand_num}')
            print("You win")
            pMoneyMade = bet_money
            # user_money += pMoneyMade * 2
            win_streak += 1
            pWin += 1
        elif user_inp == 2 and (18 < rand_num <= 36):
            # print(f'Random number is {rand_num}')
            print("You win")
            pMoneyMade = bet_money
            # user_money += pMoneyMade * 2
            win_streak += 1
            pWin += 1
        elif user_input == 3 and rand_num == 0:
            # print(f'Random number is {rand_num}')
            print("You win")
            pMoneyMade = bet_money * 35 - bet_money
            # user_money += bet_money * 35
            win_streak += 1
            pWin += 1
        else:
            # print(f'Random number is {rand_num}')
            print("You lost")
            pMoneyLost = bet_money
            # user_money -= pMoneyLost
            win_streak = 0
            pLost += 1


# when user end the game
def endgame():
    global user_money
    user_money = user_money + pMoneyMade - pMoneyLost
    print(f'Player username: {pUsername}')
    print(f'Player Name: {pLastname} {pFirstname}')
    print(f'Player Made: {pMoneyMade}')
    print(f'Player Lost: {pMoneyLost}')
    print(f'Total Win: {pWin}')
    print(f'Total Lost: {pLost}')
    print(f'Player Money: {user_money}')


# play the game
print("Welcome to Roulette Game")
display_number()
while user_money > 0:
    display_option()
    user_option = int(input("Enter option: "))
    if user_option == 1:
        user_bet = get_bet_amount()
        user_input = int(input("Enter a number: "))
        get_result(user_option, user_bet, user_input)

        if input("Continue? (y/n) ").strip().upper() != 'Y':
            endgame()
            break

    elif user_option == 2:
        roll_number()
        user_bet = get_bet_amount()
        user_input = input("Select red, black or green: ")
        get_result(user_option, user_bet, user_input)

        if input("Continue? (y/n) ").strip().upper() != 'Y':
            endgame()
            break

    elif user_option == 3:
        user_bet = get_bet_amount()
        user_input = input("Select of the Lower bet for Higher bet: \n1 - Lower\n2 - Higher\n3 - 0\n")
        get_result(user_option, user_bet, user_input)

        if input("Continue? (y/n) ").strip().upper() != 'Y':
            endgame()
            break

    if user_money <= 0:
        print('No money left')
        break
