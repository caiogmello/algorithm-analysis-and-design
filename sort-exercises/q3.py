def compare(t1, t2):
    if t1['points'] != t2['points']:
        return t1['points'] < t2['points']
    elif cesta_avg(t1['pro'], t1['contra']) != cesta_avg(t2['pro'], t2['contra']):
        return cesta_avg(t1['pro'], t1['contra']) < cesta_avg(t2['pro'], t2['contra'])
    elif t1['pro'] != t2['pro']:
        return t1['pro'] < t2['pro']
    
    return t1['id'] > t2['id']

def bubble_sort(lst):
    for i in lst:
        for j in range(len(lst)-1):
            if compare(lst[j], lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]


def cesta_avg(pro, contra):
    if contra == 0:
        return pro
    else:
        return pro/contra
    
    
start = True
instance = 1

while True:
    n = int(input())
    
    if(n==0):
        break
    
    lst = [{'id': 0,'points': 0, 'active': False, 'pro': 0, 'contra': 0} for _ in range(100)]

    if(not start):
        print()
    
    for i in range(n*(n-1)//2):
        id1, p1, id2, p2 = map(int, input().split())
                
        lst[id1-1]['active'] = True

        lst[id2-1]['active'] = True
        
        lst[id1-1]['id'] = id1
        lst[id2-1]['id'] = id2
        
        lst[id1-1]['pro'] += p1
        lst[id1-1]['contra'] += p2
        lst[id2-1]['pro'] += p2
        lst[id2-1]['contra'] += p1
        
        if p1 > p2:
            lst[id1-1]['points'] += 2
            lst[id2-1]['points'] += 1
        else:
            lst[id2-1]['points'] += 2
            lst[id1-1]['points'] += 1
        


    teams = []

    for i in lst:
        if(i['active']):
            teams.append(i)
            
    bubble_sort(teams)
    
    
    print(f'Instancia {instance}')
    instance+=1
    for i in range(len(teams)-1):
        print(teams[i]['id'], end=' ')
    print(teams[len(teams)-1]['id'])
        
    start = False
        
        
        
        
        
        
