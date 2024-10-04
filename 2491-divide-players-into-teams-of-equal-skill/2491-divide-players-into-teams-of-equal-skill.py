class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n_teams = len(skill) // 2
        total = 0
        maps = defaultdict(int)
        for val in skill:
            maps[val] += 1
            total += val
        if total % n_teams:
            return -1
        target = total // n_teams
        visited = set()
        result = []
        for val, count in maps.items():
            if val in visited:
                continue
            if val >= target:
                return -1
            need_val = target - val
            if maps[need_val] != maps[val]:
                return -1
            n_team = count if val != need_val else count // 2
            result.append(val * need_val * n_team)
            visited.add(val)
            visited.add(need_val)
        return sum(result)
            