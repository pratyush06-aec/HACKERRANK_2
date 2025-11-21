from collections import Counter

s= str(input())

count= Counter(s)

result= sorted(count.items(), key= lambda x: (-x[1], x[0]))

for character, frequency in result[:3]:
    print(character, frequency)