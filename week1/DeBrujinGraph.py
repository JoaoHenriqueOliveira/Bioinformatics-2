import unittest

def DeBrujinGraph(k, text):
    k, n, dic = k - 1, len(text), {}
    res = [text[i:i + k] for i in range(n -  k + 1)]
    res.sort()
        
    for elem in res:
        dic[elem] = []
    
    for j in range(n - k):
        dic[text[j:j + k]].append(text[j + 1: j + k + 1])
        
    for key in dic:
        dic[key].sort()
    
    return dic

def DeBrujin(patterns):
    k = len(patterns[0])
    graph = {}
    
    for k_mer in patterns:
        graph[k_mer[0:(k - 1)]] = []
        graph[k_mer[1:k]] = []
    
    for node in graph:
        for k_mer in patterns:
            if k_mer[0: (k - 1)] == node:
                graph[node].append(k_mer[1:k])
    
    return graph

class DeBrujinGraphTest(unittest.TestCase):
    def test_de_brujin_graph(self):
        self.assertEqual(DeBrujinGraph(4, "AAGATTCTCTAAGA"), {"AAG": ["AGA","AGA"], "AGA": ["GAT"], "ATT": ["TTC"],
                                                              "CTA": ["TAA"], "CTC": ["TCT"], "GAT": ["ATT"], "TAA": ["AAG"], "TCT": ["CTA","CTC"],
                                                              "TTC": ["TCT"]})
   
if __name__ == "__main__":
    print(DeBrujin(["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]))
    #unittest.main()           
    pass


