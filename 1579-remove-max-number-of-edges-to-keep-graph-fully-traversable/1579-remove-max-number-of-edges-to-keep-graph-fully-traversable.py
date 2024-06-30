class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # define unionfind data structure
        class UnionFind:
            def __init__(self, n: int):
                self.representative = list(range(n + 1))
                self.components = n
                self.component_size = [1] * (n + 1)

            def find(self, x: int):
                if self.representative[x] == x:
                    return x
                self.representative[x] = self.find(self.representative[x])
                return self.representative[x]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)

                if x == y:
                    return 0
                
                if self.component_size[x] > self.component_size[y]:
                    self.component_size[x] += self.component_size[y]
                    self.representative[y] = x
                else:
                    self.component_size[y] += self.component_size[x]
                    self.representative[x] = y
                
                self.components -= 1
                return 1
            
            def is_connected(self):
                return self.components == 1

        alice = UnionFind(n)
        bob = UnionFind(n)
        edges_required = 0

        for edge in edges:
            if edge[0] == 3:
                edges_required += (alice.union(edge[1], edge[2]) | bob.union(edge[1], edge[2]))
        
        for edge in edges:
            if edge[0] == 2:
                edges_required += bob.union(edge[1], edge[2])
            elif edge[0] == 1:
                edges_required += alice.union(edge[1], edge[2])

        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required

        return -1