def merge_tools(string, k):
    chunk= len(string)//k
    for i in range(chunk):
        t_i= string[i*k:(i+1)*k]
        seen= set()
        u_i= []
        for ch in t_i:
            if ch not in seen:
                u_i.append(ch)
                seen.add(ch)
        print("".join(u_i))

line, n= str(input()), int(input())
print(merge_tools(line, n))