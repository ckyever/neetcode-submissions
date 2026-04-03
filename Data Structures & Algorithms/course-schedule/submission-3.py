class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            self.count = 0
            def canFinish(course):
                # Course does not have prerequisites
                if course not in graph:
                    return True

                # Must be stuck in cycle
                if self.count > numCourses:
                    return False
                
                for prereq in graph[course]:
                    self.count += 1

                    # If any preqreq is unfinishable this course is unfinishable
                    if not canFinish(prereq):
                        return False
                    self.count -= 1
                
                return True
            
            if not canFinish(course):
                return False
        
        return True