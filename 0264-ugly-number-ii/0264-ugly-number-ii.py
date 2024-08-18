class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_heap = [1]
        visited = set([1])
        primes = [2, 3, 5]
        current = 0
        for _ in range(n):
            current = heappop(ugly_heap)
            for prime in primes:
                new_ugly = current * prime
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heappush(ugly_heap, new_ugly)
        return current