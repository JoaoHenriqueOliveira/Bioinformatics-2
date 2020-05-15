import unittest
from EulerianCycle import EulerianPath, MaximalNonBranchingPaths
import sys
sys.path.insert(0, '../week1')
from DeBrujinGraph import *
from StringCompositionProblem import PathToGenome

def StringReconstructionProblem(patterns):
    graph = DeBrujin(patterns)
    path = EulerianPath(graph)
    text = PathToGenome(path)
    
    return text

def ContigGenerationProblem(patterns):
    graph = DeBrujin(patterns)
    paths = MaximalNonBranchingPaths(graph)
    
    for i, edgge in enumerate(paths):
        path = ""
        aux = len(paths[i]) - 1
        for tmp, node in enumerate(paths[i]):
            path += node[:-1]
            if tmp == aux:
                path += node[-1]
        paths[i] = path  
    
    paths.sort()
    return paths
        
if __name__ == "__main__":
   
    '''file = open("test.txt", "r").readlines()
    patterns = []
    for line in file:
        patterns.append(line[:-1])
    
    #print(patterns)
    #print(StringReconstructionProblem(patterns))
    res = ContigGenerationProblem(patterns)
    f = open("tmp.txt", "w")
    for elem in res:
        f.write(elem + " ")
        
    f.close()
    print("ok")'''
    pass