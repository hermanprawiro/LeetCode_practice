class Solution:
    def maximum69Number (self, num: int) -> int:
        answer = list(str(num))
        for i, digit in enumerate(answer):
            if digit == '6':
                answer[i] = '9'
                break
        return int(''.join(answer))
