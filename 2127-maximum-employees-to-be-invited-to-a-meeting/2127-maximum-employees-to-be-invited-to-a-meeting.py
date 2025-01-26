class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        depth = [1] * n
        for i in favorite:
            indegree[i] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            fav = favorite[cur]
            depth[fav] = max(depth[fav], depth[cur] + 1)
            indegree[fav] -= 1
            if indegree[fav] == 0:
                queue.append(fav)
        
        cycle_max = 0
        cycle_two = 0
        for i in range(n):
            if indegree[i] == 0:
                continue
            cycle_size = 0
            cur = i
            while indegree[cur] != 0:
                indegree[cur] = 0
                cycle_size += 1
                cur = favorite[cur]
            
            if cycle_size == 2:
                cycle_two += depth[i] + depth[favorite[i]]
            else:
                cycle_max = max(cycle_max, cycle_size)
        return max(cycle_max, cycle_two)