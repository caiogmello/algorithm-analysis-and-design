def swaps(vagoes, tam):
    swaps = 0
    for i in range(tam):
        for j in range(i+1, tam):
            if vagoes[i] > vagoes[j]:
                swaps += 1
    
    return swaps

n = int(input())

for i in range(n):
    l = int(input())
    vagoes = [int(x) for x in input().split()]
    s = swaps(vagoes, l)
    print(f'Optimal train swapping takes {s} swaps.')
