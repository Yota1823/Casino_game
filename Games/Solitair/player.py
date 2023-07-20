class Player:
    def __init__(self,first_name,last_name,user_name,money_made,money_won,money_lost,money_cred):
        self.first_n=first_name
        self.last_n=last_name
        self.user_name=user_name
        self.password=input(" Enter your first time password:")
        self.credit=money_cred
        self.money_made=money_made
        self.game_one= money_won
        self.game_lost= money_lost
        