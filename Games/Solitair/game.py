
# class Tableau():
# 	# Class that keeps track of the seven piles of cards on the Tableau

# 	def __init__(self, card_list):
# 		self.unflipped = {x: card_list[x] for x in range(7)}
# 		self.flipped = {x: [self.unflipped[x].pop()] for x in range(7)}

# 	def flip_card(self, col):
# 		""" Flips a card under column col on the Tableau """
# 		if len(self.unflipped[col]) > 1:
# 			self.flipped[col].append(self.unflipped[col].pop())

# 	def pile_length(self):
# 		""" Returns the length of the longest pile on the Tableau """
# 		return max([len(self.flipped[x]) + len(self.unflipped[x]) for x in range(7)])

	 

	
    
# card_list=[
#     ['4 Heart'],
#     ['5 Heart'],
#     ['7 Spade'],
#     ['10 Club'],
#     ['4 Spade'],
#     ['11 Spade'],
#     ['6 Club'],
#     ['4 Club']
# ]

# Test_Table= Tableau(card_list)
# Test_Table.flip_card(0)
# Test_Table.flip_card(1)
# pile = Test_Table.pile_length()
# print(pile)




