import unittest
from DeBrujinGraph import *
from OverlapGraph import *
from StringCompositionProblem import *

class test_week1(unittest.TestCase):
    
    def test_de_brujin_graph(self):
        self.assertEqual(DeBrujinGraph(4, "AAGATTCTCTAAGA"), {"AAG": ["AGA","AGA"], "AGA": ["GAT"], "ATT": ["TTC"],"CTA": ["TAA"], "CTC": ["TCT"], "GAT": ["ATT"], 
                                                              "TAA": ["AAG"], "TCT": ["CTA","CTC"],"TTC": ["TCT"]})
    def test_overlap_graph(self):
        self.assertEqual(OverlapGraph(["ATGCG","GCATG","CATGC","AGGCA","GGCAT","GGCAC"]), 
                         {'GCATG': ['CATGC'], 'CATGC': ['ATGCG'], 'AGGCA': ['GGCAT', 'GGCAC'], 'GGCAT': ['GCATG']})
     
    def test_string_composition_problem(self):
        self.assertEqual(StringCompositionProblem('CAATCCAAC', 5), ['CAATC','AATCC','ATCCA','TCCAA','CCAAC'])
    
    def test_path_to_genome(self):
        self.assertEqual(PathToGenome(['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']), "ACCGAAGCT")
      
if __name__ == "__main__":
    unittest.main()