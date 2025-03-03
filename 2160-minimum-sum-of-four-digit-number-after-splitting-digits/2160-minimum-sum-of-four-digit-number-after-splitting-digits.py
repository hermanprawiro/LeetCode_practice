class Solution:
    def minimumSum(self, num: int) -> int:
        sort = sorted([int(i) for i in str(num)])
        return 10 * (sort[0] + sort[1]) + (sort[2] + sort[3])