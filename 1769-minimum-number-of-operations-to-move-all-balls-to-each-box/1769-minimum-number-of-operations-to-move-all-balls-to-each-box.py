class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        left_balls = 0
        left_moves = 0
        right_balls = 0
        right_moves = 0
        for i in range(n):
            left = i
            answer[left] += left_moves
            left_balls += 1 if boxes[left] == '1' else 0
            left_moves += left_balls

            right = n - 1 - i
            answer[right] += right_moves
            right_balls += 1 if boxes[right] == '1' else 0
            right_moves += right_balls
        return answer
