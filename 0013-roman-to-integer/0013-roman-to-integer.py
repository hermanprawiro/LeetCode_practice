class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        for i in range(len(s)):
            current_let = s[i]
            current_val = values[current_let]
            
            if i < len(s) - 1:
                next_let = s[i+1]
                if (current_let == 'C' and next_let in ['D', 'M']) or (current_let == 'X' and next_let in ['L', 'C']) or (current_let == 'I' and next_let in ['V', 'X']):
                    current_val *= -1
                    
            result += current_val
            
        return result