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
        # will count each team twice, so divide the answer by 2 in the end
        answer = 0
        for val in skill:
            if val >= target: # if the individual skill >= team skill
                return -1
            partner_val = target - val
            if maps[partner_val] != maps[val]: # check if partner exists
                return -1
            answer += val * partner_val
        return answer // 2
            