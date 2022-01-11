import random
from art import logo, vs
from game_data import data


def set_random():
    """Get random data"""
    A = random.choice(data)
    return A


def format_data(account):
    """Format account into printable format: name, description and country"""
    return f"{account['name']}, a {account['description']} from {account['country']}"


def check(A, B, answer):
    """Checks followers against user's answer and returns True if they got it right.
    Or False if they got it wrong."""
    if A['follower_count'] > B['follower_count'] and answer == 'A':
        return True
    elif A['follower_count'] < B['follower_count'] and answer == 'B':
        return True
    else:
        return False


account_A = set_random()
account_B = set_random()
if account_A == account_B:
    account_B = set_random()

score = 0
keep_playing = True

while keep_playing:
    account_A = account_B
    account_B = set_random()
    if account_A == account_B:
        account_B = set_random()

    print(logo)
    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")

    answer = input("Who has more follower ? Type 'A' or 'B': ").upper()
    is_correct = check(account_A, account_B, answer)
    if is_correct:
        score += 1
        print(f"You're Right, Current score: {score}")
    else:
        print(f"That's Wrong. Final score: {score}")
        keep_playing = False

