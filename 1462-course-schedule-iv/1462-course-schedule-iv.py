class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        for (i, j) in prerequisites:
            is_prereq[i][j] = True

        for mid in range(numCourses):
            for source in range(numCourses):
                for target in range(numCourses):
                    is_prereq[source][target] = is_prereq[source][target] or (
                        is_prereq[source][mid] and is_prereq[mid][target]
                    )
        
        answer = []
        for (i, j) in queries:
            answer.append(is_prereq[i][j])
        return answer