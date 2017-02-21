import random
import quicksort as qs
from minheap import minHeap
from codeDictionary import dictionaryNode

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
    leafs = []
    for i in range(0, n):
        # Children nodes is an array of indecies in S that are children of a given node
        newNode = dictionaryNode(i, f[i], [])
        leafs.append(newNode)
        H.insert(newNode)
    for k in range(n+1,2*n):
        i = H.deleteMin()
        j = H.deleteMin()
        i.addToCode('0')
        j.addToCode('1')
        newNodeChildren = [i, j]
        newNodeChildren.extend(i.children)
        newNodeChildren.extend(j.children)
        newNode = dictionaryNode(k, j.freq + i.freq, newNodeChildren)
        H.insert(newNode)
        # Add to minheap
    T = []
    for i in range(0, len(leafs)):
        T.append([S[leafs[i].index], leafs[i].encoding])
    return T


# x is the string to encode, T is the root node of the huffmanTree
def encodeString(x,T):
    return 0

x = 'hereisateststring'
S, f = string2freq(x)
y = huffmanEncode(S,f)
