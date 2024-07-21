class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        for i, j in rowConditions:
            graph_row[i].append(j)
        for i, j in colConditions:
            graph_col[i].append(j)

        order_row = self.topologicalSort(graph_row, k)
        order_col = self.topologicalSort(graph_col, k)

        if not order_row or not order_col:
            return []

        indices_row = {val: key for key, val in enumerate(order_row)}
        indices_col = {val: key for key, val in enumerate(order_col)}

        result = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            result[indices_row[i]][indices_col[i]] = i
        
        return result

    def topologicalSort(self, graph, k):
        depths = {i: 0 for i in range(1, k + 1)}
        for i in graph:
            for j in graph[i]:
                depths[j] += 1
        nodes = deque([i for i in depths if depths[i] == 0])
        result = []
        while nodes:
            node = nodes.popleft()
            result.append(node)
            for i in graph[node]:
                depths[i] -= 1
                if depths[i] == 0:
                    nodes.append(i)
        return result if len(result) == k else []

