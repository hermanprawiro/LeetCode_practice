class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0] * len(nums) # to count the num of violating nums up to i position
        answer = [False] * len(queries)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1]
            if nums[i - 1] % 2 == nums[i] % 2: # both has same parity
                prefix[i] += 1
        
        for i in range(len(queries)):
            start, end = queries[i]
            if prefix[end] - prefix[start] == 0:
                answer[i] = True
        return answer

        