def bfs(source, graph, visited, parent, distance):
        q = deque()
        q.append(source)
        distance[source] = 0

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = node
                    distance[neighbor] = distance[node] + 1 # every neighbor is at the same level while traversing through graph
                    q.append(neighbor)
                else:
                    if parent[node] != neighbor: # if true, then CYCLE is there + it means there are cross edges
                        # if odd length CYCLE and both of them are on the same level
                        if distance[node] == distance[neighbor]:
                            return False # graph is not bipartite
        return True

class Solution(object):
   


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # no need to build the graph, already built
        
        # loop through nodes
        n = len(graph)
        components = 0

        visited = [-1] * n
        parent = [-1] * n
        distance = [-1] * n

        for node in range(len(graph)):
            if visited[node] == -1:
                visited[node] = 1
                if bfs(node, graph, visited, parent, distance) is False:
                    return False
        
        return True