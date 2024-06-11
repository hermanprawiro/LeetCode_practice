class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        dict_count = {i: 0 for i in arr2}
        # key_ex = []
        result = []
        result_ex = []

        for i in range(len(arr1)):
            v = arr1[i]
            if v in arr2_set:
                dict_count[v] += 1
            else:
                result_ex.append(v)
                dict_count[v] = 1
        result_ex.sort()
        
        for i in range(len(arr2)):
            v = arr2[i]
            result = result + [v] * dict_count[v]
        return result + result_ex
