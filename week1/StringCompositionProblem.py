import unittest

def StringCompositionProblem(text, k):
    n = len(text)
    res = []
    
    for i in range(n - k + 1):
        res.append(text[i:i + k])
               
    return res

def PathToGenome(path):
    text = ''
    text += path[0]
    
    for i in range(1, len(path)):
        text += path[i][-1]
    
    return text  

class StringCompositionTest(unittest.TestCase):
    
    def test_string_composition_problem(self):
        self.assertEqual(StringCompositionProblem('CAATCCAAC', 5), ['CAATC','AATCC','ATCCA','TCCAA','CCAAC'])
    
    def test_path_to_genome(self):
        self.assertEqual(PathToGenome(['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']), "ACCGAAGCT")
        
if __name__ == "__main__":
    unittest.main()
    
    pass