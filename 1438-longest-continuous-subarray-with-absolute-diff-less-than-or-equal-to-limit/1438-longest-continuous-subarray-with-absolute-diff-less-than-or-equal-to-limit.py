class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q_asc = deque()
        q_desc = deque()
        result = 0
        l = 0

        for r in range(len(nums)):
            val = nums[r]
            while q_asc and val < q_asc[-1]:
                q_asc.pop()
            q_asc.append(val)

            while q_desc and val > q_desc[-1]:
                q_desc.pop()
            q_desc.append(val)

            while q_desc[0] - q_asc[0] > limit:
                if nums[l] == q_asc[0]:
                    q_asc.popleft()
                if nums[l] == q_desc[0]:
                    q_desc.popleft()
                l += 1
            
            result = max(result, r - l + 1)
        return result
        