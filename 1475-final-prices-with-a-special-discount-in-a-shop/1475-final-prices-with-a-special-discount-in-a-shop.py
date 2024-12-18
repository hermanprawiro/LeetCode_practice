class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy() # init with undiscounted prices
        stack = deque()
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                # can apply discount to the previous prices
                answer[stack.pop()] -= price
            stack.append(i)
        return answer
