from collections import deque, defaultdict
import heapq
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


class Maze:
    def __init__(self):
        # self.maze = [
        #     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        #     ["#", "S", "0", "0", "#", "0", "0", "0", "0", "#"],
        #     ["#", "0", "#", "0", "#", "0", "#", "#", "0", "#"],
        #     ["#", "0", "#", "0", "0", "0", "0", "#", "0", "#"],
        #     ["#", "0", "#", "#", "#", "0", "#", "#", "0", "#"],
        #     ["#", "0", "0", "0", "#", "0", "#", "0", "0", "#"],
        #     ["#", "#", "#", "0", "#", "0", "#", "0", "#", "#"],
        #     ["#", "0", "0", "0", "0", "0", "0", "0", "#", "#"],
        #     ["#", "0", "#", "#", "#", "#", "#", "0", "0", "E"],
        #     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        # ]

        # self.start = (1, 1)
        # self.end = (8, 9)

        # self.maze = [
        #     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        #     ["#", "S", "0", "#", "#", "0", "0", "0", "0", "#"],
        #     ["#", "0", "0", "0", "#", "0", "#", "#", "0", "#"],
        #     ["#", "0", "#", "0", "0", "0", "0", "#", "0", "#"],
        #     ["#", "0", "#", "#", "#", "#", "#", "#", "0", "#"],
        #     ["#", "0", "0", "0", "#", "0", "#", "0", "0", "#"],
        #     ["#", "#", "#", "0", "#", "0", "#", "0", "#", "#"],
        #     ["#", "0", "0", "0", "0", "0", "0", "0", "#", "#"],
        #     ["#", "0", "#", "#", "#", "#", "#", "0", "0", "E"],
        #     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        # ]

        # self.start = (1, 1)
        # self.end = (8, 9)

        self.maze = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "S", "0", "0", "0", "#", "0", "0", "0", "0", "0", "0", "0", "0", "#"],
            ["#", "0", "#", "#", "0", "#", "0", "#", "#", "#", "#", "#", "#", "0", "#"],
            ["#", "0", "#", "0", "0", "0", "0", "0", "#", "0", "#", "0", "0", "0", "#"],
            ["#", "0", "#", "#", "#", "#", "#", "0", "#", "0", "#", "0", "#", "0", "#"],
            ["#", "0", "#", "0", "0", "0", "#", "0", "#", "0", "0", "0", "#", "0", "#"],
            ["#", "0", "#", "0", "#", "0", "#", "0", "0", "0", "#", "0", "#", "0", "#"],
            ["#", "0", "#", "0", "#", "0", "0", "0", "#", "0", "0", "0", "#", "0", "#"],
            ["#", "0", "#", "0", "#", "#", "#", "#", "#", "0", "#", "#", "#", "0", "#"],
            ["#", "0", "#", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "#"],
            ["#", "0", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "0", "#"],
            ["#", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "E", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ]

        self.start = (1, 1)
        self.end = (11, 13)

    def bfs(self):
        rows, cols = len(self.maze), len(self.maze[0])

        queue = deque([self.start])
        visited = []  # would normally use a set for better a better time complexity but for the animation to look smooth, an array is used instead

        # hashmap to hold the child-parent relations of each node | Each child (Node) points to its parent (Node)
        parent = {self.start: None}

        while queue:
            curr = queue.popleft()
            visited.append(curr)

            # The loop terminates once the end node is reached
            if curr == self.end:
                break

            row, col = curr

            # The different directions you can view as potential candidates
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                r, c = dr + row, dc + col
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and self.maze[r][c] in ["0", "E"]
                    and (r, c) not in visited
                ):
                    queue.append((r, c))
                    parent[(r, c)] = (row, col)

        # Starting from the end node, find the path from the end to the start node
        path = deque()
        if self.end in parent:
            step = self.end
            path.appendleft(step)
            while step:
                path.appendleft(parent[step])
                step = parent[step]

        return path, visited

    # def breadthFirstSearch(self):
    #     rows, cols = len(self.maze), len(self.maze[0])

    #     queue = deque()
    #     visited = set()

    #     queue.append(self.start)

    #     parent_path = {self.start: None}

    #     while queue:
    #         curr_row, curr_col = queue.popleft()
    #         visited.add((curr_row, curr_col))

    #         if (curr_row, curr_col) == self.end:
    #             break

    #         directions = [
    #             (curr_row + 1, curr_col),
    #             (curr_row - 1, curr_col),
    #             (curr_row, curr_col + 1),
    #             (curr_row, curr_col - 1),
    #         ]

    #         for dir in directions:
    #             row_dir, col_dir = dir
    #             if (
    #                 0 <= row_dir < rows
    #                 and 0 <= col_dir < cols
    #                 and dir not in visited
    #                 and self.maze[row_dir][col_dir] in ["0", "E"]
    #             ):
    #                 queue.append(dir)
    #                 parent_path[(row_dir, col_dir)] = (curr_row, curr_col)

    #     path = deque()

    #     if self.end in parent_path:
    #         curr = self.end
    #         path.appendleft(curr)
    #         while curr:
    #             path.appendleft(parent_path[curr])
    #             curr = parent_path[curr]

    #     return path, visited

    def backtrack(self):
        rows, cols = len(self.maze), len(self.maze[0])
        res = deque()
        visited = []
        # visited = set()

        def find_path(row, col, path, visited):
            if (row, col) == self.end:
                return True

            visited.append((row, col))
            # visited.add((row, col))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and (r, c) not in visited
                    and self.maze[r][c] in ["0", "E"]
                ):
                    if find_path(r, c, path, visited):
                        path.appendleft((r, c))
                        return True

            visited.pop()
            return False

        find_path(self.start[0], self.start[1], res, visited)
        return list(res), visited

    def new_backtrack(self):
        rows, cols = len(self.maze), len(self.maze[0])

    def dijkstra(self):
        rows, cols = len(self.maze), len(self.maze[0])

        # Priority queue
        pq = [(0, self.start)]
        heapq.heapify(pq)

        distance = {self.start: 0}

        parent = {self.start: None}

        while pq:
            dist, curr = heapq.heappop(pq)

            if curr == self.end:
                break

            row, col = curr

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and self.maze[r][c] in ["0", "E"]:
                    new_dist = dist + 1
                    if (r, c) not in distance or new_dist < distance[(r, c)]:
                        distance[(r, c)] = new_dist
                        parent[(r, c)] = curr
                        heapq.heappush(pq, (new_dist, (r, c)))

        path = deque()
        step = self.end
        while step is not None:
            path.appendleft(step)
            step = parent[step]

        return list(path), distance

    def draw_maze(self):
        fig, ax = plt.subplots()
        rows, cols = len(self.maze), len(self.maze[0])
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.invert_yaxis()

        for row in range(rows):
            for col in range(cols):
                if self.maze[row][col] == "#":
                    ax.add_patch(patches.Rectangle((col, row), 1, 1, color="black"))
                elif self.maze[row][col] == "S":
                    ax.add_patch(patches.Rectangle((col, row), 1, 1, color="green"))
                elif self.maze[row][col] == "E":
                    ax.add_patch(patches.Rectangle((col, row), 1, 1, color="red"))

        return fig, ax

    def animate_bfs(self):
        path, visited = self.bfs()
        fig, ax = self.draw_maze()

        def update(frame):
            row, col = frame
            ax.add_patch(patches.Rectangle((col, row), 1, 1, color="blue"))

        anime = FuncAnimation(fig, update, frames=list(visited), repeat=False)
        plt.show()

    def animate_backtrack(self):
        backtracking_path, backtracking_visited = self.backtrack()
        fig, ax = self.draw_maze()

        def update(frame):
            row, col = frame
            #  backtracking path in yellow
            ax.add_patch(patches.Rectangle((col, row), 1, 1, color="yellow"))

        anim = FuncAnimation(fig, update, frames=backtracking_visited, repeat=False)
        plt.show()

    def animate_dijkstra(self):
        path, distances = self.dijkstra()
        fig, ax = self.draw_maze()

        def update(frame):
            row, col = frame
            ax.add_patch(patches.Rectangle((col, row), 1, 1, color="blue"))

        anime = FuncAnimation(fig, update, frames=path, repeat=False)
        plt.show()


if __name__ == "__main__":
    testMaze = Maze()
    # testMaze.animate_dijkstra()
    testMaze.animate_backtrack()
    # print(testMaze.backtrack()[0])
    # print(testMaze.bfs()[0])
