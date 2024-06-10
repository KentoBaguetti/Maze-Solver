from collections import deque


class Maze:
    
    def __init__(self):
   
        self.maze = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "S", "0", "0", "#", "0", "0", "0", "0", "#"],
            ["#", "0", "#", "0", "#", "0", "#", "#", "0", "#"],
            ["#", "0", "#", "0", "0", "0", "0", "#", "0", "#"],
            ["#", "0", "#", "#", "#", "0", "#", "#", "0", "#"],
            ["#", "0", "0", "0", "#", "0", "#", "0", "0", "#"],
            ["#", "#", "#", "0", "#", "0", "#", "0", "#", "#"],
            ["#", "0", "0", "0", "0", "0", "0", "0", "#", "#"],
            ["#", "0", "#", "#", "#", "#", "#", "0", "0", "E"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]

        self.start = (1, 1)
        self.end = (8, 9)

    def bfs(self):
        rows, cols = len(self.maze), len(self.maze[0])
        
        queue = deque([self.start])
        visited = set()
        
        # hashmap to hold the child-parent relations of each node | Each child (Node) points to its parent (Node)
        parent = {self.start: None}
        
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            
            # The loop terminates once the end node is reached
            if curr == self.end: 
                break

            row, col = curr

            # The different directions you can view as potential candidates
            directions = [(0,1), (1,0), (0,-1), (-1,0)] 
            
            for dr, dc in directions:
                r, c = dr + row, dc + col
                if 0 <= r < rows and 0 <= c < cols and self.maze[r][c] in ["0", "E"] and (r, c) not in visited:
                    queue.append((r, c))
                    parent[(r, c)] = (row, col)
        
        path = deque()
        if self.end in parent:
            step = self.end
            path.appendleft(step)
            while step:
                path.appendleft(parent[step])
                step = parent[step]
        
        return path
    
    def backtrack(self):
        pass
                    

if __name__ == "__main__":
    testMaze = Maze()
    path = testMaze.bfs()
    print(path)