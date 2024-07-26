class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # build the graph (adjacency list)
        alist = [[] for _ in range(n)]
        for n1, n2, dist in edges:
            alist[n1].append((n2, dist))
            alist[n2].append((n1, dist))

        def getNumOfNeighbors(source: int) -> int:
            visited = set()
            queue = [(0, source)]
            heapify(queue)

            while queue:
                dist_to_current, current = heappop(queue)
                if current not in visited:
                    visited.add(current)
                    for node, dist in alist[current]:
                        total_dist = dist_to_current + dist
                        if total_dist <= distanceThreshold:
                            heappush(queue, (total_dist, node))
            return len(visited) - 1 # exclude itself


        current_min = n
        result = 0

        for node in range(n):
            n_neighbors = getNumOfNeighbors(node)
            if n_neighbors <= current_min:
                current_min = n_neighbors
                result = node

        return result
