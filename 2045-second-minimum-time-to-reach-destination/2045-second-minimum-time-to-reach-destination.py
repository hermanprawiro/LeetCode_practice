class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        queue = []
        heapify(queue)
        heappush(queue, (0, 1)) # (time, node)

        visited = [0] * (n + 1)
        distance = [-1] * (n + 1)

        while queue:
            t, node = heappop(queue)
            if distance[node] == t or visited[node] >= 2:
                continue # skip
            visited[node] += 1
            distance[node] = t

            if node == n and visited[node] == 2:
                return distance[node]
            
            # waiting for green light
            if (t // change) % 2 != 0:
                t = (t // change + 1) * change
            
            for neighbor in graph[node]:
                heappush(queue, (t + time, neighbor))

        return -1
        