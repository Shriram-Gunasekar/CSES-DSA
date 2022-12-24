n = int(input())
l = input().split(' ')
l = [ int(i) for i in l ]
h = 0
if(n>1): 
    for i in range(n-1):
        if l[i] > l[i+1]:
            h += l[i] - l[i+1]
            l[i+1] = l[i]
        else:
            pass
print(h)