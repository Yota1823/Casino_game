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
Stock_length=Waste_foundation.get_stock()
Waste_length=Waste_foundation.get_waste()
print("{}\t{}".format(Stock_length, Waste_length))
Table_foundation.display_unfipped()
Table_foundation.display_c()

while(1):
    
    if len(Waste_foundation.waste)==0:
        Waste_foundation.stock_waste()
    else:
        print(f"Waste_card {Waste_foundation.waste[-1]}")
    command=input("Enter a command: ")
    if command=="1":
        value1=input("Enter column 1 : ")
        val1=int(value1)
        value2=input("Enter column 2 : ")
        val2=int(value2)
        index=input("Enter an index : ")
        i=int(index)
        test1=Table_foundation.add_C_T(val1,val2,i)
        if test1:
            print(f"Card has been succefully moved from {val1} to {val2}")
        else:
            print(" Card couldn't be moved ")
    elif command=="2":
        Value=input("Enter a column from 0 to 6 : ")
        Val=int(Value)
        test2=Table_foundation.add_W_T(Waste_foundation,Val)
        if test2:
            print(f"{Waste_foundation.waste[-1]} has succesfully been moved from waste to {Val} ")
        else:
            print(" This move couldn't be made ")
    print("{}\t{}".format(Stock_length, Waste_length))
    Table_foundation.display_unfipped()
    Table_foundation.display_c()
