class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, array: List[int]) -> List[int]:
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self.mergeSort(array[:mid])
        right = self.mergeSort(array[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    # Got TLE on large arrays with duplicate values
    def quickSort(self, array: List[int], lo: int, hi: int) -> None:
        while lo < hi:
            pivot = self.partition(array, lo, hi)
            # Tail call optimization
            if pivot - lo < hi - pivot:
                self.quickSort(array, lo, pivot - 1)
                lo = pivot + 1
            else:
                self.quickSort(array, pivot + 1, hi)
                hi = pivot - 1

    def partition(self, array: List[int], lo: int, hi: int) -> int:
        # select random number as pivot, then swap with high
        pivot_idx = random.randint(lo, hi)
        array[pivot_idx], array[hi] = array[hi], array[pivot_idx]
        pivot = array[hi]
        i = lo

        for j in range(lo, hi):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[i], array[hi] = array[hi], array[i]
        return i