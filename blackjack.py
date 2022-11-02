import random

HEARTS = chr(9829)  # Symbol 9829 — '♥'.
DIAMONDS = chr(9830)  # Symbol 9830 — '♦'.
SPADES = chr(9824)  # Symbol 9824 — '♠'.
CLUBS = chr(9827)  # Symbol 9827 — '♣'.

BACKSIDE = 'backside'


def game() -> None:
    money = 5000
    print(money, "$")
    while True:
        if money <= 0:
            print("""You're broke.\nThank's for playing!""")
            exit()
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        print("Bet: ", bet)
        while True:
            display_hand(player_hand, dealer_hand, False)
            if count_value(player_hand) > 21:
                break
            move = get_move(player_hand, money)
            if move == 'D':
                add_bet = get_bet(money-bet)
                bet += add_bet
                print("You raised the bet by {}".format(add_bet))
                print("Bet:", bet)
            if move in ('H', 'D'):
                card = deck.pop()
                print("You took a {} of {}".format(card[0], card[1]))
                player_hand.append(card)
            if move == 'S':
                break
        if count_value(dealer_hand) <= 21:
            while count_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hand(player_hand, dealer_hand, False)
                if count_value(dealer_hand) > 21:
                    break
        display_hand(player_hand, dealer_hand, True)
        player_value = count_value(player_hand)
        dealer_value = count_value(dealer_hand)
        if dealer_value > 21 or (player_value > dealer_value and player_value <= 21):
            print("You won {}$!".format(bet))
            money += bet
        elif player_value < dealer_value or player_value > 21:
            print("You've lost")
            money -= bet
        elif player_value == dealer_value:
            print("It's a tie, the bet returned to you")
        print("Your money: {}$".format(money))


def get_bet(max_bet: int) -> int:
    while True:
        print("How much do you bet? (1-{} or QUIT)".format(max_bet))
        bet = input('>').upper().strip()
        if bet == "QUIT":
            print("Thank's for playing!")
            exit()
        if not bet.isdecimal():
            print("Invalid bet")
            continue
        bet = int(bet)
        if bet < 1:
            print("Bet is so small.")
            continue
        elif bet > max_bet:
            print("Bet is so big.")
            continue
        else:
            return bet


def get_deck() -> list:
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((rank, suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hand(player: list, dealer: list, suit: bool) -> None:
    if not suit:
        print("DEALER: ???")
        display_card([BACKSIDE] + dealer[1:])
    else:
        print("DEALER: ", count_value(dealer))
        display_card(dealer)
    print("\nPLAYER:", count_value(player))
    display_card(player)


def display_card(cards: list) -> None:
    rows = ['', '', '', '']
    for card in cards:
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rows[1] += '|{} | '.format(str(card[0]).ljust(2))
            rows[2] += '| {} | '.format(card[1])
            rows[3] += '|_{}| '.format(str(card[0]).rjust(2, "_"))
    for row in rows:
        print(row)


def count_value(cards: list) -> int:
    value = 0
    count_aces = 0
    for card in cards:
        if card[0] in ('J', 'Q', 'K'):
            value += 10
        elif card[0] == 'A':
            count_aces += 1
        else:
            value += card[0]
    value += count_aces
    if count_aces and value + 10 <= 21:
        value += 10
    return value


def get_move(player_hand: list, money: int) -> str:
    while True:
        moves = ['(S)tand', '(H)it']
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)oudle down')
        print(moves)
        move = input('>').upper()
        if move in ('S', 'H'):
            return move
        elif move == 'D' and '(D)oudle down' in moves:
            return move


def print_rules() -> None:
    print("""Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.""")


def main():
    print_rules()
    try:
        game()
    except KeyboardInterrupt as e:
        print("Something wrong. Try again.")


if __name__ == "__main__":
    main()
