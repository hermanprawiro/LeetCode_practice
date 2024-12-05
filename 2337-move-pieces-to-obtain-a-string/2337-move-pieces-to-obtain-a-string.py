class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i_start = i_target = 0
        n = len(start)
        while i_start < n or i_target < n:
            while i_start < n and start[i_start] == '_':
                i_start += 1
            while i_target < n and target[i_target] == '_':
                i_target += 1
            # if one of the index reach the end, the other one must be too
            # otherwise, length without empty char differs
            if i_start == n or i_target == n:
                return i_start == n and i_target == n
            # check validity
            if (
                start[i_start] != target[i_target] or
                (start[i_start] == 'L' and i_start < i_target) or
                (start[i_start] == 'R' and i_start > i_target)
            ):
                return False
            # both char valid, so continue
            i_start += 1
            i_target += 1
        return True # normal case and valid


