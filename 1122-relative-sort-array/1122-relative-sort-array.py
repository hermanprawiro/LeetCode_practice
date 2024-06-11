class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        dict_count = {i: 0 for i in arr2}
        key_ex = []
        result = []

        for i in range(len(arr1)):
            v = arr1[i]
            if v in arr2_set:
                dict_count[v] += 1
            else:
                key_ex.append(v)
                dict_count[v] = 1
        
        key_ex = arr2 + sorted(key_ex)
        for i in range(len(key_ex)):
            v = key_ex[i]
            result = result + [v] * dict_count[v]
        return result
