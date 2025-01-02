class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        answer = [0] * len(queries)
        prefix = [0] * len(words)
        prev_sum = 0
        for i in range(len(words)):
            if words[i] and words[i][0] in vowels and words[i][-1] in vowels:
                prev_sum += 1
            prefix[i] = prev_sum
        for i in range(len(queries)):
            start, end = queries[i]
            answer[i] = prefix[end] - prefix[max(0, start - 1)]
        return answer