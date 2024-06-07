class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n_dup = 0
        n = len(arr)
        
        # find the number of zeros
        for i in range(n):
            if i >= n - n_dup:
                # stop if i is beyond the end of new list
                break
            
            if arr[i] == 0:
                # edge case: if the last num is zero
                # we wont duplicate this so just set last idx to zero
                # and exclude it
                if i == (n - n_dup - 1):
                    arr[n - 1] = 0
                    n -= 1
                    break
                n_dup += 1
        
        i_end = n - n_dup - 1
        for i in range(i_end, -1, -1):
            if arr[i] == 0:
                arr[i + n_dup] = 0
                n_dup -= 1
                arr[i + n_dup] = 0
            else:
                arr[i + n_dup] = arr[i]