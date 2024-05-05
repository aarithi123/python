from p1_random import P1Random
# import random numbers
rng = P1Random()
# define and initialize variables
continue_game = True
game_num = 0
player_win = 0
dealer_win = 0
tie_game = 0
completed_game = 0
# keep track of the number of games being played
while continue_game:
    game_num += 1
    print(f"START GAME #{game_num}")
    print()
    player_hand = 0
    card = rng.next_int(13) + 1
    player_hand = card
    # Assign card values
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10
    # Equate card value to player hand
    player_hand = card
    print(f"Your hand is: {player_hand}")
    print()
    current_game = True
    # display user options
    while current_game:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()
        player_action = int(input("Choose an option: "))
        print()
        # assign player with a random card from 1-13 and print the card.
        if player_action == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10
            print()
            player_hand += card
            print(f"Your hand is: {player_hand}")
            print()
            # print the result of option 1
            if player_hand == 21:
                print("BLACKJACK! You win!")
                player_win += 1
                current_game = False
                completed_game += 1
            elif player_hand > 21:
                print("You exceeded 21! You lose.")
                dealer_win += 1
                current_game = False
                completed_game += 1
            print()
        # option 2 is the dealer's turn and assign dealer with a card value from 16-26
        elif player_action == 2:
            dealer_hand = rng.next_int(11) + 16
            # print the outcome of the game by comparing dealer hand with player hand
            if dealer_hand > 21:
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}")
                print()
                print(f"You win!")
                player_win += 1
                current_game = False
                completed_game += 1
            elif dealer_hand == player_hand:
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}")
                print()
                print(f"It's a tie! No one wins!")
                tie_game += 1
                current_game = False
                completed_game += 1
            elif player_hand > dealer_hand:
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}")
                print()
                print(f"You win!")
                player_win += 1
                current_game = False
                completed_game += 1
            elif dealer_hand > player_hand:
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}")
                print()
                print(f"Dealer wins!")
                dealer_win += 1
                current_game = False
                completed_game += 1
            print()
        # use option 3 to print the statistics of previous games
        elif player_action == 3:
            print(f"Number of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {tie_game}")
            print(f"Total # of games played is: {completed_game}")
            percent_player_win = (player_win / completed_game) * 100
            print(f"Percentage of Player wins: {percent_player_win:.1f}%")
            print()
        # use option 4 to exit the game.
        elif player_action == 4:
            current_game = False
            continue_game = False
        else:
            print("Invalid input!\nPlease enter an integer value between 1 and 4.")


