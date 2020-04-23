import unittest

def count_edges(graph):
    count = 0
    for node in graph:
        count += len(graph[node])
    
    return count

def EulerianPath(graph):
    n = len(graph)
    in_deg = [0 for i in range(n)]
    out_deg = [0 for i in range(n)]
    path = []
    
    return FindEulerianPath(in_deg, out_deg, graph, n, path)

def FindEulerianPath(in_deg, out_deg, graph, n, path):
    m = count_edges(graph)
    in_deg, out_deg = CountInOutDegree(in_deg, out_deg, graph)
    
    if not HasEulerianPath(in_deg, out_deg, n):
        return -1
    #start = findStartNode(in_deg, out_deg, n)
    start = 1140
    path = dfs(start, out_deg, graph, path)
    
    if len(path) == m + 1:
        return path[::-1]
    
    return -1

def findStartNode(in_deg, out_deg, n):
    start = 0
    
    for i in range(n):
        if out_deg[i] - in_deg[i] == 1:
            return i
        if out_deg[i] > 0:
            start = i
    
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

def HasEulerianPath(in_deg, out_deg, n):
    start, end = 0, 0
    
    for i in range(n):
        if in_deg[i] - out_deg[i] > 1 or out_deg[i] - in_deg[i] > 1:
            return False
        elif in_deg[i] - out_deg[i] == 1:
            end += 1
        elif out_deg[i] - in_deg[i] == 1:
            start += 1
            
    return(start == 0 and end == 0) or (start == 1 and end == 1)


class EulerianCycleTest(unittest.TestCase):
    def test_count_edges(self):
        self.assertEqual(count_edges({0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}), 12)
        
    def test_has_eulerian_path(self):
        self.assertEqual(HasEulerianPath([1, 1, 2, 1, 1, 1, 2, 1, 1, 1], [1, 1, 2, 1, 1, 1, 2, 1, 1, 1], 10), True)
        
if __name__ == "__main__":
    #unittest.main()
    
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
                #print(tmp)
                nbr = int(tmp)
                graph[nbr] = []
                tmp = ''
              
    res = EulerianPath(graph)
    for node in res:
        print(f"{node}->", end = "")
    print()
    pass