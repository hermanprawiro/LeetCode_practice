class Solution:
    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        # bfs from 0 to (n-1), where the edges are unweighted (same cost)
        visited = [False] * n
        queue = deque()
        queue.append(0)
        visited[0] = True
        n_steps = 0
        while queue:
            n_current = len(queue)
            for _ in range(n_current):
                current = queue.popleft()
                if current == (n - 1):
                    return n_steps
                for neighbor in adj_list[current]:
                    if visited[neighbor]:
                        continue
                    queue.append(neighbor)
                    visited[neighbor] = True
            n_steps += 1
        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            adj_list[i].append(i + 1)
        answer = []
        for u, v in queries:
            adj_list[u].append(v)
            answer.append(self.bfs(n, adj_list))
        return answer
        