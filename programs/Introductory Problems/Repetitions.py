s = input()
temp = s[0]
max = 0
count = 0
for i in range(len(s)):
    if s[i] == temp:
        count += 1
    else:
        count = 1
        temp = s[i]
    if count > max:
        max = count
print(max)