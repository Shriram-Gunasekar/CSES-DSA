n = int(input())
l = input().split(' ')
l = [ int(i) for i in l ]
d = dict()
for i in l:
    if i not in d:
        d[i] = True
    else:
        pass
print(len(d))