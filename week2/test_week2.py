import unittest
from EulerianCycle import *
from StringReconstruction import *

class week2_test(unittest.TestCase):
     
    def test_count_edges(self):
        self.assertEqual(count_edges({0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}), 12)
        
    def test_has_eulerian_path(self):
        self.assertEqual(HasEulerianPath([1, 1, 2, 1, 1, 1, 2, 1, 1, 1], [1, 1, 2, 1, 1, 1, 2, 1, 1, 1]), True)
        
    def string_reconstruction_problem_test(self):
        self.assertEqual(StringReconstructionProblem(["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]), "GGCTTACCA")
    
if __name__ == "__main__":
    unittest.main()