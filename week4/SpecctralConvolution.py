from collections import Counter
from CyclopeptideScoring import *


def SpectralConvolution(spectrum):
    result = []
    for i, elem in enumerate(spectrum):
        for j in range(i):
            result.append(spectrum[i] - spectrum[j])
    return result


def find_range(m, spectrum):
    spectrum.sort() 
    tmp1 = SpectralConvolution(spectrum)
    tmp2 = []
    # Find 
    for elem in tmp1:
        if elem <= 200 and elem >= 50:
            tmp2.append(elem)
            
    convolution = Counter(tmp2)
    new_spectrum = convolution.most_common(m)
    last_frequency = new_spectrum[-1][1]
    new_spectrum = [k for k, v in dict(convolution).items() if v >= last_frequency]
    new_spectrum.sort()
    
    
    aminoAcidMass = {f"{str(i)}": elem for i, elem in enumerate(new_spectrum)}
    Alphabet = [f"{str(i)}" for i, _ in enumerate(new_spectrum)]
    
    return Alphabet, aminoAcidMass


def ConvolutionPeptideSequencing(n, spectrum):
   
    peptide = LeaderboardCyclopeptideSequencing(spectrum, n)
    
    return peptide

if __name__ == "__main__":
    lines = open("tmp2.txt", "r").readlines()
    aux = ""
    spectrum = []
    m = int(lines[0][:-1])
    print(m)
    n = int(lines[1][:-1])
    print(n)

    for nbr in lines[2]:
        if nbr != " " and nbr != "\n":
            aux += nbr
        else:
            spectrum.append(int(aux))
            aux = ""
    
    spectrum.sort()
    
    #res1, res2 = find_range(m, spectrum)
    #print(res1)
    #print(res2)
    x = ConvolutionPeptideSequencing(n, spectrum)
    for elem in x:
        for aux in elem:
            print(aux, end = '-')
    print()
    '''
    f = open("result.txt", "w")
    
    for x in res:
        if x != 0:
            f.write(f"{str(x)} ")
    f.close()
    print("ok")
    print(Counter(res))'''
    pass