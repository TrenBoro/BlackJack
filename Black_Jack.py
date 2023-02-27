from os import sep
from Black_Jack_Classes import Deck, Hand, Chips, Game

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips are you betting? > "))
        except ValueError:
            print('\nPlease enter an integer!')
        else:
            if chips.bet > chips.total:
                print("\nYou don't have that many chips!")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_one())

def hit_or_stand(deck, hand, gamestate):
    while True:
        choice = input("\nHIT or to STAND? > ").lower()
        if choice == "hit":
            hit(deck, hand)
            gamestate.set_playing(True)
        elif choice == 'stand':
            gamestate.set_playing(False)
            print("\nThe dealer is playing")
        else:
            print("\nPlease enter <hit> or <stand> ")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print(f"HIDDEN\n{dealer.deck[1]}")
    print("\nPlayer's hand:")
    print(*player.deck, sep = "\n")
    print(f"\nPlayer is at a total of {player.value}")

def show_all(player, dealer):
    print("\nDealer's hand:")
    print(*dealer.deck, sep = "\n")
    print(f"\nDealer is at a total of {dealer.value}")
    print("\nPlayer's hand:")
    print(*player.deck, sep = "\n")
    print(f"\nPlayer is at a total of {player.value}")

def player_bust(chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def dealer_bust(chips):
    print("\nDealer busts!")
    chips.win_bet()

def player_loss(chips):
    print("\nPlayer loses!")
    chips.lose_bet()

def dealer_loss(chips):
    print("\nDealer loses!")
    chips.win_bet()

def push():
    print("\nPlayer and Dealer are at a tie. It's a push!!!!")

def main():

    player_chips = Chips() # So that we don't lose chips between rounds

    while True:
        print("\tWELCOME TO BLACKJACK!!!\n\n")

        game = Game()
        #game.get_playing()

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal_one())
        player_hand.adjust_aces()
        player_hand.add_card(deck.deal_one())
        player_hand.adjust_aces()

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        print("\nThe player and dealer have been dealt the cards!")
        
        show_some(player_hand, dealer_hand)

        print(f"You have {player_chips.total} chips!")

        take_bet(player_chips)

        while game.get_playing():
            hit_or_stand(deck, player_hand, game)
            player_hand.adjust_aces()

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_bust(player_chips)
                break # break out of playing

        if player_hand.value <= 21 and not game.get_playing():
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)
            
            if dealer_hand.value > 21:
                dealer_bust(player_chips)
            elif dealer_hand.value > player_hand.value:
                player_loss(player_chips)
            elif dealer_hand.value < player_hand.value:
                dealer_loss(player_chips)
            else:
                push()

        print(f"Game ended with {player_chips.total}\n\n")

        again = input("\tWould you like to play again? y/n > ").lower()

        if player_chips.total <= 0:
            print("\nYou don't have any chips left...")
            exit()

        elif again == 'y':
            continue
    
        else:
            print("Bye! Thanks for playing!")
            break

if __name__ == '__main__':
    main()