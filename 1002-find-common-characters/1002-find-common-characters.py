class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        result = []
        commons = list(set(words[0])) # remove duplicates
        for char in commons:
            counts = []
            for i in range(len(words)):
                char_count = words[i].count(char)
                counts.append(char_count)
                # if a word doesn't contain that char, no need to continue
                if char_count == 0:
                    break
            min_count = min(counts)
            for _ in range(min_count):
                result.append(char)
        return result
