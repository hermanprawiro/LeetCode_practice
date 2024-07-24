class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []
        for num in nums:
            new_num = ""
            for digit in str(num):
                new_num += str(mapping[int(digit)])
            mapped_nums.append(int(new_num))

        return [x for x, _ in sorted(zip(nums, mapped_nums), key=lambda i: i[1])]
