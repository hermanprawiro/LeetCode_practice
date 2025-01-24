class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Terminal nodes (0 indegree) are safe nodes. 
        The nodes that only leads to terminal nodes (1 indegree) are also safe nodes.
        So we reverse the graph and start traversing from terminal nodes.
        """
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i) # reverse
                indegree[i] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        is_safe = [False] * n
        while queue:
            i = queue.popleft()
            is_safe[i] = True
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        
        answer = [i for i in range(n) if is_safe[i]]
        return answer