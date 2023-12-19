import random as r

suit ={'s':'Spades', 'c':'Clubs', 'd':'Diamonds', 'h':'Hearts'}
denom ={'A':'Ace', 'K':'King', 'Q':'Queen', 'J':'Jack', '10':'Ten', '9':'Nine', '8':'Eight', '7':'Seven','6':'Six',
             '5':'Five', '4':'Four', '3':'Three', '2':'Two'}

class card:
    def __init__(self, denom_choice=denom, suit_choice=suit):
        self.my_denom = denom_choice
        self.my_suit = suit_choice

    def value(self): 
        if self.my_denom == 'A':
            return 11
        elif self.my_denom in ('K', 'Q', 'J'):
            return 10
        else: 
            return int(self.my_denom)
        
    def info(self):
        return self.my_denom, self.my_suit
        
    def to_string(self):
        card_string = denom[self.my_denom] + " of " + suit[self.my_suit]
        return card_string
        
class deck:
    deck_of_cards = []
    string_deck = []
    info_deck= []

    def __init__(self, num_of_decks):
        self.shuffle(num_of_decks)
    
    def shuffle(self, num_of_decks):
        for n in range(num_of_decks):
            for i in suit:
                for j in denom:
                    self.add_card(j,i)

    def get_deck_size(self):
        return len(self.deck_of_cards)
    
    def clear_deck(self):
        self.deck_of_cards = []
        self.string_deck = []
        self.info_deck = []

    def add_card(self, denom_choice=denom, suit_choice=suit):
        temp_card = card(denom_choice, suit_choice)
        self.deck_of_cards.append(temp_card)
        self.string_deck.append(temp_card.to_string())
        self.info_deck.append(temp_card.info())

    def remove_card(self, card_index):
        del self.deck_of_cards[card_index]
        del self.string_deck[card_index]
        del self.info_deck[card_index]

    def deal_card(self):
        card_index = r.randint(0, self.get_deck_size())
        card_deal = self.deck_of_cards[card_index]
        self.remove_card(card_index)
        return card_deal
