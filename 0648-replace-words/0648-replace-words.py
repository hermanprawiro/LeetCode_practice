class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_root = dict.fromkeys(dictionary)
        max_dict = max(map(lambda x: len(x), dictionary))

        result = []
        words = sentence.split(" ")
        for word in words:
            min_len = min(len(word), max_dict)
            prefix = word
            for i in range(min_len):
                prefix = word[:i+1]
                if prefix in dict_root:
                    break
            else:
                prefix = word
            result.append(prefix)
        return ' '.join(result)
