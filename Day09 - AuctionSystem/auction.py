""" Helper Functions to auction """

def add_bidder(bidders, name, bid):
    bidder = {'name': name, 'bid': bid}
    bidders.append(bidder)
    
def get_winner_bidder(bidders):
    if not bidders:
        return None, None
    
    winner = max(bidders, key=lambda x: x['bid'])
    return winner['name'], winner['bid']
