class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self._quickSort(nums, 0, len(nums) - 1)
        answer = "".join(map(str, nums))
        return "0" if nums[0] == 0 else answer

    def _quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        pivot = self._partition(nums, left, right)
        self._quickSort(nums, left, pivot - 1)
        self._quickSort(nums, pivot + 1, right)

    def _partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if self._compare(nums[j], pivot):
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def _compare(self, a: int, b: int) -> bool:
        return (str(a) + str(b)) > (str(b) + str(a))