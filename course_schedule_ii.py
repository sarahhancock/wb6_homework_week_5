class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neighbors[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neighbors[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        if not dic:
            return res
        else:
            return []