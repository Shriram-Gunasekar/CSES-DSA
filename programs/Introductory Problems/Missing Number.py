n = int(input())
l = input().split()
l = [int(i) for i in l]
for i in range(1,len(l)+1):
    if i not in l:
        print(i)
        breakss