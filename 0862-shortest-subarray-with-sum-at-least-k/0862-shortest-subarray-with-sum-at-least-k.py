class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1) # prefix_sum[i] = sum[0:i]
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        answer = float("inf")
        # maintain an ascending deque for index, where 
        # prefix_sum[queue[-1]] < current prefix_sum
        queue = deque()
        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                # (queue[0], i]
                answer = min(answer, i - queue.popleft())
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()
            queue.append(i)
        return answer if answer != float("inf") else -1
            