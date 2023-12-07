# Blackjack

## Our Blackjack House Rules

* The deck is unlimited in size. 
* There are no jokers. 
* The Jack/Queen/King all count as 10.
* The the Ace can count as 11 or 1.
* Use the following list as the deck of cards:
    * `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
* The cards in the list have equal probability of being drawn.
* Cards are not removed from the deck as they are drawn.
* The computer is the dealer.

## Flowchart

<img src="./imgs/flowchart.png">

## Instructions

_**The instructions, variables, and function names offered are only recommendations for coding. You can make changes to the code as you see fit and that you think will be helpful and appropriate.**_

**You are not obligated to follow any particular instruction, but you must adhere to the house rules.**

### Sugested instructions

1. Create a `deal_card()` function that uses the List below to *`return`* a random card.
    * 11 is the Ace.
    * `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`

2. Deal the user and computer 2 cards each using deal_card() and append().
    * `user_cards = []`
    * `computer_cards = []`

3. Create a function called `calculate_score()` that takes a List of cards as input 
    * and returns the score. 
    * Look up the `sum()` function to help you do this.

4.  Inside `calculate_score()` check for a blackjack (a hand with only 2 cards: ace + 10) and return `0` instead of the actual score. `0` will represent a blackjack in our game.

5.  Inside `calculate_score()` check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up `append()` and `remove()`.

6.  Call `calculate_score()`. If the computer or the user has a blackjack (`0`) or if the user's score is over 21, then the game ends.

7.  If the game has not ended, ask the user if they want to draw another card. If yes, then use the `deal_card()` function to add another card to the `user_cards` List. If no, then the game has ended.

8.  The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

9.  Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

10. Create a function called `compare()` and pass in the `user_score` and `computer_score`. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (`0`), then the user loses. If the user has a blackjack (`0`), then the user wins. If the `user_score` is over 21, then the user loses. If the `computer_score` is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

11. Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from `art.py`.



[Project folder](../day_11/)  

[Back to README](../../README.md)