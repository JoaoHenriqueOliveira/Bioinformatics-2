import unittest

def OverlapGraph(collection):
    graph = {}
    n = len(collection)
    
    for i in range(n):
        pattern = collection[i]
        adjacent = []
        aux = False
        for others in collection:
            if others[:-1] == pattern[1:]:
                adjacent.append(others)
                aux = True
        if aux:
            graph[pattern] = adjacent
                  
    return graph
             
if __name__ == "__main__":
    
    pass