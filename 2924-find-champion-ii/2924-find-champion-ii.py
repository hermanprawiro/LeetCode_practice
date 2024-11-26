class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        edges_to = [0] * n
        for u, v in edges:
            edges_to[v] += 1
        answer = -1
        for i in range(n):
            if edges_to[i] == 0:
                if answer == -1:
                    answer = i
                else:
                    return -1
        return answer