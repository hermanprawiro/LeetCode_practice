class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        # attach smaller to the larger
        if self.size[root_a] < self.size[root_b]:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]


class Solution:
    DIRECTIONS = [ # [row, col]
        [0, 1], # right
        [1, 0], # down
        [0, -1], # left
        [-1, 0] # up
    ]
    def largestIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ds = DisjointSet(row * col)

        # map all lands
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: # is land
                    idx = i * col + j # flat index
                    for (di, dj) in self.DIRECTIONS:
                        ni = i + di
                        nj = j + dj
                        # check validity and is land
                        if (0 <= ni < row) and (0 <= nj < col) and (grid[ni][nj] == 1):
                            nidx = ni * col + nj # neighbor's flat index
                            ds.union(idx, nidx)
        
        # find the largest land size
        # if there are no '0' (no sea), then the entire grid is land, hence answer is row*col
        # for each sea node, check the root of its neighbors, for each distinct root, sum the size, then keep the max
        answer = 0
        has_zero = False
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0: # is sea
                    has_zero = True
                    roots = set()
                    cur_size = 1
                    for (di, dj) in self.DIRECTIONS:
                        ni = i + di
                        nj = j + dj
                        # check validity and is land
                        if (0 <= ni < row) and (0 <= nj < col) and (grid[ni][nj] == 1):
                            nidx = ni * col + nj # neighbor's flat index
                            roots.add(ds.find(nidx))
                        
                    for nidx in roots:
                        cur_size += ds.size[nidx]
                    
                    answer = max(answer, cur_size)
        
        # if not has_zero:
        #     return row * col
        return answer