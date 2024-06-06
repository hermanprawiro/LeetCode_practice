class Solution:
    def isValid(self, s: str) -> bool:
        pair_open = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        pair_close = {v: k for k, v in pair_open.items()}

        stack = []
        for char in s:
            if char in pair_open:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != pair_close[char]:
                    return False
        return len(stack) == 0
