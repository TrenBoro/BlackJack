import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Game():

    def __init__(self, playing = True):
        self.playing = playing

    def get_playing(self):
        return self.playing

    def set_playing(self, state):
        self.playing = state

class Card():
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += card.__str__() + "\n"

        return "The deck consists of: \n" + deck_str
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

class Hand():

    def __init__(self):
        self.deck = []
        self.num_aces = 0
        self.value = 0

    def adjust_aces(self):
        if self.deck[-1].rank == 'Ace':
            choice = input("Would you like to change the Ace's value? y/n > ").lower()
            if choice == 'y':
                print("Ace's value has been changed!")
                self.num_aces -= 1
                self.value -= 10
            elif choice == 'n':
                print("Ace stays the same!")
            else:
                print("Wrong input format, but whatever. Ace stays the same!")

    def add_card(self, card):
        self.deck.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.num_aces += 1

    def __str__(self):
        hand_str = ''
        for card in self.deck:
            hand_str += card.__str__() + '\n'
        return f"The player has the following cards:\n" + hand_str

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet