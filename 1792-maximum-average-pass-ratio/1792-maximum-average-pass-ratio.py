class Solution:
    def calcGain(self, n_pass, n):
        return ((n_pass + 1) / (n + 1)) - (n_pass / n)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        queue = [] # max heap, dont forget to turn the value to negative
        for n_pass, n in classes:
            heapq.heappush(queue, (-self.calcGain(n_pass, n), n_pass, n))
        # choose the class that maximize the gain
        for i in range(extraStudents):
            _, n_pass, n = heapq.heappop(queue)
            n_pass += 1
            n += 1
            heapq.heappush(queue, (-self.calcGain(n_pass, n), n_pass, n))
        # calculate ratio after adding extra students
        answer = 0
        while queue:
            _, n_pass, n = heapq.heappop(queue)
            answer += n_pass / n
        return answer / len(classes)