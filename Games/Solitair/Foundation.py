from card import Solitair_card
class foundation:
    def __init__(self):
        self.foundation={
            "Club":[],
            "Spade":[],
            "Diamond":[],
            "Heart":[]
        }
    
    def Add_to_Foundation(self,card):
        stack=self.foundation[card.suit]
        if card.value==1 or  stack[-1].below(card):
          stack.append(card)
          return True
        else:
            return False

    def get_last_card(self,suit):
        stack_atrribute=self.foundation[suit]
        if len(stack_atrribute)==0:
            return suit[0].upper()
        else:
            return self.foundation[suit][-1]

test_card=Solitair_card(1,"Heart")
Foundation=foundation()
test=Foundation.Add_to_Foundation(test_card)
if test:
    print(".")

test_card=Solitair_card(1,"Heart")
Foundation=foundation()
test=Foundation.Add_to_Foundation(test_card)
if test:
    print(".")