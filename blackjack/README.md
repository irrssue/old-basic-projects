# Blackjack Game

Welcome to my Blackjack Game readme file. This file will explain the code for a simple game of blackjack implemented using Python.

## About the Game

Blackjack, also known as 21, is a simple card game where the player attempts to beat the dealer by getting as close to 21 points as possible without going over. The game is usually played with one or more decks of standard playing cards.

## The Code

The code for the Blackjack game is written in Python and uses the random module to generate random cards from the deck. The code contains three functions random_card(), calculate_score(), and compare(). There are also some variables used to keep track of the cards dealt to the user and the computer.

**random_card()**
The random_card() function picks a random card from the deck of cards. The deck consists of the cards from 2 to 10, with the ace having a value of 11. The function uses the random.choice() method to pick a random card from the list of cards.

**calculate_score()**
The calculate_score() function calculates the score of both the user and the computer. It takes a list of cards as input and calculates the sum of the values of the cards. If the sum of the cards is equal to 21 and the number of cards is 2, then the player has a blackjack and the function returns 0. If there is an ace in the hand and the sum is greater than 21, the ace's value is reduced from 11 to 1. The function then returns the sum of the cards.

**compare()**
The compare() function compares the scores of the user and the computer and returns a message indicating the winner of the game. If the scores are the same, then the game is a draw. If the user has a blackjack, then the user wins. If the computer has a blackjack, then the computer wins. If the user or the computer goes over 21, then the other player wins. Otherwise, the player with the higher score wins.

**The Game Loop**
The game loop starts by dealing two cards to both the user and the computer. It then enters a while loop where the user is asked if they want to draw another card or not. If the user's score is greater than 21 or the user chooses not to draw another card, the loop ends. The computer then draws cards until its score is greater than or equal to 17. The scores of the user and the computer are then compared using the compare() function, and the winner of the game is announced.

### Conclusion

This is a simple implementation of the Blackjack game using Python. The code can be improved by adding more features like splitting, doubling down, and insurance. Feel free to use this code as a starting point and add your own features to create a more complex game.
