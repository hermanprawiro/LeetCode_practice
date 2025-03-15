class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        min_r = 0
        max_r = max(candies)

        while min_r < max_r:
            mid_r = (max_r - min_r + 1) // 2 + min_r

            max_child = 0
            for candy in candies:
                max_child += candy // mid_r
            
            if max_child >= k:
                min_r = mid_r
            else:
                max_r = mid_r - 1
        
        return min_r