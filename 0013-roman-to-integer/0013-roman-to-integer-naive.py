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

            if i < (len(s) - 1):
                next_letter = s[i + 1]
                if (
                    (cur_letter == 'C' and next_letter in ('D', 'M')) or
                    (cur_letter == 'X' and next_letter in ('L', 'C')) or
                    (cur_letter == 'I' and next_letter in ('V', 'X'))
                ):
                    cur_value *= -1
            result += cur_value
        return result
        