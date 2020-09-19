'''
Wellcomw to the game of cards called wars
'''
import random
suits=('Hearts','Diamonds','Clubs','Spades')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
'''
Class for giving properties to a particular card like its rank,suits
etc
'''
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank+ " of "+self.suit

'''
Class of deck of 52 cards in which each card is created and gets its
suits and ranks and stored in list
'''
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                # Creating a card object
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def suffle_deck(self):
        random.shuffle(self.all_cards)
    def card_out(self):
        try:
            return self.all_cards.pop()
        except IndexError:
            return "All cards are out"                    

'''
Class for adding a player in which player can add
and remove the cards from his/her own decks
'''            
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_card(self):
        return self.all_cards.pop(0)
    
    def add_card(self,new_cards):
        if type(new_cards) is type([]):
            #For MULTIPLE CARDS
            self.all_cards.extend(new_cards)
        else:
            #For SINGLE CARD
            self.all_cards.append(new_cards)
    def __str__(self):
        if len(self.all_cards) is 1:
            return ('Player {} has {} card left'.format(self.name,len(self.all_cards)))
        return ('Player {} have {} cards left'.format(self.name,len(self.all_cards)))

##Game Setup
player_one=Player("One")
player_two=Player("Two")

new_deck = Deck()
new_deck.suffle_deck()

for x in range(26):
    player_one.add_card(new_deck.card_out())
    player_two.add_card(new_deck.card_out())

game_on=True

round_num=0
while game_on:
    round_num+=1
    print("Round {}".format(round_num))
    if len(player_one.all_cards) is 0:
        print("Player 1 is out of the cards!!!Player 2 wins")
        game_on=False
        break
        
    if len(player_two.all_cards) is 0:
        print("Player 2 is out of the cards!!!Player 1 wins")
        game_on=False
        break    
        
    #Start A new round
    player_one_cards=[]
    player_one_cards.append(player_one.remove_card())
   
    player_two_cards=[]
    player_two_cards.append(player_two.remove_card())
    
    
    at_war= True
    
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war=False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war=False
        else:
            print("WAR!!!")
            
            if len(player_one.all_cards)<5:
                print("Player 1 Unable To Declare War!!!\nPlayer 2 Win!!!")
                game_on = False
                break
            elif len(player_two.all_cards)<5:
                print("Player 2 Unable To Declare War!!!\nPlayer 1 Win!!!")
                game_on = False
                break
            else:
                for _ in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())                