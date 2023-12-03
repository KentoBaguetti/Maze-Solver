class Maze:
    
    def __init__(self):
        self.maze_board = None
        self.visited = set()
    
    def display_maze(self):
        for row in self.maze_board:
            print(row)
            
    def maze_10x10(self):
        self.maze_board = [
            ["#","#","S","#","#","#","#","#","#","#"],
            ["#","#",".","#",".",".",".",".",".","#"],
            ["#","#",".","#",".","#","#","#",".","#"],
            ["#","#",".","#",".","#",".","#",".","#"],
            ["#","#",".",".",".","#",".","#",".","#"],
            ["#","#","#","#",".",".",".",".",".","#"],
            ["#","#",".",".",".","#","#","#","#","#"],
            ["#",".",".","#","#",".",".",".",".","#"],
            ["#","#",".",".",".",".","#","#",".","#"],
            ["#","#","#","#","#","#","#","#","E","#"]
        ]
        
    def dfs(self, cell):
        # first check
        if cell not in self.visited:
            print(cell)
            self.visited.add(cell)
            
            # recursion
            if self.maze_board[cell[0]][cell[1]] == "E":
                exit()
            if self.maze_board[cell[0]][cell[1]+1] == "." and cell[1]+1 < 10:
                self.dfs((cell[0], cell[1]+1))
            if self.maze_board[cell[0]][cell[1]-1] == "." and cell[1]-1 >= 0:
                self.dfs((cell[0], cell[1]-1))
            if self.maze_board[cell[0]+1][cell[1]] == "." and cell[0]+1 < 10:
                self.dfs((cell[0]+1, cell[1]))
            if self.maze_board[cell[0]-1][cell[1]] == "." and cell[0]-1 >= 0:
                self.dfs((cell[0]-1, cell[1]))
        

if __name__ == "__main__":
    game = Maze()
    game.maze_10x10()
    game.display_maze()
    start = (0, 2)
    game.dfs(start)
