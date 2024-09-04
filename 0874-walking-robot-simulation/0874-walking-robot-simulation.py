class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_i = 0
        obs = {tuple(k): 0 for k in obstacles}

        cur_x = 0
        cur_y = 0
        # return the max dist that the robot EVER GETS
        dist = 0
        for command in commands:
            if command == -2:
                dir_i = dir_i - 1
                if dir_i < 0:
                    dir_i = 4 + dir_i
            elif command == -1:
                dir_i = (dir_i + 1) % 4
            else:
                for _ in range(command):
                    next_x = cur_x + directions[dir_i][0]
                    next_y = cur_y + directions[dir_i][1]
                    if (next_x, next_y) not in obs:
                        cur_x = next_x
                        cur_y = next_y
            dist = max(dist, cur_x ** 2 + cur_y ** 2)
        return dist
        