import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Deck:

    def __init__(self):
        self.all_card = []
            
        for suit in suits:
            for rank in ranks:
                obj = Card(suit,rank)
                self.all_card.append(obj)

    def shuffle(self):
        random.shuffle(self.all_card)

    def pic_card(self):
        return self.all_card.pop()



class Player:

    def __init__(self,name):
        self.name = name
        self.player_all_card = []

    def remove_one_card(self):
        return self.player_all_card.pop(0)

    def add_card(self,card):
        if type(card) == type([]):
            self.player_all_card.extend(card)
        else:
            self.player_all_card.append(card)

    def __str__(self):
        return f"Player {self.name} has {len(self.player_all_card)} cards"
    

player_one = Player("Prateek")
player_two = Player("Yadav")

my_deck = Deck()
my_deck.shuffle()

length_of_card = len(my_deck.all_card)

for i in range(int(length_of_card/2)):
    player_one.add_card(my_deck.pic_card())
    player_two.add_card(my_deck.pic_card())



is_game_start = input("You Want To Start Game ? Y/N: ")
if is_game_start == 'Y' or is_game_start =='y':
    is_game_start = True
else:
    is_game_start = False

war_pile = []

while is_game_start:

    if len(player_one.player_all_card) == 0 :
        print("Player One Out !! No More Card Available")
        break
    elif len(player_two.player_all_card) == 0 :
        print("Player Two Out !! No More Card Available")
        break
    else:
        print("Length Of Player One Cards : ", len(player_one.player_all_card))
        print("Length Of Player Two Cards : ", len(player_two.player_all_card))

        player_one_card = player_one.remove_one_card()
        player_two_card = player_two.remove_one_card()

        print(f"Player One Card : {player_one_card.value}")
        print(f"Player Two Card : {player_two_card.value}")

        if player_one_card.value == player_two_card.value :
            print("Value Is Same\nSkip 3 Card")
            war_pile.append(player_one_card)
            war_pile.append(player_two_card)
            if len(player_one.player_all_card)<3:
                print("Player Two Is Win")
                break
            elif len(player_two.player_all_card) <3:
                print("Player One Is Win ")
                break
            else:
                for i in range(3):
                    skip_player_one_card = player_one.remove_one_card()
                    skip_player_two_card = player_two.remove_one_card()
                    war_pile.append(skip_player_one_card)
                    war_pile.append(skip_player_two_card)
                continue
        elif player_two_card.value > player_one_card.value:
            if war_pile:
                player_two.add_card(war_pile)
                war_pile = []
            player_two.add_card([player_one_card, player_two_card])
        elif player_one_card.value > player_two_card.value:
            if war_pile:
                player_one.add_card(war_pile)
                war_pile = []
            player_one.add_card([player_one_card, player_two_card])
        else:
            print("Else Part !!")


