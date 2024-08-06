class Solution:
    def minimumPushes(self, word: str) -> int:
        count = defaultdict(int)
        for c in word:
            count[c] += 1
        
        # we descendingly sort the letters based on its frequency
        # because we can only assign to key 2-9 (8 keys)
        # we prioritizes the highest freq letter to get 1 press and so on
        # top 8 highest freq letters get 1 press, 9th-16th get 2 press, ...
        answer = 0
        for i, (k, v) in enumerate(sorted(count.items(), key=lambda x: x[1], reverse=True)):
            answer += v * ((i // 8) + 1)
        return answer