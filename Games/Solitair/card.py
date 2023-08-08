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




  
   
