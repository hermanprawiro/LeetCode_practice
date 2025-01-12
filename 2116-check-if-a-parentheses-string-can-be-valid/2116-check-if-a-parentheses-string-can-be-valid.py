class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        Every closing bracket should has an opening bracket.
        So, if string length is even, it's invalid.
        An opening bracket can be build from locked open bracked or unlocked one.
        We prioritize from the locked one first. 
        So, we need two stacks. However, we only need to count how many of them, so just use two ints.
        """
        n = len(s)
        if n % 2 == 1:
            return False

        # unlocks = []
        # open_brackets = []
        n_unlock = 0
        n_open = 0
        for i in range(n):
            if locked[i] == '0':
                # unlocks.append(i)
                n_unlock += 1
            elif s[i] == '(':
                # open_brackets.append(i)
                n_open += 1
            else:
                # if open_brackets:
                #     open_brackets.pop()
                # elif unlocks:
                #     unlocks.pop()
                
                if n_open > 0:
                    n_open -= 1
                elif n_unlock > 0:
                    n_unlock -= 1
                else:
                    return False
        return True