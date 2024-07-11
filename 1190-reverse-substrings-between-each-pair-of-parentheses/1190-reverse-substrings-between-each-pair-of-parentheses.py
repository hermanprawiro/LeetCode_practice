class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                # pop the opening bracket
                if stack:
                    stack.pop()
                # treat as queue, but we dont need to pop
                for t in temp:
                    stack.append(t)
            else:
                stack.append(c)

        return "".join(stack)