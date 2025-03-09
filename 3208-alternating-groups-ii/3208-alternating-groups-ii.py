class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        answer = 0
        
        cur_len = 1
        prev = colors[0]
        for i in range(1, n + k - 1):
            i = i % n
            if colors[i] == prev:
                cur_len = 1
                prev = colors[i]
                continue
            
            cur_len += 1
            if cur_len >= k:
                answer += 1
            prev = colors[i]
        return answer