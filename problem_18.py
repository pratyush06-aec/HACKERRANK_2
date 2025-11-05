from itertools import permutations

string, r= input().split()
r= int(r)

permutation= list(permutations(sorted(string), r))

for i in permutation:
    print("".join(i))