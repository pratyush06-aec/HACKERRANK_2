countries= set()
limit= int(input())

for _ in range(limit):
    countries.add(str(input().strip()))

print(len(countries))