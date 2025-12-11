# x, k= map(int, raw_input().split())
# p= input()
# print(p==k)

# The above is the (python-2) style code. Because the raw_user is does not perform the job of eval.


x, k= map(int, input().split())
p= eval(input())
print(p==k)