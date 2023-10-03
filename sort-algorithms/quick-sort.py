def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp 
    i+=1
    temp = A[i]
    A[i] = x
    A[r] = temp
    
    return i

def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p, q-1)
        quick_sort(A,q+1,r)
        
l = [6,3,2,1,3,8,7,5]

quick_sort(l, 0, 7)

print(l)