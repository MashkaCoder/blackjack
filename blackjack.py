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
        money -= 1000
        bet = get_bet(money)


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
    game()


if __name__ == "__main__":
    main()
