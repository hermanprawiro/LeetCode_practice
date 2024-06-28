class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # city is 0-indexed, so we can use array to store city's connections
        # no need for dict (hash)
        connections = [0] * n

        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1

        # sort by num of connection, descending so use -
        cities = list(range(n))
        cities.sort(key=lambda x: -degree[x])

        result = 0
        for i in range(n):
            result += (n - i) * connections[cities[i]]

        return result
        