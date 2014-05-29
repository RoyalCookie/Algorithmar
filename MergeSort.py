import  math

def merge(A,p,q,r):
    n_1 = q-p+1
    n_2 = r-q
    L = tuple
    R = tuple
    for i in xrange(1, n_1):
        L[i] = A[p+i-1]
    for j in xrange(1, n_2):
        R[j] = A[q+j]
    L[n_1 + 1] = float("inf")
    R[n_2 + 1] = float("inf")
    i=1
    j=1
    for k in xrange(p, r):
        if(L[i] <= R[j]):
            i = i+1
        else:
            j = j+1

def merge_sort(A,p,r):
    if (p < r):
        q = ((p+r)//2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A,p,q,r)



listi = [12,53,21,24,65,45,87,26,42,48]

