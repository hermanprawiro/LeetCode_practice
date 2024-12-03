class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev = 0
        for i in spaces:
            result.append(s[prev:i])
            result.append(" ")
            prev = i
        result.append(s[prev:])
        return "".join(result)