class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # use counting sort
        max_n = 100
        count_seat = [0 for i in range(max_n + 1)]
        count_student = [0 for i in range(max_n + 1)]

        for seat in seats:
            count_seat[seat] += 1
        for student in students:
            count_student[student] += 1

        i_seat = 0
        i_student = 0
        result = 0
        while i_seat <= max_n and i_student <= max_n:
            while i_seat <= max_n and count_seat[i_seat] == 0:
                i_seat += 1
            while i_student <= max_n and count_student[i_student] == 0:
                i_student += 1
            
            if i_seat <= max_n and i_student <= max_n:
                # could be multiple seats or students in the same position
                count = min(count_seat[i_seat], count_student[i_student])
                result += abs(i_seat - i_student) * count
                count_seat[i_seat] -= count
                count_student[i_student] -= count
        return result