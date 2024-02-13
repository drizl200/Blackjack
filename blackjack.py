from deck import *

class hand:
    def __init__(self):
        self.cards_in_hand = []
        self.string_hand = []
        self.info_hand = []
        self.soft_hand = False
        self.hand_value = 0

    def insert_into_hand(self, insert_card:card):
        self.hand_value += insert_card.value()
        if insert_card.my_denom == 'A':
            self.soft_hand = True
        self.cards_in_hand.append(insert_card)   
        self.string_hand.append(insert_card.to_string())  
        self.info_hand.append(insert_card.info())  

    def deal_to_hand(self, game_deck:deck):
        temp_card = game_deck.deal_card()
        self.insert_into_hand(temp_card)

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
        self.own_card = None
        self.deal_house_hand(game_deck)

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

class player:
    def __init__(self, cash, cash_unit):
        self.player_hands = [hand()]
        self.num_of_hands = 1
        self.cash = cash
        self.cash_unit = cash_unit

    def player_deal(self, game_deck:deck):
        self.player_hands[0].deal_to_hand(game_deck)

    def get_player_hand_string(self, hand_index):
        return self.player_hands[hand_index].string_hand
    
    def get_player_hand_info(self, hand_index):
        return self.player_hands[hand_index].info_hand
    
    def get_player_cards_in_hand(self, hand_index):
        return self.player_hands[hand_index].cards_in_hand

    def player_deal(self, hand_index, game_deck:deck):
        self.player_hands[hand_index].deal_to_hand(game_deck)

    def get_player_hand_string(self, hand_index):
        return self.player_hands[hand_index].string_hand
    
    def get_player_hand_info(self, hand_index):
        return self.player_hands[hand_index].info_hand
    
    def get_player_cards_in_hand(self, hand_index):
        return self.player_hands[hand_index].cards_in_hand

    def split_hand(self, hand_index, game_deck:deck):
        hand_to_split = self.player_hands.pop(hand_index)
        new_hand_1 = hand()
        new_hand_1.insert_into_hand(hand_to_split.cards_in_hand[0])
        new_hand_1.deal_to_hand(game_deck)

        new_hand_2 = hand()
        new_hand_2.insert_into_hand(hand_to_split.cards_in_hand[1])
        new_hand_2.deal_to_hand(game_deck)

        self.player_hands.append(new_hand_1)
        self.player_hands.append(new_hand_2)
        self.num_of_hands += 1