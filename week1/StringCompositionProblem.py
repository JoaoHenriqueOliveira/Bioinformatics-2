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
    #unittest.main() 
    k = 100
    text = "AAGCGAATTGTGGGTGCAGCGCTAACCGGTGTCAGGTCGTAAGAGGCCGCCCTAATTGATCAGTTTCTCATAGCTAAGTCACTTTAGTATAGGGAGCTATAATGAAACACAGCTCTGCGATTAATTGCCACCTTGACCCATTTTCGTAGCATGGGGACTATAGCGGGCCGCTTTCCTTACTAGTATGAAAACGACCCGGGGGCGTTGTAAACCGCGCTCCGGTAGTTATAGTTTCTCCTCCGAGCAAATAGTTCCTGTACTGCTAGAACACCTTTTACTAACTCCGGCCAATAGCCTTGCGAGCGATAGTTCAGCCTGCAGGGGTAATGTATTTGTCTTGTCCTTTACATATTGGACTTCCATTACCTCTTGCCCTCTCATTCATTGTAGCCCCGGTATGTGGATAACTAGCAAAATCGTGGTGAAAACGGACACTGTGAGCAAGCCCAAGCTATCCCATAGCCGGTGTTATATCCCTAAGTAAACCATGGGATTTCCTAATGCGTCCGTCGTTGACATGCGAGGGCACCGCTGAGTAACCTGTCACGTCCAACCCTCATCTATGTCCCCTTCCGCTCGTGCTCATAAAACGGTCCGGGGCCTGAACTGCGACCGCCATTAGTTGGAGCCAAGGAACCTTACCGGGCAGAACACGATTTGCTACACTGACGGAGCGGGTTCTAATATAATGATTTATCTATGGAAGACATATAAAAGGTTTTGAGTCGTAGTAACCTATTTCTTCGCCTAGATTAAAAGGCATGCTAATGTCGCTGTATAGGAACACGTTGCGCCAATGATGCGTACGGGCAAGTGGCGTTCCCATTTTCATGGGGCTTAGCGTGCCACGGCTGCACGTGAGCTTGTAGCCTTTATCAAGTATTTGATCTTAAAGCGTTTACTAATAGTCAAGTTGGCTTCCAAAGCCTGCATAGGACGGGCAAGAGCGAGACCTCGTGTGGCTCACTATATTCCCCTCCCTAGGCTAGTACAGTTGCTAAGCGATCATATACGTTGTACCGCCTAGGAGACCTTGTATGTGACGGCTGCTAATCCACTATTGTCGGTTCAAGAATCGGGCGTGTATATAGTGGGTGTCCATAGACTTTGTACTCCTGGGCCGATTCCGAGCTCCGGTGGGCAACTCGCTAAGAAGTCACTTAATGGTTCCATTGTCTGCACTGTTTGACTGTCAGCCCAAGCAGTGCTGGTAGACATTGTGGGTGAGCAGTGGCTGCGGAAGTCCTTATCCAGGGCGTCCGGGAAGATGATCCGTTTTTCTGTGGTTCAGGCATCTATCGCTAACGTACCGGTTAAGTACCCGCGCCAAGTTACGACACCTACACTCTTCGCTGACTCCCGCTGTAGATAGTTATCGCAGGTACATTAGTGGCCAGGCTACCAAAATAAGCACGGACTGTGGAAATGGTTCTCTATCACACCGTATTCCCCAAACTCCAAGAAGGTGATCTTTCACGTGCGTGGATGGATTACATGGTTCGGAAATAATCGACGTTATTGCAGACGTCTTCAGCTCCAGTGAGTAGGTCCACCATTCCGTCTTTGGAGCGAAATGTTAGCCCTCCGGACACTGGTGAAAGTTGTGCTACGCATTGTTCTTAAACTATCTACCCCGCACGCTGAATTTATATATAAGGGTCCTAGGGATCCATTCCGTGCGCGACCTTAAGGTACGGAAAGGTGCCTGAATCTTTACTGTGTCAGATCCCCTCGTGGGTCCTAGGTGTATCGTGAACACCGGGCTCTACTCGGCGCGCCTACGTAATGTTCCTTTGCGACCGGGGAAATGTTAAGAGAGGAATACATGTAGGCTTAGGCTGGCCACGAGTAGTTCGATCCCGAATCAGGCAGCTGGGTCATTCTAACGACACTTAGGAATATGCCTGTATTCAGTAAATTTCCAGTCTAGATACACGGTCAAGTTTCAGAGAGCCTCGACGCCATCACAAGGTATAGTCTGAGACGTTCGCGTCGTGTCCAAACCCACGCTAAAGAGTAACGGTTGTCCCTTGCACTAGAATCCAACTCCACGTGTTGTCTACTATTCTTGCGGCGAAGCTGACGGACATCAAGTAACGTGGATCCACTTAGCACACCACGTAGCTATGATGGCGTTCTCGCATCGTGTGCGCGGGGTAATCCGCTATAACTTTGAGTTGTGCCATTACCCATTGAGCGCACGCGACTTCGTGAATTAAGCCTAAGATTAGTAAGGATATTGCTAGAACCGGTACACGGTTAGCCTTTCTAAGGTATGGTGTCTTTCTCTACATTTCAGGAAGAATGGTGCTTTTCCGAAGTAGCAGAGAGTTAGGCATATCCTCGCTGAATACGGCAGATCCCAAAGTAGGTAAATGATGTTTGGCACTCGCTAAGCGTTAGTAATGAGAGCGGCATTGTAGTGTCAGTCTACCATAGACTATCTCGCCCCCTGGTTCCAATTTCGTCAGTTGAGTTCAGTATAATGGACCCAGTCCTGGCAGACGTTGTGGAAAGAGTACACCCTCCGAACACTAGTGCACCGAAGATGTCATGGTTCTCAATAGAGACTACCTTATCGCTCACTCGCAGTAACCTTTCCCAAGTGGAGCAGACCTTTTCACTTCATGAGCGGGTCCCTTGATAGCTGCGGTTACCTCGCCCTTATAATGGGTGCTAGGAAACCCTTCACTGCATGATCCGTGGGCGCGCACTAGGAGAGCCTGTTAGATACCATGGGTGCGCTCCCGGGGGTCTCGCATTTAATGGTCCATAGCTGGGGACTTTAAACGGAAGTTCCTAAAACACAAGTGCCTCCGCTTGGAACGGTATGCATTACATGAAGTCTCAGAGTTGCGGCCACAGTTCTGTAGGTTCTCTGCGTGCACATGGAGCCAATTAATTTTATACAAGTTAAAGGCGAGCTATCGCAGTAATCACCGTAGGGCTTAACAGTCCATTTATGCCAGAGAGAGCTCGGAGTGGATCTAAAACCGAGAATTTAGAACTTCACATTGCTGAGAGAGGATTAACGATGCATTAGTGCGCTACTTTAACTGGACTCACCGTGGTGGCTCATATCACGAATCCATAGGGATAGCACGCCGATAAATGTTTTTGAGACGGGCCTGATCATACCCACCTCTTACGAACTGGAGACGACATACGGAAGCGCTCCAGACGCACCCGTTTTAATTGGCGGAACAGCTCGCGATTCCTACGCTCTATGCTGGAATTACAGCACACTAGAGAAGGATTATGAGCATGGTTGACGAAGGGTCCACCGTCAAGGTGGGCCATATCCAATGGGACGATCCTTTCGCGCACCTCCGCATAGTCCTACGTCGCCGGTCCCCTTGTAGCTATCAGCGGTTATCGACAGCCTGACCGCTTCATCCACGTCTCCGTTAAAATTTTCCAAGCGAAAGTATGTAAGGGTGGTCCTAAGATACCCTCGGGTACCCTCGGCCGTTCAGTTGTCGAAGTTGAGGTCCTGGTAGTTAACAGGTCAGTATGAGCACCACCGATCAACACATTATGGTCACCTCCACCTTTCATCCTGTATTCCCAACGAGATCTAAGAGGGAGATGTACCGGAAAGTCACGCACGACGGATGTTCTTTCTTGCATAGGCTCTCTCAATGTCAACTATCAGGACCTCACCTGTATAAAATCCACGACCGCGATCAATCAGTCCCGCCAGACCTTGGAGCGTGGTTTAAAGCATGTAAGGAGTAACTCGGCCAGACATCCGCCAGATAAGCGCTGGCACAAGTTGTGGTCGCATAGTACGGACCATACCATCTATGAACGTGCGAAGAGACTAATCCTGGAGACAGGACCAGGATAAAGGCTGACGCCCACACGTCTAATACACCCGGGACTTGCAGAAAAGTTGTCGTCTCTAACCCCCAGATGCAGGTACAGTTATGACGTCTTTAATTCGCAGTTTTTAGAGCGGAGTCCGGGAACTCGAAAATGTCGCATACGAGCCTCTGCATCACGCCGTGTGCCGGGCCCTTCGGGGATAACGCTCACACGCGTGCGGAATACACAGGAGTAGAATGCAAGAACTGACCATGGCGAAGCAAAGCATGGCATCTGGAAGAGCGTTACGGCATGTACAAGCCGGGCAACTGCGGAACAATTGGATCGTGCGGATTGTCTGGGGGTGCCCTTCGTTCGGCAAGGGCTCCATCGTTGGTTGTTCTAACTCAGTGTATGAATTTATCTTCAAAGTCCCCCTATGCACTCGTGCCTTCCCTATTGATGTATGTGAACACCTGGCAATCCGGGACGCAAACCAAGAGTCGTTGGTGCTCCGAGACGAATGGGGTACTTAGAGCGTCTATCACACTTCCTCGAATCGTGTTATCCTCTGGAGAGATTTAAGTATTTTTTTATAACCTCGGCACCACCCCGGGGGCAAACCCTTTCTGTTGCTATCTTCACTTCAGGATCGTACAGTGCGCAATCCACAGAGTCCTGAAAATTGGGCGTCCATTCAATCATCGGAGAACTTGCTGGCGACGGGGCCCATGCAATGATCCCGAGTACGCAACTACCGGGGCTCATCATACGTTTAAGGCGTCCTTTCCGTCTGTGTCTTTAGGCCCAACTAAACGATAGACGAGCTAGCGTTAATCGCGGAGTCTCGTACTGACAACATAAGTATTGGGAGATCGTCTTAGCCAGGACGGGCATTCCGGTGACCAACCCGTGGCCATTAATTGAAAATAGCCGTAGTAGGCCCCGAGTTGGCGCCTGATCCGCGCCTGATGGCACTCATTTTGCCACTCCGTTTTGTCGGCTCCTTGCAGAATATCCCGCTGAGAGTTAATACCGTTGTAATGGCCAATGGTTAATGACCAATAATTTACATCTCCGATCTGGCATTTAGATGAGAATTTAAAATCTACTCTGTGTGACTTAAATACATATTCACAGTCCAGTGTAAATACTGCGAGTTATTAGATCCATTAGTGTGGCTCTACCCAAGT"
    res = StringCompositionProblem(text, k)
    f = open("test.txt", "w")
    
    for k_mer in res:
        f.write(k_mer+'\n')
    print("ok")
    f.close()
    
    
    pass