class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in sorted(timePoints):
            times.append(int(timePoint[:2]) * 60 + int(timePoint[3:]))
        
        answer = times[0] - times[-1] + 24 * 60
        for i in range(len(times) - 1):
            answer = min(answer, times[i + 1] - times[i])
        return answer