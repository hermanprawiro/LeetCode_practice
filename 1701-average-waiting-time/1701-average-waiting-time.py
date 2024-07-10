class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        total_wait = 0
        for arrival, req_time in customers:
            if current < arrival:
                current = arrival
            wait = current + req_time - arrival
            total_wait += wait
            current += req_time
        return total_wait / len(customers)