class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        is_negative = k < 0
        if k == 0:
            return result
        elif is_negative:
            code = code[::-1]
            k = -k
        
        code = code + code[:k]
        result[0] = sum(code[1:k+1])
        for i in range(1, n):
            result[i] = result[i - 1] - code[i] + code[i + k]
        return result[::-1] if is_negative else result
        