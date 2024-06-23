## Think for only one generic NODE with all the possible cases possible for any node -
   # 0 case - jsut detecting a back edge is not enough
   # 1 case - from my subordinates, i want as ans what's the lowest arr time or the highest back edge goes to 
   # 2 case - there is a back edge going out of (me) NODE itself, in that case, the lowest arr time would be min of mine or my nei (where my back edge leads to)

# the whole code is written mainly for one NODE only
def dfs(NODE, visited, arr, timestamp, lowestarr, adjlist, result, parent):
    visited[NODE] = 1
    arr[NODE] = timestamp
    lowestarr[NODE] = arr[NODE] # set the arr and lowest arr times initially
    timestamp += 1 # after that increase the time

    for nei in adjlist[NODE]:
        if visited[nei] == -1:
            parent[nei] = NODE
            lowestarr[NODE] = min (dfs(nei, visited, arr, timestamp, lowestarr, adjlist, result, parent) , lowestarr[NODE])
        else:
            # this detected back edge will be going back from the NODE itself
            if nei != parent[NODE]: ## if any of the neighbors leads to an ancestor instead of parent, then its a back edge
                lowestarr[NODE] = min(lowestarr[NODE], arr[nei]) 

    if lowestarr[NODE] == arr[NODE] and NODE != 0:
        result.append([NODE, parent[NODE]])
    return lowestarr[NODE]

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        # n - no of NODEs
        # connections - edges

        # build the graph
        adjlist = [[] for i in range(n)]

        for (u,v) in connections:
            adjlist[u].append(v)
            adjlist[v].append(u)
            
        visited = [-1] * n
        arr = [-1] * n
        timestamp = 0
        lowestarr = [-1] * n 
        parent = [-1] * n
        result = []
        # outer loop

        dfs(0, visited, arr, timestamp, lowestarr, adjlist, result, parent)
        # dfs/bfs
        print(arr)
       
        return result