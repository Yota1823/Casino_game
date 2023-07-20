from Deck import Dek
from Table import Tableau
from Foundation import foundation
class Waste:
    def __init__(self,Deck):
        self.deck=Deck
        self.waste=[]

    def stock_waste(self):
        if len(self.deck )==0:
            self.waste.reverse()
            self.deck=self.waste.copy()
            self.waste.clear()
        
        self.waste.append(self.deck.pop())
        return True
    
    def pop_w_card(self):
        if len(self.waste)>0:
            return self.waste.pop()
        else :
            return "empty"
    
    def get_waste(self):
         if len(self.waste)>0:
            return self.waste[-1]
         else:
            return "empty"

    def get_stock(self):
        if len(self.deck)>0:
            return str(len(self.deck)) + " " + "cards"
        else:
            return "empty"
    
# """ Deck=Dek(2)

# Waste_card=Deck.deal_c(28)
# table_carrds=Deck.deal_c(28)
# table=Tableau(table_carrds)
# Stock=Waste(Waste_card)
# Card_Foundation=foundation()
# Suit=Card_Foundation.get_last_card("Club")
# print(Suit)
# table.display_c(0)
# table.display_c(1)
# table.display_c(2)
# table.display_c(3)
# table.display_c(4)
# table.display_c(5)
# table.display_c(6)




# while(1):
    
#     table.display_c(0)
#     table.display_c(1)
#     table.display_c(2)
#     table.display_c(3)
#     table.display_c(4)
#     table.display_c(5)
#     table.display_c(6)
    
 
#     if len(Stock.waste)==0:
#      Stock_C=Stock.stock_waste()
#      print(Stock_C)
#      for card in Stock.waste:
#          print(card)
    

   
#     command=input(" Enter a number :")

#     if (command=="1"):
#         value=input("Enter column 1:")
#         v=int(value)
#         value2=input("Enter column 2:")
#         v2=int(value2)
#         index=input(" Enter the index value: ")
#         x=int(index)
#         Add_card=table.add_C_T(v,v2,x)
#         if Add_card:
#             table.display_c(v)
            
#             print("_____________")
#             table.display_c(v2)
            
#             print(" Card have been transfered ")
#         else:
#             print(" Card couldn't be transfered  ")
   
#     elif(command=="2"):
#           val=input("Enter column 1:")
#           Value=int(val)
          
         
#           waste_to_table=table.add_W_T(Stock,Value)
#           if waste_to_table:
#              table.display_c(Value)
             
#              print("_______")
#              Wast_length= Stock.get_waste()
#              print(Wast_length)
#           else:
#             print(" Card couldn't be transfered ")

#     elif(command=="3"):
#         value=input("Enter a column : ")   
#         val=int(value) 
#         T_F=table.add_T_F(Card_Foundation,val)
#         if T_F:
#             card_suit=Card_Foundation.get_last_card(table.flip[val][-1].suit)
#             print(card_suit)
#         else:
#             print("Card couldn't be added to foundation ")
#         #  Waste_c= Stock.pop_w_card()
#         #  print(Waste_c)
#         #  Stock_length= Stock.get_stock()
#         #  print(Stock_length)
#         #  Wast_length= Stock.get_waste()
#         #  print(Wast_length)
    
#     else :
#         print(" This command dont exist ")
 

   




        