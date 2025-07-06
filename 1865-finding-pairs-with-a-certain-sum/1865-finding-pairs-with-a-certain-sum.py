class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.counter2 = {}
        for num in nums2:
            self.counter2[num] = self.counter2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter2[self.nums2[index]] = self.counter2.get(self.nums2[index], 0) + 1

    def count(self, tot: int) -> int:
        answer = 0
        for num in self.nums1:
            if (tot - num) in self.counter2.keys():
                answer += self.counter2[tot - num]
        return answer
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)