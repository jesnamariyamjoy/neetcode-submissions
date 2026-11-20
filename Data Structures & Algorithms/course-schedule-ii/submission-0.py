class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map: List[List[int]] = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        order: List[int] = []

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False  # Cycle detected
            if state[course] == 2:
                return True

            state[course] = 1
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            state[course] = 2
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return order