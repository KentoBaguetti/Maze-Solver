from maze_solver import Maze

if __name__ == "__main__":
    maze = Maze()
    
    # The visualizations of each algorithm
    maze.animate_backtrack()
    maze.animate_bfs()
    
    # The paths printed via a list
    backtracking_path = maze.backtrack()[0]
    bfs_paths = maze.bfs()[0]
    print(backtracking_path)
    print(bfs_paths)
    