class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # assume sentence1 is the longer one
        if len(sentence1) < len(sentence2):
            return self.areSentencesSimilar(sentence2, sentence1)

        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")

        left, right = 0, 1
        while left < len(words2) and words1[left] == words2[left]:
            left += 1
        while right <= len(words2) and words1[len(words1) - right] == words2[len(words2) - right]:
            right += 1
        return (len(words2) - right) < left
        