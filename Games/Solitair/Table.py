from card import Solitair_card
from Foundation import foundation
from Deck import Dek
class Tableau:

    def __init__(self,card_l):
       
        self.unfliped= {x: card_l[x:x+x+1] for x in range(7)}
        self.flip={x:[self.unfliped[x].pop()] for x in range(7)}

    def flip_Card(self,col):
        if len(self.unfliped[col]) >0:
            self.flip[col].append(self.unfliped[col].pop())
    
    def pile_l(self):
        return max(len(self.unfliped[x])+ len (self.flip[x]) for x in range (0,7))
    
    def add_C_T(self,Cl,CL,index):
        Card= self.flip[CL]
        Card2= self.flip[Cl]
        verify1=Card2[index].Attach(Card[-1])
        if len(Card)==0:
            self.flip[CL].append(Card2[-1])
            del (Card2[-1])
            if len(Card2)==0:
              self.flip_Card(Cl)
        
        
        elif len(Card)>0 and verify1:
             #for card in range (len(self.flip[Cl])):
             self.flip[CL].extend(Card2[index:])
             del (Card2[index:])
             if len(Card2)==0:
                 self.flip_Card(Cl)
             return True
        
        else:
            return False
        
    
       
    def add_W_T(self,waste_pile,CL):
        Card=waste_pile.waste[-1]
        Card2=self.flip[CL]
        if len(Card2)==0:
             
             self.flip[CL].append(Card)
        Verify=Card.Attach(Card2[-1])
        if len(Card2)>0 and Verify:
            self.flip[CL].append(Card)
            return True
        else:
            return False

    



    
    # def Tableau_to_Tableau(self,CL1,CL2,x):
    #     C_pile1= self.flip[CL1]
    #     C_pile2=self.flip[CL2]
        
        
    #     if x <= len(C_pile1):
    #         if self.add_C(C_pile1[-1],C_pile2[-1]):
    #          self.flip[CL2].append(C_pile1[x:])
    #          del C_pile1[x:]
    #          if x==0:
    #              self.flip_Card(CL1)
    #              return True
    #     return False    
    
    def add_T_F(self,foundation,column):
        card_column= self.flip[column]
        if len(card_column)==0:
            return False
        if foundation.Add_to_Foundation(card_column[-1]):
            card_column.pop()
            if len(card_column)==0:
                self.flip_Card(column)
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
        t1=len(self.unfliped[0])
        t2=len(self.unfliped[1])
        t3=len(self.unfliped[2])
        t4=len(self.unfliped[3])
        t5=len(self.unfliped[4])
        t6=len(self.unfliped[5])
        t7=len(self.unfliped[6])
        print("Column 1  Column 2  Column 3  Column 4  Column 5  Column6  Column 7")
        print(f"{t1}          {t2}         {t3}          {t4}          {t5}         {t6}          {t7}")
    def display_flip(self):   
        for Col, Cards in self.flip.items():
            print(f" flip {Col+1}")
            for Card in Cards :
                print(Card.value,Card.suit)
        print()
    
    def display_col(self,col):
       
        print(f'This is {col}')
        for card in self.unfliped[col] :
            print(card.value,card.suit)

    def display_c(self):
        t1=len(self.flip[0])
        t2=len(self.flip[1])
        t3=len(self.flip[2])
        t4=len(self.flip[3])
        t5=len(self.flip[4])
        t6=len(self.flip[5])
        t7=len(self.flip[6])
        w=8
        row=[]
        row2=[]
        row3=[]
        row4=[]
        row5=[]
        row6=[]
        row7=[]
        max_card=max(t1,t2,t3,t4,t5,t6,t7)
        for i in range (max_card):
         row.append(str(self.flip[0][i])) if i<t1 else ""
         row2.append(str(self.flip[1][i])) if i<t2 else ""
         row3.append(str(self.flip[2][i])) if i<t3 else ""
         row4.append(str(self.flip[3][i])) if i<t4 else ""
         row5.append(str(self.flip[4][i])) if i<t5 else ""
         row6.append(str(self.flip[5][i])) if i<t6 else ""
         row7.append(str(self.flip[6][i])) if i<t7 else ""
        max_c=max(len(row),len(row2),len(row3),len(row4),
        len(row5),len(row6),len(row7))
        for i in range (max_c):
         Card=row[i].ljust(w) if i<t1 else "".ljust(w)
         Card2=row2[i].ljust(w) if i<t2 else "".ljust(w)
         Card3=row3[i].ljust(w) if i<t3 else "".ljust(w)
         Card4=row4[i].ljust(w) if i<t4 else "".ljust(w)
         Card5=row5[i].ljust(w) if i<t5 else "".ljust(w)
         Card6=row6[i].ljust(w) if i<t6 else "".ljust(w)
         Card7=row7[i].ljust(w) if i<t7 else "".ljust(w)
         print(f"|{Card}| |{Card2}| |{Card3}| |{Card4}| |{Card5}| |{Card6}| |{Card7}|")
        
    def table_check(self,t1,t2):
        T=len(self.unfliped[t1])
        T2=len(self.unfliped[t2])
        print(f"Column {t1}")
        print(f"Length: {T}")
        for card in self.flip[T]:
            print(f"{card.value}:{card.suit}")
        print("\t")
        print(f"Column {t2}")
        print(f"Length : {T2}")
        print("\t")
        for card in self.flip[T2]:
            print(f"{card.value}:{card.suit}")
            

    #def display_card(self):
        

        
         
         
            



# Test_Deck= Dek(1)
# Numb_Deck= Test_Deck.deal_c(28)
# Test_Tableau= Tableau(Numb_Deck)
# Foundation=foundation()
# Test_Tableau.display_c()
# card=int(input("Enter column :"))
# test2=Test_Tableau.add_T_F(Foundation,card)
# if test2:
#     print("...")
# print(" This is the card in the deck ")
# #for cards in Numb_Deck:
#    # print(cards)

# #Test_Tableau.flip_Card(2)
# Test_Tableau.flip_Card(5)

# pile_l=Test_Tableau.pile_l()

# Test_Tableau= Tableau(Numb_Deck)
# Test_Tableau.display_c(1)
# print("_____________")
# Test_Tableau.display_c(2)
# print("_____________")
# Test_Tableau.display_c(3)
# print("_____________")
# Test_Tableau.display_c(4)
# print("_____________")
# Test_Tableau.display_c(5)
# print("_____________")
# Test_Tableau.display_c(6)
# print("_____________")
# while(1):

    

#     command=input(" Enter a number :")


#     value=input("Enter column 1:")
#     v=int(value)
#     value1=input(" Enter a column 2 :")
#     v1=int(value1)
#     # index=input(" Enter a number: ")
#     # i=int(index)
#     #dummy_card=Solitair_card(v,suit)
#     #Add= Test_Tableau.add_C(dummy_card,4)
#     test= Test_Tableau.add_C_T(v,v1)
#     print(test)
#     #print(Add)
#         #Test_Tableau.display_lip()
#     print("_________")
#     Test_Tableau.display_c(1)
#     print("_____________")
#     Test_Tableau.display_c(2)
#     print("_____________")
#     Test_Tableau.display_c(3)
#     print("_____________")
#     Test_Tableau.display_c(4)
#     print("_____________")
#     Test_Tableau.display_c(5)
#     print("_____________")
#     Test_Tableau.display_c(6)
#     print("_____________")


#     print(pile_l)

