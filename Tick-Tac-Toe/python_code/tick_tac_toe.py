import math
import random as rd
class TickTacToe:
    
    grid = [[0] * 3 for i in range(3)]
    int_to_mark = {1 : "X", -1 : "O", 0 : "_" }
    winner = 0  
    visited = set()
    def __init__(self):
        pass
    
    def putX(self, x, y):
        self.grid[x][y] = 1

    def putO(self, x, y):
        self.grid[x][y] = -1
    
    
    def printGrid(self):
        for line in self.grid:
            print ("| ", end= "")
            for square in line:
                print( self.int_to_mark(square), end = " | ")
            print()
         
    # TODO : Stop the program when there is a winner
    # TODO : If the grid is filled, restart the game with another player is starter
    
    def checkCondition(self):
        # Check all the win condition
        
        # Check all horizontal line
        for i in range(3):
            sum_score = 0
            for j in range(1,3):
                sum_score += self.grid[i][j]
            if sum_score == -3:
                winner = -1
                break
            elif sum_score == 3:
                winner = 1
                break
                    
        # Check all vertical line
        for i in range(3):
            sum_score = 0
            for j in range(1,3):
                sum_score += self.grid[j][i]
            if sum_score == -3:
                winner = -1
                break
            elif sum_score == 3:
                winner = 1
                break
        
        # Check all diagonal line
        sum_score = 0
        for i in range(3):
            sum_score += self.grid[i][i]
        if sum_score == -3:
            winner = -1
        elif sum_score == 3:
            winner = 1
        
        sum_score = 0
        for i in range(3):
            sum_score += self.grid[2 - i][i]
        if sum_score == -3:
            winner = -1
        elif sum_score == 3:
            winner = 1
            
            

        
                    
def main():
    game = TickTacToe()
    game.printGrid()




if __name__ == "__main__":
    main()
    