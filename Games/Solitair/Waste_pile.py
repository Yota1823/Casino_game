from Deck import Deck
From Table import
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
    
deck=Deck(1)
Waste_card=deck.deal_c(28)
Table_card=
Stock=Waste(Waste_card)
Stock_C=Stock.stock_waste()
print(Stock_C)
Wast_length= Stock.get_waste()
print(Wast_length)
Waste_c= Stock.pop_w_card()
print(Waste_c)
Stock_length= Stock.get_stock()
print(Stock_length)
Wast_length= Stock.get_waste()
print(Wast_length)


   




        