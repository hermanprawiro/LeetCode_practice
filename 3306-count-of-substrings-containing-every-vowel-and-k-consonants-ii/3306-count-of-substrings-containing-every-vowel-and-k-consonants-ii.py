class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(word)
        answer = 0
        start = end = 0
        n_vowels = {}
        n_cons = 0
        next_cons = [0] * n
        next_cons_idx = n

        for i in range(n - 1, -1, -1):
            next_cons[i] = next_cons_idx
            if word[i] not in vowels:
                next_cons_idx = i
        
        while end < n:
            end_char = word[end]
            if end_char in vowels:
                n_vowels[end_char] = n_vowels.get(end_char, 0) + 1
            else:
                n_cons += 1
            
            while n_cons > k:
                start_char = word[start]
                if start_char in vowels:
                    n_vowels[start_char] -= 1
                    if n_vowels[start_char] == 0:
                        del n_vowels[start_char]
                else:
                    n_cons -= 1
                start += 1

            while start < n and len(n_vowels) == 5 and n_cons == k:
                answer += next_cons[end] - end
                start_char = word[start]
                if start_char in vowels:
                    n_vowels[start_char] -= 1
                    if n_vowels[start_char] == 0:
                        del n_vowels[start_char]
                else:
                    n_cons -= 1
                start += 1
            end += 1
        
        return answer