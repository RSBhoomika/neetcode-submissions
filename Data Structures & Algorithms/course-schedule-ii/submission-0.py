class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
        res = []
        visited = [0]*numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
        