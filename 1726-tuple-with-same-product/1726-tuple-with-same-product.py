class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        First, find out the frequency of product.
        If the frequency is >= 2, there are at least 1 tuple (combination of 2 pairs).
        One product occurence is formed by a distinct pair.
        If the freq = 2, n_tuple = 1. If the freq = 3, n_tuple = 2. If the freq = 4, n_tuple = 6.
        For example, when freq = 4, there are 4 distinct pairs (pair a, b, c, d).
        We can form 6 tuples as (a, b), (a, c), (a, d), (b, c), (b, d), (c, d).
        Each tuple has 8 permutations.
        """
        freq = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if prod in freq:
                    freq[prod] += 1
                else:
                    freq[prod] = 1

        n_tuple = 0
        for prod, count in freq.items():
            n_tuple += (count - 1) * count // 2
        return n_tuple * 8