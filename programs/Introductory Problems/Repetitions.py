s = input()
temp = s[0]
max = 0
count = 0
for i in s:
    if i == temp:
        count += 1
    else:
        temp = i
        if max < count:
            max = count
        count = 0
print(max)
        
