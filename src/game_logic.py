import numpy as np


class Game:
    def __init__(self):
        self.round_idx = 1
        self.scores = {
            'player': 0,
            'computer': 0,
            'draw': 0,
        }

    def round(self):
        pass


class RockPaperScisors(Game):
    def __init__(self, computer_strategy='random'):
        super().__init__()

        self.strategy = computer_strategy

        self.sign2move = {
            'fist': 'rock',

            'stop': 'paper',
            'palm': 'paper',

            'two up': 'scisors',
            'two up inverted': 'scisors',
            'peace': 'scisors',
            'peace inverted': 'scisors',
        }

        self.allowed_signs = list(self.sign2move.keys())
        self.choices = list(set(self.sign2move.values()))

    
    def __decide_who_wins(self, player, computer):
        if player == 'rock':
            if computer == 'paper':
                return 'computer'
            elif computer == 'scisors':
                return 'player'
            return 'draw'
        
        elif player == 'paper':
            if computer == 'scisors':
                return 'computer'
            elif computer == 'rock':
                return 'player'
            return 'draw'
        
        else:  # player == 'scisors'
            if computer == 'rock':
                return 'computer'
            elif computer == 'paper':
                return 'player'
            return 'draw'


    def __computer_choice(self):
        if self.strategy == 'random':
            return np.random.choice(self.choices)
        else:
            raise NotImplementedError(f"Required strategy {self.strategy} is not available")



    def round(self, player_sign):
        if player_sign not in self.allowed_signs:
            return

        player_choice = self.sign2move[player_sign]
        computer_choice = self.__computer_choice()
        who_wins = self.__decide_who_wins(player_choice, computer_choice)
        self.scores[who_wins] += 1
        self.round_idx += 1
        return {
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'who_wins': who_wins
        }



if __name__ == '__main__':

    game = RockPaperScisors()

    for i in range(10_000):
        player_sign = np.random.choice(game.allowed_signs)
        pack = game.round(player_sign)

        text = f"Player choice: {pack['player_choice']}\n"
        text += f"Computer choice: {pack['computer_choice']}\n"
        text += f"Winner is {pack['who_wins']}"
        text += '\n\n'
        print(text)

    print(game.scores)
