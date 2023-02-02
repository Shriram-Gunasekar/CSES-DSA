n = int(input())
if sum(range(n+1)) % 2 == 0:
    print("YES")
    a = []
    b = []
    if n % 2 == 1:
        count = 0
        for i in range(1, n+1):
            if i % 4 in (1,2):
                a.append(i)
            else:
                b.append(i)
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)
    else:
        for i in range(1, n+1):
            if i % 4 in (0,1):
                a.append(i)
            else:
                b.append(i)
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)
else:
    print("NO")

