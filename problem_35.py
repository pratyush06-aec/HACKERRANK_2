from collections import deque

d= deque()
r= int(input())

for _ in range(r):
    cmd= input().split()
    if(cmd[0]== "append"):
        d.append(int(cmd[1]))

    elif(cmd[0]== "pop"):
        d.pop()

    elif(cmd[0]== "popleft"):
        d.popleft()

    elif(cmd[0]== "appendleft"):
        d.appendleft(int(cmd[1]))

print(*d)