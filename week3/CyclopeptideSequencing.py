import collections

aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}
uniqueAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113, #'L': 113,
    'N': 114,
    'D': 115,
    'K': 128, #'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
UniqueAlphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

def NumberCyclicSubpeptides(n):
    if n <= 0:
        return 0
    else:
        return n*(n - 1)
    
def LinearSpectrum(peptide):
    n = len(peptide)
    prefix_mass = [0 for i in range(NumberCyclicSubpeptides(n))]
    
    if n == 1:
        return [0, aminoAcidMass[peptide]]
    if n == 2:
        res = [0, aminoAcidMass[peptide[0]], aminoAcidMass[peptide[1]], CalculateMass(peptide)]
        res.sort()
        return res
        
    for i, amino in enumerate(peptide):
        for symbol in Alphabet:
            if amino == symbol:
                prefix_mass[i] = prefix_mass[i - 1] + aminoAcidMass[amino]

    linear_spectrum = []

    for i in range(n):
        for j in range(i+1, n + 1):
            linear_spectrum.append(abs(prefix_mass[j] - prefix_mass[i]))
    
    linear_spectrum.append(0)
    linear_spectrum.sort()
    
    return linear_spectrum

def CalculateMass(peptide):
    mass = 0
    for char in peptide:
        mass += aminoAcidMass[char]
    
    return mass

def CyclicSpectrum(peptide):
    n = len(peptide)
    CyclicSpectrum = []
    
    # 0 mass
    CyclicSpectrum.append(0)
    
    #Append mass of total peptide
    CyclicSpectrum.append(CalculateMass(peptide))
    
    #Append each amino acid's mass
    for char in peptide:
        CyclicSpectrum.append(CalculateMass(char))
            
    #Append each cyclic combinations' masses
    for w in range(2, n):
        peptide = peptide + peptide[w - 2]
        #print(peptide)
        n = len(peptide)
        for i in range(n - w + 1):
            sub_pep = peptide[i:i + w]
            mass = CalculateMass(sub_pep)
            CyclicSpectrum.append(mass)
    
    #Sort
    CyclicSpectrum.sort()
    return CyclicSpectrum
    
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def CountingPeptides(m):
    count = 0
    if m == 0:
        return 1
    if m < 0:
        return 0
    
    for amino in uniqueAcidMass:
        mass = uniqueAcidMass[amino]
        count += CountingPeptides(m - mass)

    return count

CountingPeptides = memoize(CountingPeptides)

def BFCyclopeptideSequencing(spectrum):
    
    pass

def consistent(parent_spectrum, son_spectrum):
           
    son = dict((i, son_spectrum.count(i)) for i in son_spectrum)
    dad = dict((i, parent_spectrum.count(i)) for i in parent_spectrum)
    
    for elem in son:
        if elem not in dad or son[elem] > dad[elem]:
            return False
        
    return True

def Expand(candidates):
    tmp = []
    for elem in candidates:
        for amino in UniqueAlphabet:
            tmp.append(elem + amino)
    return tmp

def CycloPeptideSequencing(spectrum):
    candidates = [""]
    final = []
    parent_mass = spectrum[-1]
   
    while len(candidates) != 0:
    #for k in range(3):
        candidates = Expand(candidates)
        aux = candidates.copy()
        #print(candidates)
        for x in aux:
            #if x == "IKW":
                #print(x)
            if CalculateMass(x) == parent_mass:
                #print(f"1: {x}")
                if collections.Counter(CyclicSpectrum(x)) == collections.Counter(spectrum) and x not in final:
                    final.append(x)
                    #print(f"2: {final}")
                candidates.remove(x)
                trash.append(x)
                
                
            elif not consistent(spectrum, LinearSpectrum(x)):
                candidates.remove(x)
                trash.append(x)
        
    return final

    
def NumberOfSubpeptides(n):
    
    return int(n * ((n + 1) / 2) + 1)

if __name__ == "__main__":
    #x = CountingPeptides(2000)
    #y = CountingPeptides(2050)
    #c = y / x
    #c = c ** (1/50)
    #print(c)
    #print(CyclicSpectrum("TAIM"))
    #print(LinearSpectrum("ATA"))
    #print(NumberOfSubpeptides(10592))
    '''el_dad = CyclicSpectrum("VKLFPWFNQY")
    el_son = CyclicSpectrum("VKY")
    print(consistent(el_dad, el_son))
    print(Expand(['G','A','S','P','V','T','C','I','N','D','K','E','M','H','F','R','Y','W']))
    print(CalculateMass("RHTIY"))'''
    #print(CountingPeptides(427))
    res = CycloPeptideSequencing([0, 113, 128, 186, 241, 299, 314, 427])
    print(res)
    
    '''test = CyclicSpectrum("ITTHF")
    print(test)'''
    #print(CalculateMass("DIAAG"))
    #res = CyclicSpectrum("NQEL")
    #print(res)
    #parent = CyclicSpectrum("VKLFPWFNQY")
    parent = [0, 113, 128, 186, 241, 299, 314, 427]
    son = LinearSpectrum("I")
   # print(Expand(['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']))
    #print(consistent(parent, son))
    #print(CyclicSpectrum("WKI"))
    #print(len(Expand(["A", "S"])))
    
    pass
