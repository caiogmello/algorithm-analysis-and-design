def merge(A,p,q,r):
    N = 10000000000000
    n1 = q-p+1
    n2 = r-q
    L = [N]*(n1+1)
    R = [N]*(n2+1)
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]

    i=0
    j=0
    
    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

def merge_sort(A,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    

l2 = [1,4,6,1,2,7,15,12,10,9]

# merge(l,0,3,7)

merge_sort(l2,0,(len(l2)-1))

print(l2)         