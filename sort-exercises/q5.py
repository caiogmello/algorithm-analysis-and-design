def compare(r1,r2):
    if r1['wt'] != r2['wt']:
        return r1['wt'] < r2['wt']
    elif r1['age'] != r2['age']:
        return r1['age'] > r2['age']
    elif r2['ht'] != r2['ht']:
        return r1['ht'] > r2['ht']
    else:
        return r1['name'] > r2['name']

def bubble_sort(lst):
    for i in lst:
        for j in range(len(lst) -1):
            if(compare(lst[j], lst[j+1])):
                lst[j], lst[j+1] = lst[j+1], lst[j]


t = int(input())

count = 1

for i in range(t):
    n, m = map(int, input().split())

    lst = []
    
    for j in range(n):
        name, wt, age, ht = input().split()
        d = {}
        
        d['name'] = name
        d['wt'] = int(wt)
        d['age'] = int(age)
        d['ht'] = float(ht)
        
        lst.append(d)
        
    bubble_sort(lst)
    
    print('CENARIO {' + f'{count}' + '}')
    count+=1
    
    for i in range(m):
        r = lst[i]['name']
        print(f'{i+1} - {r}')
    
       
     