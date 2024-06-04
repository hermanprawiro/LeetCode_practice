class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return num

        result = 0
        while len(s) > 1:
            result = 0
            for i in s:
                result += int(i)
            s = str(result)

        return result