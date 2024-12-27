class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        The score component can be divided into two parts, the left (i) part and the right (j) part.
        As all the left parts is positive and maximizes the final score, we can store the max we seen so far.
        """
        max_left = values[0]
        answer = 0
        for j in range(1, len(values)):
            score = max_left + values[j] - j
            answer = max(answer, score)
            max_left = max(max_left, values[j] + j)
        return answer