import sys

class Board():
    def __init__(self, input_string):
        self.boardInitFromString(input_string)
        
    # won't tolerate extra newlines at the end of the input.
    def boardInitFromString(self, input):
        self.board = []
        self.numbers = {}
        x = 0
        for row in input.split("\n"):
            _row = []
            y = 0
            for col in row.split():
                col = int(col)
                _row.append({ 'number' : col, 'played' : False })
                self.numbers[col] = [x,y]
                y += 1
            x += 1
            self.board.append(_row)
            
        self.dim_x = len(_row)
        self.dim_y = len(self.board)
        
    def print(self):
        for row in self.board:
            for col in row:
                if col['played']:
                    sys.stdout.write("*{: <2}* ".format(col['number']))
                else:
                    sys.stdout.write(" {: <2}  ".format(col['number']))
            sys.stdout.write("\n")
        sys.stdout.write("\n")
                    
        
    def play(self, number):
        # track the last played number
        self.lastplayed = number
        
        # add it to the board if we have it
        try:
            x,y = self.numbers[number]
        except KeyError:
            return
        self.board[x][y]['played'] = True
        
    def didIWin(self):
        # row win
        for row in self.board:
            count = 0
            for col in row:
                if col['played'] == True:
                    count += 1
            if count == self.dim_x:
                print("Winner! (row)")
                return(True)
        # col win
        for col in range(0,self.dim_y):
            count = 0
            for row in self.board:
                if row[col]['played'] == True:
                    count += 1
            if count == self.dim_y:
                print("Winner! (column)")
                return(True)
        
        # fallthrough
        return(False)
        
    def score(self):    
        score = 0
        for row in self.board:
            for col in row:
                if col['played'] == False:
                    score += col['number']
        score *= self.lastplayed
        
        return(score)
