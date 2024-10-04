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
        target = total // n_teams # target skill for each team
        # iterate the map with an additional visited set to skip the partner's
        visited = set()
        answer = 0
        for val, count in maps.items():
            if val in visited:
                continue
            if val >= target: # if the individual skill >= team skill
                return -1
            partner_val = target - val
            if maps[partner_val] != maps[val]:
                return -1
            n_team = count if val != partner_val else count // 2
            answer += val * partner_val * n_team
            visited.add(val)
            visited.add(partner_val)
        return answer
            