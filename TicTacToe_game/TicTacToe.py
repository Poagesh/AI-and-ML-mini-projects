import random

class tictactoe:
    def __init__(self):
        self.board=[[' ' for _ in range(3)] for _ in range(3)]
        self.currentwinner=None
    
    def printboard(self):
        for row in self.board:
            print('| ' + ' | '.join(row)+' |')
    
    @staticmethod
    def printboardnums():
        numberboard=[[str(i * 3 + j) for j in range(3)] for i in range(3)]
        for row in numberboard:
            print('| ' + ' | '.join(row) + ' |')
    
    def availablemoves(self):

        return [(r, c) for r,row in enumerate(self.board) for c, spot in enumerate(row) if spot ==' ']
    
    def emptysquares(self):
        return ' ' in [spot for row in self.board for spot in row]
    
    def numemptysquares(self):
        return len(self.available_moves())
    
    def makemove(self,square,letter):
        if self.board[square[0]][square[1]]==' ':
            self.board[square[0]][square[1]]=letter
            if self.winner(square,letter):
                self.currentwinner=letter
            return True
        return False
    
    def winner(self,square,letter):
        rowind, colind=square
        row=self.board[rowind]
        if all([s==letter for s in row]):
            return True
        
        col=[self.board[r][colind] for r in range(3)]
        if all([s==letter for s in col]):
            return True
        
        if rowind==colind:
            diagonal1=[self.board[i][i] for i in range(3)]
            if all([s==letter for s in diagonal1]):
                return True
        
        if rowind + colind==2:
            diagonal2 = [self.board[i][2-i] for i in range(3)]
            if all([s==letter for s in diagonal2]):
                return True
        
        return False

def minimax(state,depth,alpha,beta,maximizingplayer):
    maxplayer='O' 
    otherplayer='X' if maxplayer=='O' else 'O'

    if state.currentwinner==otherplayer:
        return {'position':None,'score':1*(depth+1) if otherplayer==maxplayer else-1*(depth+1)}
    
    elif not state.emptysquares():
        return {'position':None,'score':0}
    
    if maximizingplayer:
        best = {'position':None,'score':-float('inf')}
    else:
        best = {'position':None,'score':float('inf')}
    
    for possiblemove in state.availablemoves():
        state.makemove(possiblemove,maxplayer if maximizingplayer else otherplayer)
        simscore = minimax(state,depth+1,alpha,beta,not maximizingplayer)
        
        state.board[possiblemove[0]][possiblemove[1]]=' '
        state.currentwinner=None
        simscore['position']=possiblemove
        
        if maximizingplayer:
            if simscore['score']>best['score']:
                best=simscore
            alpha=max(alpha,simscore['score'])
        else:
            if simscore['score']<best['score']:
                best=simscore
            beta=min(beta,simscore['score'])
        
        if beta<=alpha:
            break
    
    return best

def play(game,xplayer,oplayer,printgame=True):
    if printgame:
        game.printboardnums()
    
    letter='O'
    aifirstmove=True
    
    while game.emptysquares():
        if letter=='O':
            if aifirstmove:
                square=oplayer.getfirstmove(game)
                aifirstmove=False
            else:
                square=oplayer.getmove(game)
        else:
            square=xplayer.getmove(game)
        
        if game.makemove(square, letter):
            if printgame:
                print(letter+f' makes a move to square {square[0]*3+square[1]}')
                game.printboard()
                print('')
            
            if game.currentwinner:
                if printgame:
                    print(letter+' wins!')
                return letter
            
            letter = 'O' if letter=='X' else 'X'
    
    if printgame:
        print('It\'s a tie!')

class HumanPlayer:
    def __init__(self, letter):
        self.letter=letter
    
    def getmove(self, game):
        validsquare=False
        val=None
        while not validsquare:
            square=input(self.letter+'\'s turn. Input move (0-8): ')
            try:
                val=int(square)
                if val not in range(9):
                    raise ValueError
                row,col=val//3,val%3
                if game.board[row][col]!=' ':
                    raise ValueError
                validsquare=True
            except ValueError:
                print('Invalid square. Try again.')
        
        return row,col

class AIPlayer:
    def __init__(self,letter):
        self.letter=letter
    
    def getfirstmove(self,game):
        available=game.availablemoves()
        return random.choice(available)  

    def getmove(self,game):
        if len(game.availablemoves())==9:
            square=random.choice(game.availablemoves())
        else:
            square=minimax(game,0,-float('inf'),float('inf'),True)['position']
        return square


xplayer=HumanPlayer('X')
oplayer=AIPlayer('O')
t=tictactoe()
play(t,xplayer,oplayer,printgame=True)
