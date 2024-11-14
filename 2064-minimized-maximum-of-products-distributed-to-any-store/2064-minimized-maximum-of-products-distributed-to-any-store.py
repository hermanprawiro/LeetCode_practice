class Solution:
    def canDistribute(self, quantities: List[int], n: int, target: int) -> bool:
        # suppose max quantity for each product and each store is target
        # if we divide the product qty by target and ceil it, we get num of stores
        # if the total stores is <= n, we can distribute within target condition
        n_stores = sum([math.ceil(q / target) for q in quantities])
        return n_stores <= n

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        while left < right:
            mid = left + (right - left) // 2
            if self.canDistribute(quantities, n, mid):
                right = mid
            else:
                left = mid + 1
        return left