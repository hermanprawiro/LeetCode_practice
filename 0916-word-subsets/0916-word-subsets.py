class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq_max = [0] * 26
        for word in words2:
            for k, v in enumerate(self.countFreq(word)):
                freq_max[k] = max(freq_max[k], v)
        
        answer = []
        for word in words1:
            if all(a >= b for a, b in zip(self.countFreq(word), freq_max)):
                answer.append(word)
        return answer


    def countFreq(self, word: str) -> List[str]:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        return freq
