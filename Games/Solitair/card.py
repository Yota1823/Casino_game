import random
class Solitair_card:

    card_name={
        1:'A',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'10',
        11:'j',
        12:'Q',
        13:'K'


    }

    def __init__(self,value,suit):
        self.value= value
        self.suit = suit  
        self.card = str(self.suit) +" "+  str( self.value)
        
    def below(self,card):
      
      return self.value == card.value-1

    def Opposite(self,card):
        if self.suit=="Club" or self.suit=="Spade":
            return card.suit == "Heart" or  card.suit=="Diamond"
        else:
            return card.suit == "Club" or card.suit=="Spade" 

    def Attach(self,card):
        if self.below(card ) and self.Opposite(card):
            return True
        else:
            return False
    
    def __str__(self):
        return self.card

#unshuf_deck=[Solitair_card(s,v) for v in range (1,14) for s in ["Club","Spade","Diamond","Heart"]]
#random.shuffle(unshuf_deck)
#for card in unshuf_deck :
 
 
 
card1= Solitair_card(11,"Heart") 
card2=Solitair_card(8,"Club")
card3=Solitair_card(12,"Spade")

C=[card1,card3]
C2=[card3,card2,card1]

# test= card1.below(card2)
# test2=card1.Opposite(card2)
test3= C[0].Attach(C2[-1])
# print(test)
# print(test2)
print(test3)

for i in range (max (len(C),len (C2))):
    card=C[i] if i<len(C) else ""
    card3=C2[i] if i<len(C2) else ""
    card4=C[i] if i<len(C) else ""
    print("{}\t{}\t{}\t".format(card1,card3,card4))





  
   
