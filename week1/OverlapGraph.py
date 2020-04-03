import unittest

def OverlapGraph(collection):
    graph = {}
    n = len(collection)
    
    for i in range(n):
        pattern = collection[i]
        adjacent = []
        aux = False
        for others in collection:
            if others[:-1] == pattern[1:]:
                adjacent.append(others)
                aux = True
        if aux:
            graph[pattern] = adjacent
            
                    
    return graph

class OverlapGraphTest(unittest.TestCase):
    
    def test_overlap_graph(self):
        self.assertEqual(OverlapGraph(["ATGCG","GCATG","CATGC","AGGCA","GGCAT","GGCAC"]), {'GCATG': ['CATGC'], 'CATGC': ['ATGCG'], 'AGGCA': ['GGCAT', 'GGCAC'], 'GGCAT': ['GCATG']})
        
        
if __name__ == "__main__":
    unittest.main()
    #print(OverlapGraph(["ATGCG","GCATG","CATGC","AGGCA","GGCAT","GGCAC"]))
    #collection = []
    #f = open("test.txt", "r").readlines()
    
    #for line in f:
    #    collection.append("".join(line[:-1]))
        
    #res = OverlapGraph(collection)
    #print(res)
    #file = open('answer.txt', "w")
    
    #for key in res:
    #    file.write(f"{key} -> ")
    #    for elem in res[key]:
     #       file.write(f'{elem} ')           
      #  file.write("\n")
        
    #file.close()
    pass