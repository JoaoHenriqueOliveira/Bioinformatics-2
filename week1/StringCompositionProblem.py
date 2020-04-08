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

def base10_base2(k):
    tmp = ''
    
    while k != 0:
        tmp += str(k%2)
        k = int(k/2)
    tmp = tmp[::-1]
    while len(tmp) != 4:
        tmp = '0' + tmp
        
    return tmp

def k_universal(numbers):
    pass

class StringCompositionTest(unittest.TestCase):
    
    def test_string_composition_problem(self):
        self.assertEqual(StringCompositionProblem('CAATCCAAC', 5), ['CAATC','AATCC','ATCCA','TCCAA','CCAAC'])
    
    def test_path_to_genome(self):
        self.assertEqual(PathToGenome(['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']), "ACCGAAGCT")
        
if __name__ == "__main__":
    unittest.main()
    
    #aux = []
    
    #for i in range(16):
    #    aux.append(base10_base2(i))
    #print(aux)
    
    #print(PathToGenome(aux))
    
    pass