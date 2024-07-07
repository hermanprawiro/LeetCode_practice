class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n_drink = numBottles
        n_full = 0
        n_empty = numBottles

        while n_empty >= numExchange:
            n_full = n_empty // numExchange
            n_empty = n_empty % numExchange
            n_drink += n_full
            n_empty += n_full
            n_full = 0

        return n_drink