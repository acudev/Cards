import random
class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '[%s of %s]' % (Card.rank_names[self.rank],
                               Card.suit_names[self.suit])
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
       return self.cards.pop()
