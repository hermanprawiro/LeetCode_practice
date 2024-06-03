class Solution:
    # 1. Horizontal Scanning
    #"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix
    #"""
    # 2. Vertical Scanning
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
    """
    # 3. Divide and Conquer
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        return self.longestCommonPrefixHelper(strs, 0, len(strs) - 1)
    
    def longestCommonPrefixHelper(self, strs: List[str], left: int, right: int) -> str:
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            lcpLeft = self.longestCommonPrefixHelper(strs, left, mid)
            lcpRight = self.longestCommonPrefixHelper(strs, mid + 1, right)
            return self.commonPrefix(lcpLeft, lcpRight)
        
    def commonPrefix(self, left: str, right: str) -> str:
        minLength = min(len(left), len(right))
        for i in range(minLength):
            if left[i] != right[i]:
                return left[:i]
        return left[:minLength]
    """