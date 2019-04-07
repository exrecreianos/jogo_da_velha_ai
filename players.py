from random import randint

class rand_player():
    def __init__(self, name='P1', player_sign='X'):
        self.name = name
        self.sign = player_sign

    def play(self, board):
        possible = [num for num in board if num.isdigit()]
        movement = randint(0, len(possible) - 1)
        return int(possible[movement])

class human_player():
    def __init__(self, name='P1', player_sign='O'):
        self.name = name
        self.sign = player_sign

    def play(self, board):
        movement = int(input())
        return movement