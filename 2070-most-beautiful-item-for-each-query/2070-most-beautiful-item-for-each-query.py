class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        # inplace modify items into the prefix max
        cur_max = items[0][1]
        for i in range(len(items)):
            cur_max = max(cur_max, items[i][1])
            items[i][1] = cur_max
        return [self.binarySearch(items, q) for q in queries]

    def binarySearch(self, items: List[List[int]], target: int) -> int:
        l, r = 0, len(items) - 1
        result = 0
        while l <= r:
            mid = l + (r - l) // 2
            if items[mid][0] > target:
                r = mid - 1
            else:
                result = max(result, items[mid][1])
                l = mid + 1
        return result