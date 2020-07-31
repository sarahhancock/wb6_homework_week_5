class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, seen) == False:
                    return False
        return True

    def check(self, graph, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            popped, group = q.pop(0)
            if popped in seen:
                if seen[popped] != group:
                    return False
                continue
            seen[popped] = group
            vertices = graph[popped]
            for v in vertices:
                q.append((v, -group))
        return True