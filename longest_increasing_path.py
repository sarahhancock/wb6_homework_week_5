class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        hashmap = {}
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                count = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] < matrix[i][j]:
                        count += 1
                hashmap[(i, j)] = count
                
                if count == 0:
                    queue.append((i, j))
        step = 0
        while queue:
            size = len(queue)
            for k in range(size):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] > matrix[i][j] and (x, y) in hashmap:
                        hashmap[(x, y)] -= 1
                        if hashmap[(x, y)] == 0:
                            queue.append((x, y))
            step += 1
        return step