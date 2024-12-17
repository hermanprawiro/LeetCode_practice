class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        pq = [] # max heap
        for k, v in enumerate(freq):
            if v > 0:
                heapq.heappush(pq, (-k, v))
        
        answer = []
        while pq:
            char_i, char_count = heapq.heappop(pq)
            char = chr(-char_i + ord('a'))
            n_use = min(repeatLimit, char_count)
            answer.append(char * n_use)
            if char_count > n_use and pq: # there's a remainder
                next_char_i, next_char_count = heapq.heappop(pq)
                answer.append(chr(-next_char_i + ord('a')))
                if next_char_count > 1:
                    heapq.heappush(pq, (next_char_i, next_char_count - 1))
                heapq.heappush(pq, (char_i, char_count - n_use))
        return "".join(answer)