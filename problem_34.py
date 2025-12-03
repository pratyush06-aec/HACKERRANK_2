n= int(input())
word_count= {}
order= []

for _ in range(n):
    word= str(input().strip())
    if word not in word_count:
        word_count[word]= 0
        order.append(word)
    word_count[word]+= 1

print(len(word_count))
print(*[word_count[word] for word in order])