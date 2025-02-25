class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        prefix_sum = 0
        n_odd = 0
        n_even = 1 # initial prefix_sum is even (0)

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                answer += n_odd
                n_even += 1
            else:
                answer += n_even
                n_odd += 1
            answer %= (10**9 + 7)

        return answer