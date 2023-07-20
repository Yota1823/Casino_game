from card import Solitair_card
from Deck import Dek
from Waste_pile import Waste
from Foundation import foundation
from Table import Tableau
from player import Player
Card_Deck=Dek(2)
Table_Card=Card_Deck.deal_c(28)
Table_foundation=Tableau(Table_Card)
Waste_card=Card_Deck.deal_c(28)
Waste_foundation=Waste(Waste_card)
Foundation=foundation()
Stock_length=Waste_foundation.get_stock()
Waste_length=Waste_foundation.get_waste()
Player1=Player("Manuel","Choute","The Jack")
Start= input(" Enter your username:")
if Start==Player1.user_name:
    print(f'Player first name => {Player1.first_n}\t')
    print(f'Player last name => {Player1.last_n}\t')
    print(f'Player user name => {Player1.user_name}\t')
    print(f'Game won : {Player1.game_one}\t')
    print(f'Game lost : {Player1.game_lost}\n')
    print("{}\t{}".format(Stock_length, Waste_length))
    print("\t")
    Table_foundation.display_unfipped()
    Table_foundation.display_c()
    Player_card=input("Enter column of card to play:")
    Card_cl=int(Player_card)
    Bet_round=input(f"After how many move will the {Table_foundation.flip[Card_cl][-1]} ")
    Round=int(Bet_round)
    i=0
    while(i<=Round):
        i=0
        print(f"card bet on:{Table_foundation.flip[Card_cl][-1]}\n")
        print(f'Round left : {i}')
        if len(Waste_foundation.waste)==0:
            Waste_foundation.stock_waste()
        else:
            print(f"Waste_card {Waste_foundation.waste[-1]}")
        command=input("Enter a command: ")
        if command=="1":
            #value1=input("Enter column 1 : ")
            val1=Card_cl
            value2=input("Enter column 2 : ")
            val2=int(value2)
            index=input("Enter an index : ")
            i=int(index)
            test1=Table_foundation.add_C_T(val1,val2,i)
            if test1:
                print(f"Card has been succefully moved from {val1} to {val2}")
                i=i+1
                Card_cl=val2
                Table_foundation.table_check(val1,val2)
                print("\t")
            else:
                print(" Card couldn't be moved ")
        elif command=="2":
            Value=input("Enter a column from 0 to 6 : ")
            Val=int(Value)
            test2=Table_foundation.add_W_T(Waste_foundation,Val)
            if test2:
                print(f"{Waste_foundation.waste[-1]} has succesfully been moved from waste to {Val} ")
        elif command=="3":
              Column=input("Enter a column :")
              Col=int(Column)
              card=Table_foundation.flip[Col][-1].suit
              test3=Table_foundation.add_T_F(Foundation,Col)
            
              if test3:
                  card_value= Foundation.get_last_card(card)
                  print(card_value)
                  i=i+1
              else:
                 print(" Card couldn't be move to foundation ")

        else:
            print(" This move couldn't be made ")
        print("{}\t{}".format(Stock_length, Waste_length))
        Table_foundation.display_unfipped()
        Table_foundation.display_c()
