import unittest
import sys
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


class EulerianCycleTest(unittest.TestCase):
    def test_count_edges(self):
        self.assertEqual(count_edges({0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}), 12)
        
    def test_has_eulerian_path(self):
        self.assertEqual(HasEulerianPath([1, 1, 2, 1, 1, 1, 2, 1, 1, 1], [1, 1, 2, 1, 1, 1, 2, 1, 1, 1]), True)
        
if __name__ == "__main__":
    #unittest.main()
    #graph1 = {"AGG": ['GGG'], "CAG": ['AGG', 'AGG'], "GAG": ['AGG'], "GGA": ['GAG'], "GGG": ['GGA','GGG']}
    graph1 = {'CTT': ['TTA'], 'TTA': ['TAC'], 'ACC': ['CCA'], 'CCA': [], 'TAC': ['ACC'], 'GGC': ['GCT'], 'GCT': ['CTT']}
    print(EulerianPath(graph1))
    #print("***********************************")
    lines = open("test.txt", "r").readlines()
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

    res = EulerianPath(graph)
    
    for node in res:
        print(f"{node}->", end = "")
    print()
    
    pass