class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        nums_count = {}
        for i in nums:
            nums_count[i] = nums_count.get(i, 0) + 1
        
        nums_val = sorted(list(nums_count.keys()))

        while len(nums_val):
            key = nums_val[0]
            if nums_count[key] > 0:
                for i in range(k):
                    key_count = nums_count.get(key + i, 0)
                    if key_count == 0:
                        return False
                    new_count = key_count - 1
                    nums_count[key + i] = new_count
                    if new_count == 0:
                        nums_val.remove(key + i)

        return True
        