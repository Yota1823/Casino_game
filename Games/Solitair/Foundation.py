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
        if (len(stack)==0 and card.value==1) or (len(stack)>0 and stack[-1].below(card)):
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

# test_card=Solitair_card(1,"Heart")
# Foundation=foundation()
# test=Foundation.Add_to_Foundation(test_card)
# test_card2=Solitair_card(2,"Heart")
# test2=Foundation.Add_to_Foundation(test_card2)
# if test:
#      print(".")


# if not test :
#       print(">>>")





# Suit= Foundation.get_last_card("Heart")
# print(Suit)