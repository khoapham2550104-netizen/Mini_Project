from collections import defaultdict
import numpy as np
class TickTacToe:
    
    symbol_number_encode = defaultdict(int)
    number_symbol_encode = defaultdict(str)
    def __init__(self, mark1 = 'X', mark2 = 'O'):
        self.grid = np.array([[0] * 3 for i in range(3)])
        
        self.symbol_number_encode[mark1] = -1
        self.number_symbol_encode[-1] = mark1
        self.symbol_number_encode[mark2] = 1
        self.number_symbol_encode[1] = mark2
        


        
    def mark(self, x, y, symbol):
        
        while True:
            if self.grid[x][y] != 0:
                print("You can't choose this !!! \n Please choose again")
            else:
                self.grid[x][y] = self.symbol_number_encode[symbol] # Convert symbol to numerical values
        return
    
    # TODO: implement these two
    
    def checkWinner(self):
        win = True
        
        # Check the horizontal
        for i in range(3):
            pre = self.grid[i][0]
            if pre == 0:
                continue
            win = True
            
            for j in range(1,3):
                if self.grid[i][j] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.symbol_number_encode[pre]}")
                return                    
            
        # Check the vertical 
        for i in range(3):
            pre = self.grid[0][i]
            if pre == 0:
                continue
            win = True

            for j in range(1,3):
                if self.grid[j][i] != pre:
                    win = False

            if win:
                print(f"The winner is: {self.symbol_number_encode[pre]}")
                return  
            
        # Check the diagonal
        pre = self.grid[0][0]
        if pre != 0:
            win = True
            for i in range(1, 3):
                if self.grid[i][i] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.symbol_number_encode[pre]}")
                return  
        
        # Check the diagonal 
        pre = self.grid[0][2]
        if pre != 0:
            win = True
            for i in range(1, 3):
                if self.grid[i][2 - i] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.symbol_number_encode[pre]}")
                return  
            

    
    
    def gameplay(self):
        pass
    
                
                    
            