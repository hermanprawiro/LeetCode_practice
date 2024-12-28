class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        cur_sum1 = sum(nums[:k])
        cur_sum2 = sum(nums[k:2*k])
        cur_sum3 = sum(nums[2*k:3*k])

        best_start1 = 0
        best_start2 = [0, k]
        best_start3 = [0, k, 2*k]

        best_sum1 = cur_sum1
        best_sum2 = best_sum1 + cur_sum2
        best_sum3 = best_sum2 + cur_sum3

        cur_start1 = best_start1 + 1
        cur_start2 = best_start2[-1] + 1
        cur_start3 = best_start3[-1] + 1

        while cur_start3 <= len(nums) - k:
            cur_sum1 = cur_sum1 - nums[cur_start1 - 1] + nums[cur_start1 + k - 1]
            cur_sum2 = cur_sum2 - nums[cur_start2 - 1] + nums[cur_start2 + k - 1]
            cur_sum3 = cur_sum3 - nums[cur_start3 - 1] + nums[cur_start3 + k - 1]

            if cur_sum1 > best_sum1:
                best_start1 = cur_start1
                best_sum1 = cur_sum1
            
            if best_sum1 + cur_sum2 > best_sum2:
                best_start2[0] = best_start1
                best_start2[1] = cur_start2
                best_sum2 = best_sum1 + cur_sum2
            
            if best_sum2 + cur_sum3 > best_sum3:
                best_start3[0] = best_start2[0]
                best_start3[1] = best_start2[1]
                best_start3[2] = cur_start3
                best_sum3 = best_sum2 + cur_sum3

            cur_start1 += 1
            cur_start2 += 1
            cur_start3 += 1

        return best_start3