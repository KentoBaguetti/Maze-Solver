from maze_solver import Maze

if __name__ == "__main__":
    maze = Maze()
    
    print("1. BFS (No visualization)\n2. Backtracking (No visualization)\n 3. BFS (Visualization)\n4. Backtracking (Visualization)")
    user_choice = input("Enter what algorithm you want to view (1, 2, 3, or 4) or any other key to exit:")
    
    if user_choice == "1":
        print(maze.bfs()[0])
    elif user_choice == "2":
        print(maze.backtrack()[0])
    elif user_choice == "3":
        maze.animate_bfs()
    elif user_choice == "4":
        maze.animate_backtrack()
    else:
        print("Bye bye!")
    
    
    