class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # treat as graph
        # every connected stone form a cluster
        # for each cluster, we can remove all stones except 1
        # so answer = total_stones - n_cluster
        n = len(stones)
        graph = [[] for _ in range(n)] # adjacency list
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        n_cluster = 0
        visited = [False] * n

        def dfs(stone):
            visited[stone] = True
            for neighbor in graph[stone]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                n_cluster += 1

        return n - n_cluster