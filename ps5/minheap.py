import math
from quicksort import swap
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
        if (key < self.A[i][0]):
            return None
        self.A[i][0] = key
        while(i > 0 and (self.A[self.parent(i)][0] > self.A[i][0])):
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

    def insert(self, key, node):
        self.A.append([-1, node])
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
