class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        Brute force using sliding window and counting vowel is inefficient.
        We don't really need to know the exact count of the vowels.
        We can use boolean to indicate whether each vowel count is even or odd. 
        We can use 5 bits to track 5 vowels. (e.g., first bit is 'a', second is 'e', etc.).
        Then we calculate running XOR value, 0 for even and 1 for odd.
        This way, we have 32 possibilities, where 0 for all even and 31 for all odd.
        We need to track the index of the first occurence of each case (xor value), then when we
        encounter a same xor value again, we can count the length of the subarray.
        """
        n = len(s)
        charmap = [0] * 26
        charmap[ord('a') - ord('a')] = 2**0
        charmap[ord('e') - ord('a')] = 2**1
        charmap[ord('i') - ord('a')] = 2**2
        charmap[ord('o') - ord('a')] = 2**3
        charmap[ord('u') - ord('a')] = 2**4
        idxmap = [-1] * 32
        answer = 0
        xor = 0
        for i in range(n):
            xor ^= charmap[ord(s[i]) - ord('a')]
            if xor != 0 and idxmap[xor] == -1:
                idxmap[xor] = i
            answer = max(answer, i - idxmap[xor])
        return answer