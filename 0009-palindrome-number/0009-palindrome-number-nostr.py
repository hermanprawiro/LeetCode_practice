class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if the x < 0, it's not a palindrome
        # if the last digit is 0, it's a palindrome only if x == 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x = x // 10
        
        # if the length of odd, ignore the middle digit
        return x == reverted or x == (reverted // 10)