import card
from card import Solitair_card


import random
class Dek:
     unshuf_deck=[Solitair_card(v,s) for v in range (1,14) for s in ["Club","Spade","Diamond","Heart"]]

     def __init__(self,num_deck):
        self.deck= self.unshuf_deck * num_deck
        random.shuffle(self.deck)

     def flip_C(self):
       return self.deck.pop()

     def deal_c(self, num_c):
      return [self.deck.pop() for x in range  (0,num_c)]

     def display_deck(self):
      return self.deck
      
     def remainer(self):
        return[str(card)for card in self.deck]

deck=Dek(1)

c_distributed= deck.deal_c(1)

for card in c_distributed:
    print(card)
# Test_card=Solitair_card(3,"Club")
# test= c_distributed[0].below(Test_card)
# print(test)
# card =deck.flip_C()
# print(" ")
# print(card)

# card_left=deck.remainer()
# print (card_left)
# print(" ")