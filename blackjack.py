from deck import *

class hand:
    def __init__(self, game_deck:deck):
        self.cards_in_hand = []
        self.string_hand = []
        self.info_hand = []
        self.soft_hand = False
        self.hand_value = 0

        for _ in range(2):
            self.deal_to_hand(game_deck)

    def deal_to_hand(self, game_deck:deck):
        temp_card = game_deck.deal_card()
        self.hand_value += temp_card.value()
        if temp_card.my_denom == 'A':
            self.soft_hand = True

        self.cards_in_hand.append(temp_card)   
        self.string_hand.append(temp_card.to_string())  
        self.info_hand.append(temp_card.info())  

    def get_hand_value(self):
        if self.soft_hand:
            if self.hand_value >21:
                return self.hand_value - 10
            else:
                return self.hand_value
        else:
            return self.hand_value

    ### Insert hand_cards into all 3 lists.


class house_hand(hand):
    def __init__(self, game_deck:deck):
        self.cards_in_hand = []
        self.string_hand = []
        self.info_hand = []
        self.soft_hand = False
        self.hand_value = 0
        self.up_card = None
        self.down_card = None

        self.deal_house_hand()

    def deal_to_hand(self, game_deck:deck):
        return super().deal_to_hand(game_deck)
        
    def down_card_to_hand(self,game_deck:deck):
        self.down_card = game_deck.deal_card()
        self.cards_in_hand.append(self.down_card)

    def flip_card(self):
        self.hand_value = self.down_card.value()
        if self.down_card.my_denom == 'A':
                self.soft_hand = True
    
    def deal_house_hand(self,game_deck:deck):
        self.deal_to_hand(game_deck)
        self.down_card_to_hand(game_deck)
        self.up_card = self.cards_in_hand[1]