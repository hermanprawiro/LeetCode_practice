class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        result = -1
        left = 1
        right = max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            cons_flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    cons_flowers += 1
                    bouquets += cons_flowers // k
                    cons_flowers = cons_flowers % k
                else:
                    cons_flowers = 0
            if bouquets >= m:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
                    
        