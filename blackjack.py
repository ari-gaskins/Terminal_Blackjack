import random


is_hit = False
is_hold = False

def show_hands(user_hand, dealer_hand):
    print(f'Your hand: {user_hand}')
    print(f'Dealer card: {dealer_hand[0]}')


# setup hands
def set_user():
    user_hand = []

    for i in range(2):
        user_hand.append(random.randint(1,10))
   
    return user_hand


def set_dealer():
    dealer_hand = []

    for i in range(2):
        dealer_hand.append(random.randint(1, 10))
    
    return dealer_hand


# take in user input, continue asking until they say hit or hold
def get_input(user_hand, dealer_hand):
    global is_hit, is_hold
    hit_or_hold = input('Enter hit or hold: ')
    hit_or_hold = hit_or_hold.lower()

    while not is_hold:
        if hit_or_hold == 'hit':
             is_hit = True
             is_hold = False
             check_input(user_hand, dealer_hand)

        elif hit_or_hold == 'hold':
            is_hold = True
            is_hit = False
            check_input(user_hand, dealer_hand)

        else:
            hit_or_hold = input('Enter hit or hold: ')
            hit_or_hold = hit_or_hold.lower()


# react to user action
def check_input(user_hand, dealer_hand):
    global is_hit, is_hold

    def add_user_vals(user_hand, dealer_hand):
        user_hand.append(random.randint(1,10))
        print(f'Your hand: {user_hand}')
        get_input(user_hand, dealer_hand)

    if is_hit:
        add_user_vals(user_hand, dealer_hand)

    elif is_hold:
        print(f'Dealer hand: {dealer_hand}')

user_hand = set_user()
dealer_hand = set_dealer()

show_hands(user_hand, dealer_hand)
get_input(user_hand, dealer_hand)
show_hands(user_hand, dealer_hand)
check_input(user_hand, dealer_hand)

