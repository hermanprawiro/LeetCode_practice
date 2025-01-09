class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            if word.startswith(pref):
                answer += 1
        return answer