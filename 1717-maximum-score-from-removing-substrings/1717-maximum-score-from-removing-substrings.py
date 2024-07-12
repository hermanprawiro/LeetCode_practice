class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedily remove all occurences of a substring one after another
        # ordered by its score (descending)
        if x > y:
            words = ["ab", "ba"]
            scores = [x, y]
        else:
            words = ["ba", "ab"]
            scores = [y, x]

        ans = 0
        for word, score in zip(words, scores):
            stack = []

            for c in s:
                stack.append(c)
                if len(stack) >= 2:
                    # peek the last 2 chars and compare with the current substring
                    cur = stack[-2] + stack[-1]
                    if cur == word:
                        ans += score
                        stack.pop()
                        stack.pop()
            # build a new string from what remains after removal
            s = "".join(stack)

        return ans