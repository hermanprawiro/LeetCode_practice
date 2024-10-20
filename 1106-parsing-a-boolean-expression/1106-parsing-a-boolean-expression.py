class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque()

        for char in expression:
            if char == ")":
                values = []
                while stack[-1] != "(":
                    values.append(stack.pop())
                stack.pop() # "("
                operator = stack.pop()
                stack.append(self.evaluate(operator, values))
            elif char != ",":
                stack.append(char)
        return stack[-1] == "t"

    def evaluate(self, operator: str, values: List[str]) -> str:
        if operator == "!":
            return "f" if values[0] == "t" else "t"
        
        if operator == "&":
            for val in values:
                if val == "f":
                    return "f"
            return "t"
        
        if operator == "|":
            for val in values:
                if val == "t":
                    return "t"
            return "f"
        
        return "f"