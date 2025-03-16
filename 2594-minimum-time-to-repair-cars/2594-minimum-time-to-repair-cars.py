class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Time `t` for a mechanic with rank `r` to repair `n` cars is:
        t = r * n**2

        Using binary search, we want to constraints t <= mid, so:
        r * n**2 <= mid

        Solving for n:
        n <= (mid / r) ** 0.5
        """
        low = 1
        high = max(ranks) * cars * cars

        while low < high:
            mid = low + (high - low) // 2
            n_cars = sum(int((mid / rank) ** 0.5) for rank in ranks) # we want to floor rounding

            if n_cars < cars:
                low = mid + 1
            else:
                high = mid
        return low
        