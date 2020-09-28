import sys
sys.path.insert(0, '../week3')
from CyclopeptideSequencing import *
from collections import Counter


def memoize(f):
    memo = {}

    def helper(x, spectrum):
        if x not in memo:
            memo[x] = f(x, spectrum)
        return memo[x]
    return helper


def CycloPeptideScoring(peptide, spectrum):
    count = 0
    theorical = CyclicSpectrum(peptide)
    theorical =Counter(theorical)# {i: theorical.count(i) for i in theorical}
    spectrum = Counter(spectrum) # {i: spectrum.count(i) for i in spectrum}

    for elem in theorical:
        if elem in spectrum:
            count += min(theorical[elem], spectrum[elem])

    return count


CycloPeptideScoring = memoize(CycloPeptideScoring)


def LinearPeptideScoring(peptide, spectrum):
    count = 0
    theorical = LinearSpectrum(peptide)
    theorical = Counter(theorical) # {i: theorical.count(i) for i in theorical}
    spectrum = Counter(spectrum) # {i: spectrum.count(i) for i in spectrum}

    for elem in theorical:
        if elem in spectrum:
            count += min(theorical[elem], spectrum[elem])

    return count


LinearPeptideScoring = memoize(LinearPeptideScoring)


def LeaderboardCyclopeptideSequencing(spectrum, n):
    LeaderBoard = [""]
    LeaderPeptide = ""
    parentMass = max(spectrum)
    nbr = []
    # memo = []
    var1 = -int(1e9)
    # var2 = 0
    while len(LeaderBoard) != 0:
        LeaderBoard = Expand(LeaderBoard)
        aux = LeaderBoard.copy()
        for elem in aux: 
            if CalculateMass(elem) == parentMass:
                score = CycloPeptideScoring(elem, spectrum)

                if score > CycloPeptideScoring(LeaderPeptide, spectrum):
                    LeaderPeptide = elem
                if score > var1:
                    nbr = []
                    nbr.append(elem)
                    var1 = score
                elif score == var1:
                    nbr.append(elem)
                
                #print(f"{elem} -- {score}")
                
            elif CalculateMass(elem) > parentMass:
                LeaderBoard.remove(elem)

        LeaderBoard = Trim(LeaderBoard, spectrum, n)
    
    
    #for elem in nbr:
     #   memo.append(numberfy(elem))
    #memo[-38:] 
    return numberfy(LeaderPeptide) 


def Trim(leaderboard, spectrum, n):
    size = len(leaderboard)
    LinearScores = [0 for i in range(size)]

    for i, elem in enumerate(leaderboard):
        LinearScores[i] = LinearPeptideScoring(elem, spectrum)

    leaderboard = [peptide for _, peptide in sorted(
        zip(LinearScores, leaderboard))]
    leaderboard = leaderboard[::-1]
    LinearScores.sort()
    LinearScores = LinearScores[::-1]

    for i in range(n, size):
        if LinearScores[i] < LinearScores[n - 1]:
            leaderboard = leaderboard[:i]
            return leaderboard

    return leaderboard


if __name__ == "__main__":

    ''' 
    lines = open("tmp.txt", "r").readlines()
    n = int(lines[2][:-1])
    #print(n)
    aux = ""
    seq = []
    for char in lines[1]:
        if char != " ":
            aux += char
        if char == " " or char == "\n":
            seq.append(int(aux))
            aux = ""
    #print(seq)

    leaderboard = []
    aux = ""
    for char in lines[0]:
        if char != " " and char != "\n":
            aux += char
        else:
            leaderboard.append(aux)
            aux = ""

    #print(leaderboard)

    #leaderboard = ["LAST", "ALST", "TLLT", "TQAS"]
    #spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
    #n = 2

    res = Trim(leaderboard, seq, n)

    for elem in res:
        print(elem, end = " ")
    print()

    '''
    #n = 10
    #seq = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]

    
    lines = open("tmp2.txt", "r").readlines()
    n = int(lines[0][:-1])
    print(n)
    aux = ""
    spectrum = []
    for nbr in lines[1]:
        if nbr != " " and nbr != "\n":
            aux += nbr
        else:
            spectrum.append(int(aux))
            aux = ""
    print(spectrum)
    res = LeaderboardCyclopeptideSequencing(spectrum, n)
    print(res)
    
    pass
