def minion_game(string):
    length= len(string)
    stuart_score= 0
    kevin_score= 0
    vowel= "AEIOU"
    for i in range(length):
        if(string[i] in vowel):
            kevin_score+= length-i

        else:
            stuart_score+= length-i

    if(stuart_score>kevin_score):
        print("Stuart", stuart_score)

    elif(stuart_score<kevin_score):
        print("Kevin", kevin_score)

    else:
        print("Draw")

s= str(input("Enter the word: "))
print(minion_game(s))