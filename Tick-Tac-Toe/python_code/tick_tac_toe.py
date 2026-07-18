class TickTacToe:
    
    grid = [["_"] * 3 for i in range(3)]
    def __init__(self):
        pass
    
    def putX(self, x, y):
        self.grid[x][y] = "X"

    def putO(self, x, y):
        self.grid[x][y] = "O"
        
    def printGrid(self):
        for line in self.grid:
            print ("| ", end= "")
            for square in line:
                print(square, end = " | ")
            print()
                      
                    
def main():
    game = TickTacToe()
    game.printGrid()




if __name__ == "__main__":
    main()
    