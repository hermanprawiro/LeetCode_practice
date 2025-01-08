class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                answer += int(self.isPrefixAndSuffix(words[i], words[j]))
        return answer
        
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        if n1 > n2:
            return False
        return str2[:n1] == str1 and str2[-n1:] == str1
        