class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        answer = 0
        for word in words:
            word = set(word)
            if all(char in allowed for char in word):
                answer += 1
            # consistent = True
            # for letter in word:
            #     if letter not in allowed:
            #         consistent = False
            # answer += 1 if consistent else 0
        return answer