# from card import Solitair_card
# from Deck import Dek
# from Waste_pile import Waste
# from Foundation import foundation
# from Table import Tableau
# from player import Player
# Card_Deck=Dek(2)
# Table_Card=Card_Deck.deal_c(28)
# Table_foundation=Tableau(Table_Card)
# Waste_card=Card_Deck.deal_c(28)
# Waste_foundation=Waste(Waste_card)
# Foundation=foundation()
# Stock_length=Waste_foundation.get_stock()
# Waste_length=Waste_foundation.get_waste()


# while(1):
#     print("{}\t{}".format(Stock_length, Waste_length))
#     print("\t")
#     Table_foundation.display_unfipped()
#     Table_foundation.display_c()
    
#     Player_card=input("Enter column of card to play:")
#     Card_cl=int(Player_card)
#     Bet_round=input(f"After how many move will the {Table_foundation.flip[Card_cl][-1]} ")
#     Round=int(Bet_round)
#     j=0
#     L=0
#     while(j<=Round):
            
#             print(f"card bet on:{Table_foundation.flip[Card_cl][-1]}\n")
#             print(f'Round left : {j}')
#             if len(Waste_foundation.waste)==0:
#                 Waste_foundation.stock_waste()
#             else:
#                 print(f"Waste_card {Waste_foundation.waste[-1]}")
#             command=input("Enter a command: ")
#             if command=="1":
        
#                 val1=Card_cl
#                 value2=input("Enter column 2 : ")
#                 val2=int(value2)
#                 index=input("Enter an index : ")
#                 i=int(index)
#                 test1=Table_foundation.add_C_T(val1,val2,i)
#                 if test1:
#                     print(f"Card has been succefully moved from {val1} to {val2}")
#                     j=j+1
#                     Card_cl=val2
#                     Table_foundation.table_check(val1,val2)
#                     print("\t")
#                 else:
#                     print(" Card couldn't be moved ")
#                     L=L+1
#             elif command=="2":
#                 Value=input("Enter a column from 0 to 6 : ")
#                 Val=int(Value)
#                 test2=Table_foundation.add_W_T(Waste_foundation,Val)
#                 if test2:
#                     print(f"{Waste_foundation.waste[-1]} has succesfully been moved from waste to {Val} ")
#             elif command=="3":
                
                
#                 card=Table_foundation.flip[Card_cl][-1].suit
#                 V=int(input(" Column : "))
#                 test3=Table_foundation.add_T_F(Foundation,V)
                
#                 if test3:
#                     card_value= Foundation.get_last_card(card)
#                     print(card_value)
#                     j=j+1
#                     if j== Round:


#                       Playe.game_one=Player1.game_won+1


# >>>>>>> b8df4fedf56e5145dcf89083db8bc33d9f4046b
#                       game_one = game_one+1

#                       Player1.game_one=Player1.game_won+1
# <<<<<<< HEAD


# =======
# >>>>>>> main
# >>>>>>> b8df4fedf56e5145dcf89083db8bc33d9f4046bb
#                       print(" Great you won ")
#                       break
                    
#                 else:
#                     print(" Card couldn't be move to foundation ")
#                     L=L+1
                

#             else:
#                 print(" This move couldn't be made ")
#             print("{}\t{}".format(Stock_length, Waste_length))
#             Table_foundation.display_unfipped()
#             Table_foundation.display_c()
#             if (j>Round):
#                 print(" You are out of move ")

#                 game_lost=game_lost+1

#                 self.game_lost=self.game_lost+1

#             if(L>4):
#                 print(" You are out of tries ")
#                 game_lost=game_lost+1
#                 break
