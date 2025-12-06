from itertools import groupby

result= []

s= input().strip()

for key, group in groupby(s):
    count= len(list(group))
    result.append(f"({count}, {key})")

print(" ".join(result))