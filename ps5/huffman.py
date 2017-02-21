import random
import quicksort as qs
from huffmanTree import huffmanNode
from minheap import minHeap

def removeDuplicates(S, f):
    A = ''
    counter = 0
    for i in range(0, len(f)):
        A += chr(S[counter])
        counter += f[i]
    return A

def countStringFrequencies(S):
    prev = None
    counter = - 1
    f = []
    for i in range(0, len(S)):
        if (S[i] != prev):
            counter += 1
            f.append(0)
        f[counter] += 1
        prev = S[i]
    return f

def string2freq(x):
    S = bytearray(x)
    # S is a list of unique symbols in x in lexicographic order
    S = qs.quicksort(S, 0, len(S)-1)
    # f is a histogram of frequencies of symbols in x, same order as S
    f = countStringFrequencies(S)
    S = removeDuplicates(S, f)
    return S,f

def huffmanEncode(S,f):
    # Create empty H which is a min heap
    H = minHeap()
    n = len(f)
    for i in range(0, n):
        newNode = huffmanNode(S[i])
        H.insert(f[i], newNode)
    root = None
    S = list(S)
    for k in range(n+1, 2*n):
        f.append(-1)
        i = H.deleteMin()
        j = H.deleteMin()
        f[k-1] = f[i[0]] + f[j[0]]
        S.append(i[1].key() + j[1].key())
        root = huffmanNode(S[k-1], i[1], j[1])
        H.insert(f[k-1], root)
    return root

# x is the string to encode, T is the root node of the huffmanTree
def encodeString(x,T):
    return 0

x = 'hereisateststring'
S, f = string2freq(x)
y = huffmanEncode(S,f)
# Y should be the pointer to the root node of the dictionary
