class Solution:
    def intToRoman(self, num: int) -> str:
        dict_num = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        result = ""
        for i_num, i_let in dict_num.items():
            result += num // i_num * i_let
            num = num % i_num

        return result