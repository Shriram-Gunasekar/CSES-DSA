n = input().split(' ')
x = int(n[1])
l = input().split(' ')
l = [ int(i) for i in l ]
flag = False
for i in range(n[0]):
    if x - l[i] in l:
        flag = True
        print(i+1, l.index(x-l[i])+1)
        break
if not flag:
    print("IMPOSSIBLE")


