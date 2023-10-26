def bubble_sort(lst):
  for i in lst:
    for j in range(len(lst) - 1):
        if lst[j]['color'] > lst[j + 1]['color']:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        elif lst[j]['color'] == lst[j + 1]['color']:
            if lst[j]['size'] < lst[j + 1]['size']:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif lst[j]['size'] == lst[j + 1]['size']:
                if lst[j]['name'] > lst[j + 1]['name']:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    

start = True

while(True):
    n = int(input())
    if(n==0):
        break
    
    lst = []
    
    if(not start):
        print()
    
    
    for i in range(n):
        d = {}
        
        name = input()
        color, size = input().split()
        
        d["name"] = name
        d["color"] = color
        d["size"] = size
        
        lst.append(d)
        
    bubble_sort(lst)
    
    for i in lst:
        print(i['color'], i['size'], i['name'])
                
    start = False
    
        
    