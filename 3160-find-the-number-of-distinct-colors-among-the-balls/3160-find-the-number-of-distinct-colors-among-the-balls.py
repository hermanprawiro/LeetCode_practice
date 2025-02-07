class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        answer = [0] * n

        ball_map = {} # color of each ball
        color_freq = {} # count of each color
        
        for i in range(n):
            ball, color = queries[i]
            if color in color_freq:
                color_freq[color] += 1
            else:
                color_freq[color] = 1

            if ball in ball_map:
                prev_color = ball_map[ball]
                color_freq[prev_color] -= 1
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]

            ball_map[ball] = color
            answer[i] = len(color_freq)
        
        return answer
