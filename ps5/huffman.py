import random 
import math
# Implementing a min-heap version of a priority key
class minHeap:
    A = []

    # Turn A into a min-heap 
    # https://courses.csail.mit.edu/6.006/fall10/handouts/recitation10-8.pdf
    # http://cs.stackexchange.com/questions/10203/increase-key-and-decrease-key-in-a-binary-min-heap
    def left(self,i):
        if (2*i <= (len(self.A)-1)):
            return (2*i)
        else:
            return 0 
    def right(self,i):
        if ((2*i+1) <= (len(self.A)-1)):
            return (2*i + 1)
        else:
            return 0
    def parent(self,i):
        if (i == 0):
            return 0 
        return int(math.floor(i/2))

    def decreaseKey(self, i, key):
        if (key < self.A[i]):
            print('damn!')
        self.A[i] = key
        while(i > 0 and (self.A[self.parent(i)] > self.A[i])):
            swap(self.A, i, self.parent(i))
            i = self.parent(i)
        return 0

    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (len(self.A)-1) and self.A[l] < self.A[i]):
            smallest = l
        else:
            smallest = i
        if (r <= (len(self.A)-1) and self.A[r] < self.A[0]):
            smallest = r
        if (smallest != i):
            swap(self.A, 0, smallest)
            self.minHeapify(smallest)
    
    def insert(self, key):
        self.A.append(-1)
        self.decreaseKey(len(self.A)-1,key)

    # Return min value in heap
    def getMin(self):
        if (len(self.A) > 0):
            return self.A[0]
        else:
            return -1 
    # Delete min value in heap 
    def deleteMin(self):
        if (len(self.A) < 0):
            return -1
        min = self.A[0]
        self.A[0] = self.A[len(self.A)-1]
        self.A.remove(self.A[len(self.A)-1])
        self.minHeapify(0)
        return min


def swap(A, i, j):
    key = A[i]
    A[i] = A[j]
    A[j] = key

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            swap(A, i, j)
    swap(A, i+1, r)
    return i+1

def quicksort(A,p,r):
    if (p < r):
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A
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
    S = quicksort(S, 0, len(S)-1) 
    # f is a histogram of frequencies of symbols in x, same order as S
    f = countStringFrequencies(S) 
    S = removeDuplicates(S, f)
    return S,f

def huffmanEncode(S,f):
    # Create empty H which is a min heap
    H = minHeap()
    for i in range(0, len(f)):
        H.insert(f[i])

def encodeString(x,T):
    return 0

x = ''
S, f = string2freq(x)
huffmanEncode(S,f)
