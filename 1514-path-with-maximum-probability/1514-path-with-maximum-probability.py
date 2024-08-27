class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # using Shortest Path Faster Algorithm (SPFA), an improvement to Bellman Ford
        # hashmap to represent the graph {u: [(v, dist)], v: [(u, dist)]}
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        max_probs = [0.] * n
        max_probs[start_node] = 1.

        queue = deque([start_node])
        while queue:
            cur = queue.popleft()
            for (neighbor, prob) in graph[cur]:
                # only if current path increases prob of reaching neighbor
                if max_probs[cur] * prob > max_probs[neighbor]:
                    max_probs[neighbor] = max_probs[cur] * prob
                    queue.append(neighbor)
        
        return max_probs[end_node]