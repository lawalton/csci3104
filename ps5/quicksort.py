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
