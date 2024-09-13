class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        If we build prefix sum array with len = n, we have to check if left == 0
        to avoid out of array index error.
        So, we build prefix sum array with len = n + 1, and put prefix[0] = 0,
        because x ^ 0 = x
        """
        n = len(arr)
        pre = [0] * (n + 1)
        pre[1] = arr[0]
        for i in range(1, n):
            pre[i + 1] = pre[i] ^ arr[i]
        
        result = []
        for (left, right) in queries:
            result.append(pre[left] ^ pre[right + 1])
        return result

        