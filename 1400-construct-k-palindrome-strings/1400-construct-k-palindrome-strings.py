class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        Palindrome can be formed from:
        * One letter string (ex: 'a')
        * Even freq chars (ex: 'aabb', 'abba')
        * One odd freq char in the mid + even freq chars (ex: 'abcba')
        Assume n is the length of string and m is the num of odd freq chars.
        It will be invalid if n < k or m > k.
        """
        n = len(s)
        if n == k: # One letter string palindromes
            return True
        if n < k: # Impossible because n is the max
            return False
        
        freq = [0] * 26
        m = 0
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for count in freq:
            if count % 2 == 1:
                m += 1
        if m > k:
            return False
        return True