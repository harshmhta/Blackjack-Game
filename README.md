# Blackjack Game

This is a Python implementation of Blackjack, which can be played by multiple players. The game involves drawing cards from a deck and trying to get a hand that is worth more than the dealer's hand, without going over 21.

## Installation

Clone this repository to your local machine.

## Usage

To play the game, import the BlackjackGame class and create an instance of it with a list of player names as an argument. Then call the play_rounds method to start playing the game.

The play_rounds method takes an optional argument num_rounds that specifies the number of rounds to play. The default value is 1.

## Game Rules
In this implementation of Blackjack, each player plays against the dealer. At the start of each round, the dealer shuffles the deck and deals two cards to each player and to themselves. The players can see their own cards and one of the dealer's cards. The other card is face down.

The goal of the game is to get a hand that is worth more than the dealer's hand, without going over 21. The value of a hand is the sum of the point values of the individual cards. The point values of the cards are as follows:

1. Numbered cards are worth their face value (e.g. a 2 of hearts is worth 2 points).
2. Face cards (jack, queen, king) are worth 10 points each.
3. Aces can be worth either 1 or 11 points, depending on which value would be more beneficial to the player.

After the initial deal, each player takes a turn to decide whether to "hit" (draw another card) or "stand" (keep their current hand). If a player's hand goes over 21 points, they "bust" and automatically lose the round.

After all players have taken their turns, the dealer reveals their face-down card and hits until their hand is worth at least 17 points. If the dealer busts, all remaining players win the round. Otherwise, the player with the highest hand value wins the round. If multiple players have the same highest hand value, it is a tie.

## Project Description

This project involved implementing four classes: CardDeck, Dealer, Player, and BlackjackGame.

The CardDeck class represents a deck of cards. It has methods for shuffling the deck and dealing cards.

The Dealer class represents the dealer in the Blackjack game. It has methods for dealing cards to players and for hitting (drawing another card) when necessary.

The Player class represents a player in the Blackjack game. It has methods for hitting, standing, and recording wins/losses/ties.

The BlackjackGame class is the main class that runs the Blackjack game. It has methods for playing rounds of the game and resetting the game.

The doctest module was used to test the functionality of the classes and methods.

## Academic Integrity Statement

Please note that all work included in this project is the original work of the author, and any external sources or references have been properly cited and credited. It is strictly prohibited to copy, reproduce, or use any part of this work without permission from the author.

If you choose to use any part of this work as a reference or resource, you are responsible for ensuring that you do not plagiarize or violate any academic integrity policies or guidelines. The author of this work cannot be held liable for any legal or academic consequences resulting from the misuse or misappropriation of this work.

In summary, any unauthorized copying or use of this work may result in serious consequences, including but not limited to academic penalties, legal action, and damage to personal and professional reputation. Therefore, please use this work only as a reference and always ensure that you properly cite and attribute any sources or references used.
