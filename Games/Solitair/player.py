class Player:
    def __init__(self,first_name,last_name,user_name,p_Cred,win,made,lost,m_lost,current):
        self.first_n=first_name
        self.last_n=last_name
        self.user_name=user_name
        self.credit=p_Cred
        self.money_made=made
        self.game_won=win
        self.game_lost=lost
        self.money_lost=m_lost
        self.current=current

    def info(self):
      print(f'Player first name => {self.first_n}\t')
      print(f'Player last name => {self.last_n}\t')
      print(f'Player user name => {self.user_name}\t')
      print(f'Game won : {self.game_won}\t')
      print(f'Game lost : {self.game_lost}\n')
      
    def rules(self):
         return '''Command 1: move card from column to column \t
          command 2: move card from pile to table \t
          command 3: move card from table to foundation\t
          command 4: display help menu \t
          How to play:
          1) Start by selecting a column from 0 to 6 card at 
          the end of that column is the card bet on\t
          2) Select one of the command from 1 to 3 to perform a move 
          command 4 is here to display the menu\t
          Command functionality:

          Command 1: move card from column to column 
          card can only be move if card 1 less then card 2
          and card suit spade,club can attached to card heart ,diamond
          first move when  selecting index of card can either be -1 or 0 
          Error!!
          if index out of colum current length error might be generated \t
          if other type such as letter or special  case entered error might
          be generated 

          Command 2: move waist card from waist to table
          waist card can only be moved to column is empty 
          or the card conditions are the same for command 1\t
          Error!!
          if column out of range of table error might be generated .

          Command 3: move last card of column to foundation if possible\t 
          card can be moved to foundation if card  being added has a value of  either one
          or card being added value greater then last card in suit foundation.

          Game dynamic :
          
          Once bet card selected player can either move card selected or other card 
          each time a moved is perform number of move decreases 
          each time a move can't not be made number of try decrease\t
          games end either if the player move card to foundation in 
          number of moved predicted therefore win game\t
          games ends if player out of moved therefore lost bet\t
          games ends if player out of try therefore lost bet  \t

          Money will be added or removed after each game depending on if 
          player won or lost  '''     
    
    
    def main(self):
        from card import Solitair_card
        from Deck import Dek
        from Waste_pile import Waste
        from Foundation import foundation
        from Table import Tableau
        
        Card_Deck=Dek(2)
        Table_Card=Card_Deck.deal_c(28)
        Table_foundation=Tableau(Table_Card)
        Waste_card=Card_Deck.deal_c(28)
        Waste_foundation=Waste(Waste_card)
        Foundation=foundation()
        Stock_length=Waste_foundation.get_stock()
        Waste_length=Waste_foundation.get_waste()
        print("{}\t{}".format(Stock_length, Waste_length))
        print("\t")
        Table_foundation.display_unfipped()
        Table_foundation.display_c()
              
        Player_card=input("Enter column of card to play:")
        Card_cl=int(Player_card)
        index=0
        Card_played=Table_foundation.flip[Card_cl][index]
        Bet_round=input(f"After how many move will the {Card_played} be moved to the foundation  ")
        Round=int(Bet_round)
        j=Round
        L=4
         
              
        while(j>0):
                      F=Foundation.get_last_card("Heart")
                      F2=Foundation.get_last_card("Diamond")
                      F3=Foundation.get_last_card("Spade")
                      F4=Foundation.get_last_card("Club")
                      print(f"{F}   {F2}   {F3}   {F4}")
                      print("\n")
                      print(f"card bet on: {Card_played}\n")
                      print(f'Round left : {j}')
                      print(f"Try left: {L}")
                      Stock_length=Waste_foundation.get_stock()
                      if len(Waste_foundation.waste)==0:
                          Waste_foundation.stock_waste()
                      else:
                          print(f"Waste_card {Waste_foundation.waste[-1]}")
                      print('''Command 1: move card from column to column \t
                      command 2: move card from pile to table \t
                      command 3: move card from table to foundation\t
                      command 4: display help menu \t''')
                      command=input("Enter a command: ")
                      if command=="1":
                  
                          Player_card=Card_cl
                         
                          choice=input("wich card do you want to use ")
                          v_choice=int(choice)
                          if v_choice==Player_card:
                            value2=input("Enter column 2 : ")
                            val2=int(value2)
                            index=input("Enter an index : ")
                            i=int(index)
                            test1=Table_foundation.add_C_T(Player_card,val2,i)
                            if test1:
                               print(f"Card has been succefully moved from {Player_card} to {val2}")
                               j=j-1
                               Player_card=val2
                               index=i
                               Table_foundation.table_check(Player_card,val2)
                               print("\t")
                            else:
                                print(" Card couldn't be moved ")
                                L=L-1
                          else:
                                
                                Val1=v_choice
                                value2=input("Enter column 2 : ")
                                val2=int(value2)
                                index=input("Enter an index : ")
                                i=int(index)
                                test1=Table_foundation.add_C_T(Val1,val2,i)
                                if test1:
                                   print(f"Card has been succefully moved from {Player_card} to {val2}")
                                   j=j-1
                                   Player_card=val2
                                   Table_foundation.table_check(Player_card,val2)
                                   print("\t")
                                else:
                                  print(" Card couldn't be moved ")
                                  L=L-1
                      elif command=="2":
                          Value=input("Enter a column from 0 to 6 : ")
                          Val=int(Value)
                          test2=Table_foundation.add_W_T(Waste_foundation,Val)
                          if test2:
                              print(f"{Waste_foundation.waste[-1]} has succesfully been moved from waste to {Val} ")
                              j=j-1
                          else:
                               L=L-1
                               print(f"{Waste_foundation.waste[-1]} couldn't  been move from waste to {Val} " )
                      if j==1:
                                V=Player_card
                                v=int(V)
                                test3=Table_foundation.add_T_F(Foundation,v)
                                if test3:
                                  self.game_won=self.game_won+1
                                  self.credit=self.credit+self.Bet
                                  self.money_made=self.money_made + self.Bet
                                  print(" Great you won ")
                                  self.data()
                                  break 
                                else:   
                                  print(" You are out of move ")
                                  self.game_lost=self.game_lost+1
                                  self.credit=self.credit-self.Bet
                                  self.money_lost=self.money_lost+ self.Bet

                      elif command=="3":
                                
                                V=int(input(" Column : "))
                                
                                test3=Table_foundation.add_T_F(Foundation,V)
                                
                               
                                if test3:
                                 j=j-1
                                if not test3:
                                  print(" Card couldn't be move to foundation ")
                                  L=L-1
                          
                      elif command=="4":
                           rule=P1.rules()
                           print(rule)
                           print("\n")
                      else:
                          print(" This move couldn't be made ")
                      print("{}\t{}".format(Stock_length, Waste_length))
                      Table_foundation.display_unfipped()
                      Table_foundation.display_c()
                      
                          
                      if(L==0):
                          print(" You are out of tries ")
                          self.game_lost=self.game_lost+1
                          self.credit=self.credit-self.Bet
                          self.money_lost=self.money_lost+ self.Bet
                          self.data()
                          break
                

    def Data(self):
      import sqlite3
      self.connect=sqlite3.connect("Casino.db")
      self.cursor=self.connect.cursor()
      Select="SELECT * FROM Player WHERE playerUserName=? "
      self.cursor.execute(Select,(self.first_n))
      Selected=self.cursor.fetchall()
      if Selected:
        for Result in Selected:
          self.user_name=Result[0]
          self.first_n=Result[1]
          self.last_n=Result[2]
          self.credit=Result[3]
          self.money_made=Result[4]
          self.money_lost=Result[5]
          self.current=Result[6]
          self.game_won=Result[7]
          self.game_lost=Result[8]
      else:
        print("Player not part of data base ")


      
    
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
        self.cursor.execute(Change,(value,self.user_name,))
        self.cursor.execute(Change2,(value2,self.user_name,))
        self.cursor.execute(Change3,(value3,self.user_name,))
        self.cursor.execute(Change4,(value4,self.user_name,))
        self.cursor.execute(Change5,(value5,self.user_name,))
        self.connect.commit()
        self.connect.close()
    
    def  bet(self):
           bet=input("Enter your bet: ")
           self.Bet=int(bet)
           if self.Bet<self.credit:
             return True
           else:
             return False
       



P1=Player("M","N","MN",500,0,0,0,0,0)
P1.Data()
P1.info()
while(1):
  if P1.bet():
       P1.main()
  else:
     print("You have no money left ")



        