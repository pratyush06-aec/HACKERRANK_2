def count_string(string, sub_string):
    count= 0
    for i in range(len(string)- len(sub_string)+ 1):
        if(string[i:i+ len(sub_string)]== sub_string):
            count+= 1

    return count
    
s= str(input("Enter a string: ").split())
sub_s= "sdk"
print(count_string(s, sub_s))