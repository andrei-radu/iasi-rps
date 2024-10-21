import random

class Strategy:
    """ Class for computer strategy. """
    def __init__(self):
        """ Initialize the strategy object properties. """
        pass

    def move(self):
        """ Return the move. """
        pass

    def update(self, player, computer):
        """ Update the strategy based on the last round. """
        pass
    
    
    
class RandomStrategy(Strategy):
    """ Class for computer random move strategy. """
    def __init__(self):
        """ Initialize the random strategy object properties. """
        super().__init__()

    def move(self):
        """ Return the move. """
        return random.choice(['rock', 'paper', 'scissors'])

    def update(self, player, computer):
        """ Update the strategy based on the last round. """
        pass  # nothing to update
    
    def __call__(self):
        return self.move()
    
    
    
if __name__ == '__main__':
    strat = RandomStrategy()

    for _ in range(10):
        print(strat())