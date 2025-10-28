def print_full_name(name):
    return " ".join(i.capitalize() for i in name.split(" "))
    
s= str(input())
print(print_full_name(s))