class Solution:
    def fractionAddition(self, expression: str) -> str:
        # manual parsing then add/subtract using cross multiplication
        # then simplify the end result by finding greatest common denominator
        num = 0
        denom = 1
        
        n = len(expression)
        i = 0
        while i < n:
            cur_num = 0
            cur_denom = 0
            is_negative = False

            if expression[i] == "-":
                is_negative = True
                i += 1
            elif expression[i] == "+":
                is_negative = False
                i += 1
            
            # numerator
            while i < n and expression[i] != "/":
                val = int(expression[i])
                cur_num = cur_num * 10 + val
                i += 1
            i += 1
            if is_negative:
                cur_num *= -1

            # denominator
            while i < n and expression[i] not in ("-", "+"):
                val = int(expression[i])
                cur_denom = cur_denom * 10 + val
                i += 1
            
            num = num * cur_denom + cur_num * denom
            denom = denom * cur_denom
        
        gcd = abs(self.find_gcd(num, denom))
        num = num // gcd
        denom = denom // gcd
        
        return f"{num}/{denom}"

    def find_gcd(self, a, b):
        if a == 0:
            return b
        return self.find_gcd(b % a, a)