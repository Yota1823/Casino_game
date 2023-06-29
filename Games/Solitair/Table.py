from card import Solitair_card
from Deck import Deck
class Tableau:

    def __init__(self,card_l):
       
        self.unfliped= {x: card_l[x:x+x+1] for x in range(7)}
        self.flip={x:[self.unfliped[x].pop()] for x in range(7)}

    def flip_Card(self,col):
        if len(self.unfliped[col]) >0:
            self.flip[col].append(self.unfliped[col].pop())
    
    def pile_l(self):
        return max(len(self.unfliped[x])+ len (self.flip[x]) for x in range (0,7))

    def add_C(self,C,CL):
        column_C=self.flip[CL][-1]
        verify=column_C.Attach(C)
        if len(self.flip[CL])==0:
            self.flip[CL].extend(C)
            return True
        elif len(self.unfliped[CL])>0 and verify:
            self.flip[CL].extend(C)
            return True
        else:
            return False



    
    def Tableau_to_Tableau(self,CL1,CL2,x):
        C_pile1= self.flip[CL1]

        if x>=len(self.unfliped[CL1]):
           return False 
        if self.add_C(C_pile1[x],self.flip[CL2][-1]):
             self.flip[CL1]=C_pile1[:x]
             if x==0:
                 self.flip_Card(CL1)
                 return True
        return False    
    
    def Tableau_to_foundation(self,foundation,column):
        card_column= self.flip[column]
        if len(card_column)==0:
            return False
        if foundation.add_C(card_column[-1]):
            card_column.pop()
            if len(card_column)==0:
                self.flip(column)
            return True
        else :
           return False 

    def pile_to_Tableau(self,waste_p,Column):
        Card= waste_p.waste[-1]
        if self.add_C([Card],Column):
            waste_p.pop_w_card()
            return True
        else:
            return False 
    
    def display_unfipped(self):
        for col ,cards in self.unfliped.items():
            print(f"Unfliped  {6}")
            for card in cards:
              print(card.value, card.suit)
        print()
        
    def display_flip(self):   
        for Col, Cards in self.flip.items():
            print(f" flip {Col+1}")
            for Card in Cards :
                print(Card.value,Card.suit)
        print()
         
         
            



Test_Deck= Deck(1)
Numb_Deck= Test_Deck.deal_c(28)
Test_Tableau= Tableau(Numb_Deck)

print(" This is the card in the deck ")
for cards in Numb_Deck:
    print(cards)

Test_Tableau.flip_Card(2)
Test_Tableau.flip_Card(5)

pile_l=Test_Tableau.pile_l()




Test_Tableau= Tableau(Numb_Deck)

Test_Tableau.display_unfipped()
dummy_card=Solitair_card(2,"Heart")
Add= Test_Tableau.add_C(dummy_card,6)
test= Test_Tableau.Tableau_to_Tableau(2,5,2)
print(Add)

if (test):
    print(pile_l)

else:
    print(" can't add cards ")






