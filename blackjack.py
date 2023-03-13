from player import Player
from dealer import Dealer

 
class BlackjackGame:
    def __init__(self, player_names):
        # Create an empty list to hold Player objects and create a Dealer object
        self.player_list=[]
        self.dealer=Dealer() 

        # For each player name passed in the player_names list, create a Player object with the name
        # and the Dealer object as arguments and add it to the player_list
        for a in player_names:
            p=Player(a,self.dealer)
            self.player_list.append(p)

    def play_rounds(self, num_rounds=1): 
        """
        Simulates playing num_rounds rounds of Blackjack and returns a string describing the results

        :param num_rounds: Number of rounds to simulate (default=1)
        :return: A string describing the results of each round
        """
        
        # Initialize an empty string to hold the output
        out=""

        # Play num_rounds rounds
        for roundp in range(num_rounds):

            # Shuffle the deck before every round
            self.dealer.shuffle_deck()

            # Add a new line to the output string to separate rounds
            out+= "Round "+str(roundp+1)+'\n'

            # Deal two cards to each player and the dealer
            for x in range(0,2):
                    
                for y in self.player_list:
                    # Signal each player to draw a card from the deck
                    self.dealer.signal_hit(y)
                # Signal the dealer to draw a card from the deck
                self.dealer.signal_hit(self.dealer)
                
            # Allow each player to play their turn
            for i in self.player_list:
                i.play_round()
            # Allow the dealer to play their turn
            self.dealer.play_round()
            # Add a string representation of the dealer's hand to the output string
            out+= str(self.dealer)+ '\n'
            
            # Determine the winner of the round for each player and update their win/loss statistics
            for ply in self.player_list:

                if ply.card_sum > self.dealer.card_sum:
                    ply.record_win()

                elif ply.card_sum==self.dealer.card_sum:
                    ply.record_tie()

                else:
                    ply.record_loss()

                # Add a string representation of the player's hand and statistics to the output string
                out+=str(ply)+ '\n'
                # Discard the player's hand
                ply.discard_hand()
            # Discard the dealer's hand
            self.dealer.discard_hand()    
        
        # Remove the trailing whitespace from the output string and return it
        out=out.rstrip()
        return out         
        
            

               

    def reset_game(self):
        """
        Resets the game by discarding all player and dealer hands and resetting win/loss statistics

        :return: None
        """

        # For each player in the player_list, discard their hand and reset their win/loss statistics
        for x in self.player_list:
            x.hand=[]
            x.reset_stats()
            # Discard the dealer's hand
            self.dealer.hand=[] 
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
