class Player:
    def __init__(self,first_name,last_name,user_name):
        self.first_n=first_name
        self.last_n=last_name
        self.user_name=user_name
        self.password=input(" Enter your first time password:")
        self.game_one=0
        self.game_lost=0
        