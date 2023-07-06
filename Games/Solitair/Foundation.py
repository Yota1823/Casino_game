from card import Solitair_card
class Foundation:
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
