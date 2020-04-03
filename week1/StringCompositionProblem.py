import unittest

def StringCompositionProblem(text, k):
    n = len(text)
    res = []
    
    for i in range(n - k + 1):
        res.append(text[i:i + k])
               
    return res

class StringCompositionTest(unittest.TestCase):
    
    def test_string_composition_problem(self):
        self.assertEqual(StringCompositionProblem('CAATCCAAC', 5), ['CAATC','AATCC','ATCCA','TCCAA','CCAAC'])
        
        
        
if __name__ == "__main__":
    unittest.main() 
    
    pass