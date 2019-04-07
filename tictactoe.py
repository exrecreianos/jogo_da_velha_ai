from random import randint

from players import human_player, rand_player

class tictactoe():
    
    def __init__(self, player1=None, player2=None):
        self.board = ['1','2','3',
                    '4','5','6',
                    '7','8','9']
        self.turn = 1 # 1 - Player 1 | 2 - Player 2
        self.player1 = player1
        self.player2 = player2
        self.palyersSigns = [player1.sign, player2.sign]

    def winner(self):
        pl = self.getPlayerOfTurn()
        # horizontal
        if self.board[0] == self.board[1] == self.board[2] == pl.sign: return True
        if self.board[3] == self.board[4] == self.board[5] == pl.sign: return True
        if self.board[6] == self.board[7] == self.board[8] == pl.sign: return True
        # vertical
        if self.board[0] == self.board[3] == self.board[6] == pl.sign: return True
        if self.board[1] == self.board[4] == self.board[7] == pl.sign: return True
        if self.board[2] == self.board[5] == self.board[8] == pl.sign: return True
        # diagonal
        if self.board[0] == self.board[4] == self.board[8] == pl.sign: return True
        if self.board[6] == self.board[4] == self.board[2] == pl.sign: return True
        return False

    def endGame(self):
        possible = [num for num in self.board if num.isdigit()]
        return len(possible) <= 0

    def view(self):
        print(" %s | %s | %s " % (self.board[0],self.board[1],self.board[2]))
        print("---+---+---")
        print(" %s | %s | %s " % (self.board[3],self.board[4],self.board[5]))
        print("---+---+---")
        print(" %s | %s | %s " % (self.board[6],self.board[7],self.board[8]))

    def assertIfMoveIsLegal(self, move):
        if not move: return False
        if not 0 < move < 10: return False
        if self.board[move-1] in self.palyersSigns: return False
        return True

    def getPlayerOfTurn(self):
        return (self.player2,self.player1)[self.turn == 1]

    def updateBoard(self,pos):
        p = self.getPlayerOfTurn()
        self.board[pos-1] = p.sign

    def nextTurn(self):
        self.turn = (1,2)[self.turn == 1]
    
    def showEndGameMessage(self, winner):
        if winner:
            p = self.getPlayerOfTurn()
            self.view()
            print("%s Wins!" % p.name)
        else:
            self.view()
            print("Draw!")

    def processLegalMove(self, movement):
        self.updateBoard(movement)
        win = self.winner()
        if win:
            self.showEndGameMessage(win)
            exit(0)

        self.nextTurn()

    def processIlegalMove(self, movement):
        print("ilegal move..try again")

    def play(self):
        while True:

            # assert if game has ended on previous loop
            endGame = self.endGame()
            if endGame:
                self.showEndGameMessage(False)
                exit(0)

            self.view()
            print("\nPlayer {}: ".format(self.turn))

            # wait for player input
            pl = self.getPlayerOfTurn()
            movement = pl.play(self.board)
            print("")

            # process move
            legalMove = self.assertIfMoveIsLegal(movement)
            if legalMove:
                self.processLegalMove(movement)
            else:
                self.processIlegalMove(movement)

P1 = human_player("P1", 'X')
P2 = rand_player('P2', "O")

game = tictactoe(player1=P1, player2=P2)
game.play() 