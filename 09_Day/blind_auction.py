from replit import clear
from art import logo

auction_data = {}
auction = True

def add_bidder(player, amount):
    auction_data[player] = amount

def who_won(payer_data):
    max_bid = 0
    max_bidder = ""
    for bidder in payer_data:
        if payer_data[bidder] > max_bid:
            max_bid = payer_data[bidder]
            max_bidder = bidder

    return max_bidder, max_bid

while auction:
    print(logo)
    bidder_name = input("What is your name: ")
    bid = int(input("what is your bid amount: $"))

    add_bidder(player=bidder_name, amount=bid)

    repeat = input("Is there any other bidder who want to bid? 'Y' to Enter his bid or 'N' to see who won\n").lower()
    if repeat == "y":
        clear()
    else:
        winner, amount_bid = who_won(payer_data=auction_data)
        print(f"The winner of Bid is {winner} because he/she bid the highest amount ${amount_bid}.")
        auction = False
