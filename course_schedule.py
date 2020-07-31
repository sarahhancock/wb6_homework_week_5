class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
            
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        while queue:
            node = queue.popleft()
            for neighbor in backward[node]:
                forward[neighbor].remove(node)
                if len(forward[neighbor]) == 0:
                    queue.append(neighbor)
            forward.pop(node)
        return not forward