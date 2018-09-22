
# coding: utf-8

# In[2]:


def PatternCount(Pattern, Text):
    import re
    return len(re.findall('(?='+Pattern+')', Text))

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if m == freq[key]:
            words.append(key)
    return words

def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return ''.join([complement[base] for base in Pattern])

def ReverseComplement(Pattern):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return "".join(complement[i] for i in Pattern[::-1])

def PatternMatching(Pattern, Genome):
    return [i  for i in range(len(Genome) - len(Pattern) + 1) if Genome[i:i + len(Pattern)] == Pattern]

def SymbolArray(Genome, symbol):
    array = {}
    ExtendedGenome = Genome + Genome[0:len(Genome)//2]
    for i in range(len(Genome)):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(len(Genome)//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:(n//2)]
    array[0] = PatternCount(Pattern=symbol, Text=ExtendedGenome[0:(n//2)])
    for i in range(1,n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] -= 1
        if ExtendedGenome[i+ (n//2) -1] == symbol:
            array[i] += 1
    return array

def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
    return skew

def SkewArray_Map(Genome):
    import matplotlib.pyplot as plt
    import numpy as np
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
    position = np.linspace(0, len(skew), len(skew))
    return plt.plot(position, skew)

def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    values = min(skew)
    return [i for i in range(len(Genome)) if values == skew[i]]

def ApproximatePatternMatching(Text, Pattern, d):
    return [i for i in range(len(Text) - len(Pattern) + 1) if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d]

def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance
