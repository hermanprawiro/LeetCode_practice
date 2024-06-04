class Solution:
    def fib(self, N: int) -> int:
        return self.fib_helper(N, {})
        
    def fib_helper(self, N: int, memo) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N in memo:
            return memo[N]
        else:
            return self.fib_helper(N - 1, memo) + self.fib_helper(N - 2, memo)