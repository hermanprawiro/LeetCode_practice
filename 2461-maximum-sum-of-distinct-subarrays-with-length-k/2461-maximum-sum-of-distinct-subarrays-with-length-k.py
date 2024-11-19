class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        visited = {}
        answer = sums = 0
        for i in range(len(nums)):
            num = nums[i]
            if i >= k:
                visited[nums[i - k]] -= 1
                sums -= nums[i - k]
            if num in visited and visited[num] > 0:
                sums = 0
                visited[num] += 1
            else:
                sums += num
                visited[num] = 1
            if i >= k - 1:
                answer = max(answer, sums)
        return answer
