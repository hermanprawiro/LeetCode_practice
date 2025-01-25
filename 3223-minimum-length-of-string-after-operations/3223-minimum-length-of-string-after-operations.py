class Solution:
    def minimumLength(self, s: str) -> int:
        """
        For each triplet of the same char, we can remove 2. Ex: 'abbbaba' => '_bbbab_' => '_b_ab' => 'bab'.
        If the freq of the char is odd, it will still be odd after removal. Max remaining is 1.
        If the freq of the char is even, it will still be even after removal. Max remaining is 2.
        """
        freq = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            freq[i] += 1
        answer = 0
        for x in freq:
            if x == 0:
                continue
            if x % 2 == 1:
                answer += 1
            else:
                answer += 2
        return answer