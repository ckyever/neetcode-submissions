class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {}

        for course in range(numCourses):
            courseMap[course] = []

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        completed = []

        visited = set()
        def dfs(course):
            if not courseMap[course]:
                if course not in completed:
                    completed.append(course)
                return True

            for prereq in courseMap[course]:
                if prereq in visited:
                    return False

                visited.add(prereq)
                if not dfs(prereq):
                    return False
                visited.remove(prereq)

            if course not in completed:
                completed.append(course)
            
            return True

        for course in courseMap.keys():
            if not dfs(course):
                return []
        
        return completed
