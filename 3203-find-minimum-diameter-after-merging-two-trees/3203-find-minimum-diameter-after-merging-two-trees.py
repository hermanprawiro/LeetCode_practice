class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        The answer is the max of these:
        1. The diameter of tree 1
        2. The diameter of tree 2
        3. The ceil(diameter_1 / 2) + ceil(diameter_2 / 2) + 1
        The third point is due to the most optimal merging is to select the middle node from each tree,
        resulting in the half diameter of each tree and +1 due to the additional edge connecting both trees.
        
        The hard part boils down to how to calculate the diameter of the tree. Using BFS, DFS, or topological sort?
        """
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = self.buildAdjList(n, edges1)
        adj2 = self.buildAdjList(m, edges2)

        diameter1 = self.calcDiameter(n, adj1)
        diameter2 = self.calcDiameter(m, adj2)
        merged = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, merged)

    def buildAdjList(self, size: int, edges: List[List[int]]) -> None:
        adj = [[] for _ in range(size)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        return adj

    def calcDiameter(self, size: int, adj: List[List[int]]) -> int:
        """
        Diameter endpoints must be leaves. By removing all leaves reduces the diameter by two.
        Repeat this process n times until there are only 1 or 2 nodes left.
        If 1 node left, the diameter is 2n.
        If 2 nodes left, the diameter is 2n + 1.
        """
        queue = deque()
        degrees = [0] * size
        for node, neighbor in enumerate(adj):
            degrees[node] = len(neighbor)
            if degrees[node] == 1:
                queue.append(node)
        
        n_remain = size
        n = 0
        while n_remain > 2:
            n_queue = len(queue)
            n_remain -= n_queue
            n += 1
            for _ in range(n_queue):
                cur = queue.popleft()
                for neighbor in adj[cur]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        if n_remain == 2:
            return 2 * n + 1
        return 2 * n
        