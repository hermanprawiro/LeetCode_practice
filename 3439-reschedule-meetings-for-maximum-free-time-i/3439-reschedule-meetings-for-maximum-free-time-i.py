class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime) # num of events
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + endTime[i] - startTime[i]
        
        answer = 0
        for i in range(k - 1, n):
            # boundary of free time
            left = 0 if i == (k - 1) else endTime[i - k]
            right = eventTime if i == (n - 1) else startTime[i + 1]

            # free time minus adjacent meeting times
            answer = max(answer, right - left - (presum[i + 1] - presum[i - k + 1]))
        
        return answer