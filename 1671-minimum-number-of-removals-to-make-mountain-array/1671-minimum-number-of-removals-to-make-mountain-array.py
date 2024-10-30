class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        answer = n
        n_lis = [1] * n # increasing
        n_lds = [1] * n # decreasing
        # find LIS, left to right
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    n_lis[i] = max(n_lis[i], 1 + n_lis[j])
        # find LDS, right to left
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    n_lds[i] = max(n_lds[i], 1 + n_lds[j])
        # calculate removal
        for i in range(n):
            if n_lis[i] > 1 and n_lds[i] > 1:
                answer = min(answer, n - n_lis[i] - n_lds[i] + 1)
        print(n_lis, n_lds)
        return answer