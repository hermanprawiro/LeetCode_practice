class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}

        for start in range(len(s)):
            char = s[start]
            for end in range(start, len(s)):
                if char == s[end]:
                    length = end - start + 1
                    count[(char, length)] = count.get((char, length), 0) + 1
                else:
                    break
        answer = 0
        for (_, length), freq in count.items():
            if freq >= 3:
                answer = max(answer, length)
        return -1 if answer == 0 else answer