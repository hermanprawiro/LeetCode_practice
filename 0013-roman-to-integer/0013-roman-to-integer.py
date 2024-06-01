class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            cur_letter = s[i]
            cur_value = char_map[cur_letter]
            
            if i > 0 and (cur_value > char_map[s[i - 1]]):
                # compare with the previous letter
                # if the current one is larger than the previous one,
                # substract 2x to also substract the previous step (else)
                result += cur_value - (2 * char_map[s[i - 1]])
            else:
                result += cur_value

        return result
        