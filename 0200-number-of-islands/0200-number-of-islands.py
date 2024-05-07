class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Grid Problem, Graphs type - BFS
        # Not every grid problem will be a graph problem, it may be backtracking
        # Approach - we have to find the number of components basically, use the generic template

        # bfs approach
        def bfs(grid, i, j, nr, nc):
        # //put the node in the queue
            # //look for its neighbors i.e. 1s 
            # //if 1 add them to queue
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            #wrong q = deque((i,j))
            # two methods of adding a tuple to the queue
            q = deque([(i,j)]) 
            # q = deque()
            # q.append((i,j))

            grid[i][j] = '0'

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    rr = dr+r
                    cc = dc+c
                    if 0<= rr < nr and 0<=cc<nc:
                        if grid[rr][cc] == '1': #all 8 directions
                            grid[rr][cc] = '0'
                            q.append((rr,cc))
    
        # outer loop
        components = 0
        nc = len(grid[0])
        nr = len(grid)
        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    components += 1
                    bfs(grid, i, j, nr, nc)
                else:
                    continue
        
        return components

        