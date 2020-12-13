odds = [1,3,5,7]
length = len(odds)
i=0
ii=0

while ii < length :
    if(odds[i]%odds[i]==0):
        print(odds[i],"is divisible by",odds[i+1])
    else:
        print(odds[i],"is not divisible by",odds[i+1])


    i +=1
    ii+=1

#while odds>6
 # /  print(odds)


