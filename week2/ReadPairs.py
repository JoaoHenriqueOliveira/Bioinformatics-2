class Pair:
    def __init__(self, kmer1, kmer2, k = -1, d = -1):
        self.kmer1 = kmer1
        self.kmer2 = kmer2
        self.k = k
        self.d = d
        
    def __lt__(self, other): #for sorting lt = less than
         return self.kmer1 < other.kmer1
    
    def __repr__(self): #for printing right
        return "(" + str(self.kmer1) + "|" + str(self.kmer2) + ")"
        
def ReadPairs(text, k, d):
    result = []
    n = len(text)
    for i in range(n - k - d):
        kmer1 = text[i:i + k]
        kmer2 = text[i + k + d: i + 2*k + d]
        pair = Pair(kmer1, kmer2, k, d)
        result.append(pair)
    
    result.sort()
    return result

if __name__ == "__main__":
    res = ReadPairs("TAATGCCATGGGATGTT", 3, 2)
    for pair in res:
        print(pair, end = ' ')
    print()
    pass