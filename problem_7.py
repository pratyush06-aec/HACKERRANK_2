# HackerRank.com presents "Pythonist 2".

# a= str(input("Enter a string: "))

# for i in a:
#     if(i.upper()):
#         a.lower()
#         # print(a)

#     elif(i.lower()):
#         i.upper()
#         # print(a)

#     else:
#         print("You are alien!!!1")

# print(a)



def swapcase(s:str)-> str:
    return s.swapcase()

a= str(input("Enter a string: "))
print(swapcase(a))