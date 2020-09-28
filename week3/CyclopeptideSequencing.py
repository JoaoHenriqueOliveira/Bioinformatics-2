import collections
'''
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
    'I': 113,  # 'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,  # 'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}
'''
'''
aminoAcidMass = {f"{str(i - 50)}": i for i in range(50, 201)} # for all range of masses
uniqueAcidMass = {f"{str(i - 50)}": i for i in range(50, 201)} # for all range of masses
#Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
#UniqueAlphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
UniqueAlphabet = [f'{str(i - 50)}' for i in range(50, 201)] # for all range of masses
Alphabet = [f'{str(i - 50)}' for i in range(50, 201)] # for all range of masses
'''
aminoAcidMass = {'0': 50, '1': 55, '2': 71, '3': 73, '4': 81, '5': 87, '6': 97, '7': 99, '8': 101, '9': 113, '10': 115, '11': 116, '12': 125, '13': 127, '14': 128, '15': 131, '16': 147, '17': 162, '18': 165, '19': 168, '20': 186, '21': 200}
#{'0': 57, '1': 65, '2': 66, '3': 81, '4': 96, '5': 97, '6': 113, '7': 114, '8': 115, '9': 128, '10': 129, '11': 130, '12': 131, '13': 145, '14': 146, '15': 147, '16': 162, '17': 163, '18': 177, '19': 186, '20': 194}
uniqueAcidMass = {'0': 50, '1': 55, '2': 71, '3': 73, '4': 81, '5': 87, '6': 97, '7': 99, '8': 101, '9': 113, '10': 115, '11': 116, '12': 125, '13': 127, '14': 128, '15': 131, '16': 147, '17': 162, '18': 165, '19': 168, '20': 186, '21': 200}
Alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

UniqueAlphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']


def memoize(f):

    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def NumberCyclicSubpeptides(n):
    if n <= 0:
        return 0
    else:
        return n*(n - 1)


def CalculateMass(peptide):
    mass = 0
    for char in peptide:
        mass += aminoAcidMass[char]   
    return mass


CalculateMass = memoize(CalculateMass)


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
        #UniqueAlphabet
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


LinearSpectrum = memoize(LinearSpectrum)


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


CyclicSpectrum = memoize(CyclicSpectrum)


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
        candidates = Expand(candidates)
        aux = candidates.copy()
        for x in aux:
            if CalculateMass(x) == parent_mass:
                if collections.Counter(CyclicSpectrum(x)) == collections.Counter(spectrum) and x not in final:
                    final.append(x)
                candidates.remove(x)
            elif not consistent(spectrum, LinearSpectrum(x)):
                candidates.remove(x)
                
    return numberfy(final)


def numberfy(peptides):
    res = []
    for peptide in peptides:
        tmp = []
        for char in peptide:
            tmp.append(aminoAcidMass[char])
        res.append(tmp)
    return res


def NumberOfSubpeptides(n):
    return int(n * (n + (n - 1) / 2) + 1)


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
    
    lines = open("tmp.txt", "r").readlines()
    aux = ""
    seq = []
    for char in lines[0]:
        if char != " ":
            aux += char
        if char == " " or char == "\n":
            seq.append(int(aux))
            aux = ""
    seq = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299,
            299, 301, 394, 396, 398, 400, 400, 497]
    res = CycloPeptideSequencing(seq)
    for elem in res:
        n = len(elem)
        for i, nbr in enumerate(elem):
            if i != n - 1:
                print(f"{nbr}-", end = "")
            else:
                print(nbr, end = " ")
    
    print()
    '''test = CyclicSpectrum("ITTHF")
    print(test)'''
    #print(CalculateMass("DIAAG"))
    #res = CyclicSpectrum("NQEL")
    #print(res)
    #parent = CyclicSpectrum("VKLFPWFNQY")
   # parent = [0, 113, 128, 186, 241, 299, 314, 427]
    #son = LinearSpectrum("I")
   # print(Expand(['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']))
    #print(consistent(parent, son))
    #print(CyclicSpectrum("WKI"))
    #print(len(Expand(["A", "S"])))
    
    pass
