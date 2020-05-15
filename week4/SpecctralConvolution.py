from collections import Counter

def SpectralConvolution(spectrum):
    result = []
    
    for i, elem in enumerate(spectrum):
        for j in range(i):
            result.append(spectrum[i] - spectrum[j])
            
     
    return result

if __name__ == "__main__":
    lines = open("tmp2.txt", "r").readlines()
    aux = ""
    spectrum = []
    for nbr in lines[0]:
        if nbr != " " and nbr != "\n":
            aux += nbr
        else:
            spectrum.append(int(aux))
            aux = ""
    #print(spectrum)
    spectrum.sort()
    print(spectrum)
    res = SpectralConvolution(spectrum)
    f = open("result.txt", "w")
    
    for x in res:
        if x != 0:
            f.write(f"{str(x)} ")
    f.close()
    print("ok")
    print(Counter(res))
    
    pass