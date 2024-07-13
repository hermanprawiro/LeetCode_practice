class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append({
                'pos': positions[i],
                'hp': healths[i],
                'dir': directions[i],
                'idx': i
            })
        robots.sort(key=lambda x: x['pos'])

        # similar idea to bracket matching, we store R robots in stack
        # then when we found L robots, we check the collision
        stack = []
        for i in range(n):
            if robots[i]['dir'] == 'L':
                while stack and robots[stack[-1]]['dir'] == 'R' and robots[stack[-1]]['hp'] < robots[i]['hp']:
                    stack.pop()
                    robots[i]['hp'] -= 1
                if not stack or robots[stack[-1]]['dir'] == 'L':
                    stack.append(i)
                elif stack and robots[stack[-1]]['hp'] == robots[i]['hp']:
                    stack.pop()
                elif stack and robots[stack[-1]]['hp'] > robots[i]['hp']:
                    robots[stack[-1]]['hp'] -= 1
            else:
                stack.append(i)
        return [robots[i]['hp'] for i in sorted(stack, key=lambda x: robots[x]['idx'])]