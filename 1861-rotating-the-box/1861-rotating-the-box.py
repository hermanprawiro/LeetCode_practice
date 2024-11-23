class Solution:
    STONE = '#'
    OBSTACLE = '*'
    EMPTY = '.'
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rbox = [[self.EMPTY] * m for _ in range(n)]
        for j in range(m):
            bot = n - 1
            for top in range(n - 1, -1, -1):
                if box[j][top] == self.STONE:
                    rbox[bot][m - j - 1] = self.STONE
                    bot -= 1
                if box[j][top] == self.OBSTACLE:
                    rbox[top][m - j - 1] = self.OBSTACLE
                    bot = top - 1
        return rbox
