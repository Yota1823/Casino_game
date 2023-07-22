class Player:
    def __init__(self,first_name,last_name,user_name,p_Cred,win,made,lost,m_lost):
        self.first_n=first_name
        self.last_n=last_name
        self.user_name=user_name
        self.credit=p_Cred
        self.money_made=made
        self.game_won=win
        self.game_lost=lost
        self.money_lost=m_lost

    def info(self):
      print(f'Player first name => {self.first_n}\t')
      print(f'Player last name => {self.last_n}\t')
      print(f'Player user name => {self.user_name}\t')
      print(f'Game won : {self.game_won}\t')
      print(f'Game lost : {self.game_lost}\n')
      
    
    def main(self):
       from game import Dek
    
    def data(self):
        import sqlite3
        self.connect=sqlite3.connect("Casino.db")
        self.cursor=self.connect.cursor()
        Change="UPDATE Player SET pCredit=? WHERE playerUserName=?"
        Change2="UPDATE Player SET pMoneyMade=? WHERE playerUserName=?"
        Change3="UPDATE Player SET pMoneyLost=? WHERE playerUserName=?"
        Change4="UPDATE Player SET pWin=? WHERE playerUserName=?"
        Change5="UPDATE Player SET pLoss=? WHERE playerUserName=?"
        value=self.credit
        value2=self.money_made
        value3=self.money_lost
        value4=self.game_won
        value5=self.game_lost
        self.cursor.execute(Change,(value,))
        self.cursor.execute(Change2,(value2,))
        self.cursor.execute(Change3,(value3,))
        self.cursor.execute(Change4,(value4,))
        self.cursor.execute(Change5,(value5,))
        self.connect.commit()
        self.connect.close()




moneylost=0

P1=Player("M","N","MN",500,0,0,0,0)
P1.info()
P1.main()



        