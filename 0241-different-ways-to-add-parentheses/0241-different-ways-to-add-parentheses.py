class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        if len(expression) == 0:
            return results
        elif len(expression) <= 2 and expression.isdigit():
            return [int(expression)]
        
        for i, char in enumerate(expression):
            if char.isdigit():
                continue

            lefts = self.diffWaysToCompute(expression[:i])
            rights = self.diffWaysToCompute(expression[i+1:])

            for left in lefts:
                for right in rights:
                    if char == "+":
                        results.append(left + right)
                    elif char == "-":
                        results.append(left - right)
                    elif char == "*":
                        results.append(left * right)

        return results
        