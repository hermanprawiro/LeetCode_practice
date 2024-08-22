class Solution:
    def findComplement(self, num: int) -> int:
        head, tail = bin(num).split('b')
        tail = tail.replace('0', 'a').replace('1', '0').replace('a', '1')
        return int("b".join((head, tail)), 2)