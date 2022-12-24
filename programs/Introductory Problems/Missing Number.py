n = int(input())
l = input().split()
l = {int(i) for i in l}
s = set(range(1, n+1))
for i in s:
    if i not in l:
        print(i)
        break