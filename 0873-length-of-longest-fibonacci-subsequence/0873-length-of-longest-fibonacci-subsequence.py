class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        n = len(arr)
        answer = 0

        for i in range(n):
            for j in range(i + 1, n):
                prev = arr[j]
                cur = arr[i] + arr[j]
                cur_size = 2 # i and j, doesn't include cur yet

                while cur in arr_set:
                    cur_size += 1
                    answer = max(answer, cur_size)
                    prev, cur = cur, cur + prev
        return answer
                    