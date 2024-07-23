class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # count the number's frequency
        # {num: freq}
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        # get all the numbers for each frequency
        # {freq : [num, ..., num]}
        freq_list = defaultdict(list)
        for num, freq in freqs.items():
            freq_list[freq].append(num)

        # assemble the result
        
        result = []
        for freq in sorted(freq_list.keys()):
            nums_in_freq = freq_list[freq]
            if len(nums_in_freq) == 1:
                result += nums_in_freq * freq
            else:
                nums_in_freq.sort(reverse=True)
                for num in nums_in_freq:
                    result += [num] * freq

        return result