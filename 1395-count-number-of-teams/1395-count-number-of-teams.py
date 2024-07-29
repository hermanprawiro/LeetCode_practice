class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        loop for each soldier as the middle one, then
        count how many soldiers with smaller/larger rating
        on the left and on the right
        num of ascending teams will be n_smaller_left * n_larger_right
        num of descending teams will be n_larger_left * n_smaller_right
        answer is the sum for all soldiers
        """
        answer = 0
        for i in range(len(rating)):
            answer += self.countTeams(rating, i)
        return answer
        
    def countSmallerLarger(self, rating: List[int], start: int, end: int, ref: int) -> Tuple[int, int]:
        n_small = 0
        n_large = 0

        for i in range(start, end):
            if rating[i] < ref:
                n_small += 1
            elif rating[i] > ref:
                n_large += 1
        return n_small, n_large

    def countTeams(self, rating: List[int], current: int) -> int:
        n_left = self.countSmallerLarger(rating, 0, current, rating[current])
        n_right = self.countSmallerLarger(rating, current + 1, len(rating), rating[current])

        n_smaller_left, n_larger_left = n_left
        n_smaller_right, n_larger_right = n_right
        n_ascending = n_smaller_left * n_larger_right
        n_descending = n_larger_left * n_smaller_right

        return n_ascending + n_descending