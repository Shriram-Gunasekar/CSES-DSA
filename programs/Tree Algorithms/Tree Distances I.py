n = int(input())
x = []
adjmatrix = dict()
for i in range(n-1):
    x = input().split(' ')
    if int(x[0]) in adjmatrix:
        adjmatrix[int(x[0])].append(int(x[1]))
    else:
        adjmatrix[int(x[0])] = [int(x[1])]
    if int(x[1]) in adjmatrix:
        adjmatrix[int(x[1])].append(int[0])
    else:
        adjmatrix[int(x[1])] = [int(x[0])]
distance = dict()
for i in range(1,n+1):
    distance[i] = 0
def dfs(node, parent):
    for child in adjmatrix[node]:
        if child != parent:
            distance[node] += 1
            dfs(child, node)
for i in range(1,n+1):
    for j in adjmatrix[i]:
        dfs(j, i)
print(distance)


    
    
