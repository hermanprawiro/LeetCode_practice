class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1, p2 = 0, 0

        def getMin():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0: # even, so get avg of idx (m+n)/2 and (m+n)/2+1
            for _ in range((m + n) // 2 - 1):
                getMin()
            return (getMin() + getMin()) / 2
        else: # odd, get the val of idx (m+n)/2
            for _ in range((m + n) // 2):
                getMin()
            return getMin()