class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))
        
        answer = ""
        while heap:
            count, char = heapq.heappop(heap)
            if len(answer) >= 2 and answer[-1] == char and answer[-2] == char:
                if not heap:
                    break
                temp_count, temp_char = heapq.heappop(heap)
                answer += temp_char
                temp_count += 1
                if temp_count < 0:
                    heapq.heappush(heap, (temp_count, temp_char))
                heapq.heappush(heap, (count, char))
            else:
                answer += char
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, char))
        return answer