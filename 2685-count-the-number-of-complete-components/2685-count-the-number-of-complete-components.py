class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [False] * n
        answer = 0
        
        for node in range(n):
            if not visited[node]:
                cur_comp = []
                queue = deque([node])
                visited[node] = True

                while queue:
                    cur_node = queue.popleft()
                    cur_comp.append(cur_node)

                    for neighbor in adj[cur_node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                
                is_complete = True
                for cur_node in cur_comp:
                    if len(adj[cur_node]) != len(cur_comp):
                        is_complete = False
                        break
                
                if is_complete:
                    answer += 1
        
        return answer