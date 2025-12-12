# x= int(input())
# nums= list(map(int, input().split()))

# all_positives= all(i>0 for i in nums)

# has_palindrome= any(str(i)== str(i)[::-1] for i in nums)


# print(all_positives and has_palindrome)



x= int(input())
nums= list(map(int, input().split()))

for i in nums:
    all_positives= all(i>0)

for i in nums:
    has_palindrome= any(str(i)==str(i)[::-1])


print(all_positives and has_palindrome)