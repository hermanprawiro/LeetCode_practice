class Solution:
    def minimumDeletions(self, s: str) -> int:
        n_b = 0 # num of char 'b'
        answer = 0

        for c in s:
            if c == 'b':
                n_b += 1
            elif n_b:
                # because c can only 'a' or 'b'
                # if we found 'a' after 'b', we have two options
                # either remove the 'a' or remove all encountered 'b'
                # the answer is whichever the smallest
                answer = min(answer + 1, n_b)
        return answer
        