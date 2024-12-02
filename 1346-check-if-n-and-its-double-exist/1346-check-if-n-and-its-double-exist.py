class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or (num // 2 in seen and num % 2 == 0):
                return True
            if num not in seen:
                seen.add(num)
        return False
        