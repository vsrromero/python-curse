""" Auction program """

import art
import helper
import auction

helper.clear_output()

print(art.logo)
print("Welcome to the secret auction program.")

auction_is_running = True
bidders = []

while auction_is_running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    auction.add_bidder(bidders, name, bid)
    
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    while new_bidder != 'yes' and new_bidder != 'no':
        new_bidder = input("Please, choose a valid answer, 'yes' or 'no': ").lower()
    
    if new_bidder == 'no':
        winner_bidder, winner_bid = auction.get_winner_bidder(bidders)
        print(f"The winner is {winner_bidder} with a bid of ${winner_bid}")
        auction_is_running = False
    else:
        helper.clear_output()
        
