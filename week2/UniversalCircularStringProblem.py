from EulerianCycle import EulerianPath
import sys
sys.path.insert(0, '../week1')
from DeBrujinGraph import *
from StringCompositionProblem import PathToGenome


def base10_to_base2(nbr, k):
    result = ""
    while(nbr != 0):
        result += str(nbr%2)
        nbr = int(nbr/2)
    size = len(result)
    if size > k:
        return f"String bigger than {k}"
    if size < k:
        while len(result) != k:
            result += '0'
        
    return result[::-1]    
    
def generate_patterns(k):
    patterns = []
    cases = 2 ** k
    for i in range(cases):
        patterns.append(base10_to_base2(i, k))
    
    return patterns

def UniversalCircularString(k):
    patterns = generate_patterns(k)
    graph = DeBrujin(patterns)
    path = EulerianPath(graph)
    text = PathToGenome(path)
    return text[:-(k - 1)]

if __name__ == "__main__":
    #print(base10_to_base2(3, 3))
    #print(generate_patterns(3))
    print(UniversalCircularString(9))
    pass