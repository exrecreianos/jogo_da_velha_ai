
class tictactoe():
    
    def __init__(self, player1=None, player2=None):
        self.board = ['1','2','3',
                    '4','5','6',
                    '7','8','9']
        self.turn = 1 # 1 - Player 1 | 2 - Player 2
        self.p_char = 'X'
        self.c_char = 'O'
        self.player1 = player1
        self.player2 = player2
        self.playerToPlay = 0

    def winner(self):
        for i in ['X','O']:
            # horizontal
            if self.board[0] == self.board[1] == self.board[2] == i: return i
            if self.board[3] == self.board[4] == self.board[5] == i: return i
            if self.board[6] == self.board[7] == self.board[8] == i: return i
            # vertical
            if self.board[0] == self.board[3] == self.board[6] == i: return i
            if self.board[1] == self.board[4] == self.board[7] == i: return i
            if self.board[2] == self.board[5] == self.board[8] == i: return i
            # diagonal
            if self.board[0] == self.board[4] == self.board[8] == i: return i
            if self.board[6] == self.board[4] == self.board[2] == i: return i
        return None

    def view(self):
        print(" %s | %s | %s " % (self.board[0],self.board[1],self.board[2]))
        print("---+---+---")
        print(" %s | %s | %s " % (self.board[3],self.board[4],self.board[5]))
        print("---+---+---")
        print(" %s | %s | %s " % (self.board[6],self.board[7],self.board[8]))

    def move(self,pos):

        if not pos: return None
        if not 0 < pos < 10: return False
        if self.board[pos-1] in ['X','O']: return False

        self.board[pos-1] = ('O','X')[self.turn == 1]
        self.turn = (1,2)[self.turn == 1]
    
    def play(self):
        while True:
            self.view()

            print("Player {}: ".format(self.turn))
            movement = int(input())
            self.move(movement)

            win = self.winner()
            if not win: continue
            if win == self.p_char:
                print("Player 1 Wins!")
                input()
                exit(0)
            if win == self.c_char:
                print("Player 2 Wins!")
                input()
                exit(0)


game = tictactoe()
game.play()