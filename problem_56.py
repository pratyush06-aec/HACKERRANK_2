s= input().strip()

def key(c):
    if(c.islower()):
        group= 0
        sub=0

    elif(c.isupper()):
        group=1
        sub=0

    else:
        group= 2
        sub=0

        sub= 0 if(int(c)%2==1)  else 1

    return (group, sub, c)


print(''.join(sorted(s, key=key)))


# ((group) indicates the order, i.e, group=0 means lower, group=1 means upper, group=2 means digits)
# ((sub) indicates the order also, i.e, sub=0 means odd number and sub=1 means even number) 