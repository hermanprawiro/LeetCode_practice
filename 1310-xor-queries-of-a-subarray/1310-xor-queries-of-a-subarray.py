class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0] * n
        pre[0] = arr[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ arr[i]
        
        result = []
        for i, (left, right) in enumerate(queries):
            if left == right:
                result.append(arr[right])
            elif left == 0:
                result.append(pre[right])
            else:
                result.append(pre[left - 1] ^ pre[right])
        return result

        