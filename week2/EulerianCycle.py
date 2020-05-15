import sys
try: 
    import queue
except ImportError:
    import Queue as queue
sys.setrecursionlimit(5000)

def count_edges(graph):
    count = 0
    for node in graph:
        count += len(graph[node])
    
    return count

def count_nodes(graph):
    nodes = []
    for node in graph:
        if not node in nodes:
            nodes.append(node)
        adj = graph[node]
        for elem in adj:
            if not elem in nodes:
                nodes.append(elem)
    
    return len(nodes), nodes

def EulerianPath(graph):
    n, nodes = count_nodes(graph)
    path = []
    in_deg = {}
    out_deg = {}
    
    for node in nodes:
        in_deg[node] = 0
        out_deg[node] = 0
    
    return FindEulerianPath(in_deg, out_deg, graph, n, nodes, path)

def FindEulerianPath(in_deg, out_deg, graph, n, nodes, path):
    m = count_edges(graph)
    in_deg, out_deg = CountInOutDegree(in_deg, out_deg, graph)
    
    if not HasEulerianPath(in_deg, out_deg):
        print("No Eulerian Path!")
        return -1
    
    start = findStartNode(in_deg, out_deg)
    path = dfs(start, out_deg, graph, path)
    
    if len(path) == m + 1:
        return path[::-1]
    
    return -1

def findStartNode(in_deg, out_deg):
    start = 0
    
    for node in in_deg:
        if out_deg[node] - in_deg[node] == 1:
            return node
        if out_deg[node] > 0:
            start = node
    
    return start

def dfs(at, out_deg, graph, path):
    while out_deg[at] != 0:
        next = graph[at][out_deg[at] - 1]
        out_deg[at] -= 1
        dfs(next, out_deg, graph, path)
        
    path.append(at)
    return path        
    
def CountInOutDegree(in_deg, out_deg, graph):
    
    for node in graph:
        neighbors = graph[node]
        for elem in neighbors:
            in_deg[elem] += 1
            out_deg[node] += 1
    
    return in_deg, out_deg

def HasEulerianPath(in_deg, out_deg):
    start, end = 0, 0
    
    for node in in_deg:
        if in_deg[node] - out_deg[node] > 1 or out_deg[node] - in_deg[node] > 1:
            return False
        elif in_deg[node] - out_deg[node] == 1:
            end += 1
        elif out_deg[node] - in_deg[node] == 1:
            start += 1
            
    return(start == 0 and end == 0) or (start == 1 and end == 1)

def MaximalNonBranchingPaths(graph):
    n, nodes = count_nodes(graph)
    paths = []
    in_deg = {}
    out_deg = {}
    for node in nodes:
        in_deg[node] = 0
        out_deg[node] = 0
    in_deg, out_deg = CountInOutDegree(in_deg, out_deg, graph)
    
    visited = {}
    for node in nodes:
        visited[node] = False
    
    for node in graph:
        if (not(in_deg[node] == 1) or not(out_deg[node] == 1)) and not(visited[node]):
            if out_deg[node] > 0:
                for w in graph[node]:
                    non_branching_path = []
                    non_branching_path.append(node)
                    non_branching_path.append(w)
                    while in_deg[w] == 1 and out_deg[w] == 1:
                        visited[w] = True
                        for u in graph[w]:
                            non_branching_path.append(u)
                            w = u
                    paths.append(non_branching_path)
    
    
    for node in graph:
        if in_deg[node] == 1 and out_deg[node] == 1 and not(visited[node]):
            memory = node
            for a in graph[node]:
                isolated_cycle = []
                isolated_cycle.append(memory)
                while in_deg[a] == 1 and out_deg[a] == 1:
                    isolated_cycle.append(a)
                    visited[a] = True
                    if a == memory:
                        visited[memory] = True
                        paths.append(isolated_cycle)
                        break
                    for v in graph[a]:
                        a = v
    return paths

# BFS starting at node
def BreadthFirstSearch(node, n, graph):
    q = queue.Queue()
    q.put(node)
    
    print(node, end = " ")
    
    n, nodes = count_nodes(graph)
    visited = {}
    prev = {}
    for elem in nodes:
        visited[elem] = False
        prev[elem] = []  #track the parent of each node, this is to help reconstruct the path
            
    visited[node] = True
    
    while not q.empty():
        next = q.get()
        neighbors = graph[next]
        
        for elem in neighbors:
            if not visited[elem]:
                print(elem, end = " ")
                q.put(elem)
                visited[elem] = True
                prev[elem].append(next)
    print()
    return prev

#Application
def FindPath(graph, s, e):
    n = len(graph)
    FindPath_bfs(s, e, graph, n)    
    pass

def FindPath_bfs(start, end, graph, n):
    prev = BreadthFirstSearch(start, n, graph)
    
    return reconstruct_path(start, end, prev, n)

def reconstruct_path(start, end, prev, n):
    path = []
    
    at = end
    while at != -1:
        path.append(at)
        at = prev[at]
        
    path.reverse()
    if path[0] == start:
        print(path)
        return path
    
    return []

   
if __name__ == "__main__":
    
    #graph1 = {"AGG": ['GGG'], "CAG": ['AGG', 'AGG'], "GAG": ['AGG'], "GGA": ['GAG'], "GGG": ['GGA','GGG']}
    '''graph1 = {'CTT': ['TTA'], 'TTA': ['TAC'], 'ACC': ['CCA'], 'CCA': [], 'TAC': ['ACC'], 'GGC': ['GCT'], 'GCT': ['CTT']}
    print(EulerianPath(graph1))
    #print("***********************************")
    '''
    '''lines = open("test.txt", "r").readlines()
    graph = {}
    for line in lines:
        tmp = ''
        for index, char in enumerate(line):
            if char != ' ' and char != '-' and char != ">":
                if char != ',' and char != '\n':
                    tmp += char
                elif char == "," or char == '\n':
                    graph[nbr].append(int(tmp))
                    tmp = ""
            if char == '>':
                nbr = int(tmp)
                graph[nbr] = []
                tmp = ''

    #res = EulerianPath(graph)
    res = MaximalNonBranchingPaths(graph)
    #print(graph)
    for path in res:
        N = len(path)
        for i, node in enumerate(path):
            if i == N - 1:
                print(f"{node}")
            else:
                print(f"{node} -> ", end = "")
        
    
    #graph = {1 : [2], 2: [3], 3: [4, 5], 4: [], 5: [], 6: [7], 7: [6]}
    
    '''
    
    pass