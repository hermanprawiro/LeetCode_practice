class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        max_len = max(len1, len2)

        result = ""
        carry = 0
        for i in range(max_len):
            v1 = int(num1[-1 -i]) if i < len1 else 0
            v2 = int(num2[-1 -i]) if i < len2 else 0
            cur = carry + v1 + v2
            carry = cur // 10
            cur = cur % 10
            result += str(cur)
        
        if carry > 0:
            result += str(carry)

        return result[::-1]
            
