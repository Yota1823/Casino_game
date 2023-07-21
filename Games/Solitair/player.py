class Player:
    def __init__(self,first_name,last_name,user_name):
        self.first_n=first_name
        self.last_n=last_name
        self.user_name=user_name
        self.credit=500
        self.money_made=0
        self.game_one=0
        self.game_lost= 0

    def info(self):
      print(f'Player first name => {self.first_n}\t')
      print(f'Player last name => {self.last_n}\t')
      print(f'Player user name => {self.user_name}\t')
      print(f'Game won : {self.game_one}\t')
      print(f'Game lost : {self.game_lost}\n')
      
    
    def main(self):
       from game import Dek
       

moneylost=0

P1=Player("M","N","MN")
P1.info()
P1.main()



        