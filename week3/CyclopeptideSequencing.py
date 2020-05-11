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

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

def numberSubpeptides(n):
    if n <= 0:
        return 0
    else:
        return n*(n - 1)
    
def LinearSpectrum(peptide):
    n = len(peptide)
    prefix_mass = [0 for i in range(numberSubpeptides(n))]
    
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
    

if __name__ == "__main__":
    pass
