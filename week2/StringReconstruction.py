import unittest
from EulerianCycle import EulerianPath
import sys
sys.path.insert(0, '../week1')
from DeBrujinGraph import *
from StringCompositionProblem import PathToGenome

def StringReconstructionProblem(patterns):
    graph = DeBrujin(patterns)
    path = EulerianPath(graph)
    text = PathToGenome(path)
    
    return text

class string_reconstruction_test(unittest.TestCase):
    def string_reconstruction_problem_test(self):
        self.assertEqual(StringReconstructionProblem(["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]), "GGCTTACCA")
        
if __name__ == "__main__":
    #unittest.main()
    file = open("test.txt", "r").readlines()
    patterns = []
    for line in file:
        patterns.append(line[:-1])
    
    #print(patterns)
    print(StringReconstructionProblem(patterns))
    
    pass