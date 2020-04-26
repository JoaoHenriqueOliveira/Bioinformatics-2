from EulerianCycle import EulerianPath
import sys
sys.path.insert(0, '../week1')
from DeBrujinGraph import *
from StringCompositionProblem import PathToGenome

class Pair:
    def __init__(self, kmer1, kmer2, k = -1, d = -1):
        self.kmer1 = kmer1
        self.kmer2 = kmer2
        self.k = k
        self.d = d
        
    def __lt__(self, other): #for sorting lt = less than
         return str(self.kmer1)+str(self.kmer2) < str(other.kmer1) + str(other.kmer2)
    
    def __repr__(self): #for printing right
        return "(" + str(self.kmer1) + "|" + str(self.kmer2) + ")"
    
    
    def __eq__(self, other): #for comparison
        return isinstance(other, self.__class__) and self.kmer1 == other.kmer1 and self.kmer2 == other.kmer2

    def __hash__(self):
        return hash(self.kmer1) * hash(self.kmer2)
    
    def get_kmer1(self):
        return str(self.kmer1)
    
    def get_kmer2(self):
        return str(self.kmer2)
    
    def prefix(self):
        return str(self.kmer1[:-1]) + str(self.kmer2[:-1])
    
    def suffix(self):
        return str(self.kmer1[1:]) + str(self.kmer2[1:])
    
    def node_prefix(self):
        return Pair(str(self.kmer1[:-1]), str(self.kmer2[:-1]))
    
    def node_suffix(self):
        return Pair(str(self.kmer1[1:]), str(self.kmer2[1:]))
        
def ReadPairs(text, k, d):
    result = []
    n = len(text)
    for i in range(n - 2 * k - d + 1):
        kmer1, kmer2 = text[i:i + k], text[i + k + d: i + 2*k + d]
        pair = Pair(kmer1, kmer2, k, d)
        result.append(pair)
    
    result.sort()
    return result

def DeBrujin_pairs(pairs): #pairs: list of Pair's
    graph = {}
    
    for pair in pairs: #create all nodes in graph
        prefix = pair.node_prefix()
        suffix = pair.node_suffix()
        graph[prefix] = []
        graph[suffix] = []
    
    for node in graph: #add neighbors
        for pair in pairs:
            p = pair.node_prefix()
            if  p == node:
                s = pair.node_suffix()
                graph[node].append(s)
    
    return graph

def StringSpelledByPatterns(path, k, d):
    n = len(path)
    p_string = ""
    s_string = ""  
    for i in range(n):
        node_s = path[i]
        if i == 0:
            p_string += node_s.kmer1[:-1]
            s_string += node_s.kmer2[:-1]
        p_string += node_s.kmer1[-1]
        s_string += node_s.kmer2[-1]
       
    for i in range(k + d, len(p_string)):
        if p_string[i] != s_string[i - k - d]:
            return "there is no string spelled by the gapped patterns"   
    
    return p_string + s_string[-(k + d):]

def StringReconstruction(k, d, pairs):
    graph = DeBrujin_pairs(pairs)
    path = EulerianPath(graph)
    n = len(path)
    edges = []
    for i in range(n - 1):
        p_up = path[i].kmer1
        p_d = path[i].kmer2
        s_up = path[i + 1].kmer1
        s_d = path[i + 1].kmer2
        kmer1 = p_up + s_up[1:]
        kmer2 = p_d + s_d[1:]
        edge = Pair(kmer1, kmer2)
        edges.append(edge) 
    final = StringSpelledByPatterns(edges, k, d)
    
    return final


if __name__ == "__main__":
    #res = ReadPairs("TAATGCCATGGGATGTT", 3, 2)
    #for pair in res:
    #    print(pair, end = ' ')
    #print()
    
    #p = Pair("TAA", "GCC")
    #p1 = p.node_prefix()
    #p2 = p.node_suffix()
    #print(p)
    #print(p1) #TA|GC
    #print(p2)
    
    #pairs = [Pair("AG", "AG"), Pair("GC", "GC"), Pair("CT", "CT"), 
     #        Pair("TG", "TG"), Pair("GC", "GC"), Pair("CT", "CA")]
             #Pair("CA", "CT"), Pair("AG", "TG"), Pair("GC", "GC"), Pair("CT", "TA")]
    
    #graph = DeBrujin_pairs(pairs)
    #print(graph)
    #print(EulerianPath(graph))
    
    #path = [Pair("GACC", "GCGC"),Pair("ACCG", "CGCC"), Pair("CCGA", "GCCG"), Pair("CGAG", "CCGG"), Pair("GAGC", "CGGA")]
    
    #print("******************************************")
    #path = [Pair("AG", "AG"), Pair("GC", "GC"), Pair("CA", "CT")]
    #print(StringSpelledByPatterns(path, 4, 2))
    
    lines = open("test.txt", "r").readlines()
    k = 50
    d = 200
    pairs = []
    #print(lines[-1][:50])
    #print(lines[-1][51:-1])
    for line in lines:
        kmer1 = line[:k]
        kmer2 = line[(k+1):-1]
        node = Pair(kmer1, kmer2)
        pairs.append(node)
    tmp = StringSpelledByPatterns(pairs, k, d) 
    print(tmp)
        
    
    pass