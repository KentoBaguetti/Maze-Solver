from maze_solver import Maze

if __name__ == "__main__":
    maze = Maze()

    print("1. BFS\n2.Backtracking\n3. Dijkstras Algorihtm")
    user_choice = input(
        "Enter what algorithm you want to view (1, 2, or 3) or any other key to exit: "
    )

    if user_choice == "1":
        maze.animate_bfs()
    elif user_choice == "2":
        maze.animate_backtrack()
    elif user_choice == "3":
        maze.animate_dijkstra()
    else:
        print("Bye bye!")
