s1 = input("Enter a string: ")

d = {}

for ch in s1:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)