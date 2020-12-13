##Function for reverse traingle
def opptrian(num):
    row=num
    while row>0: 
        space = num-row
        while space>0:
            #dinkarTaneja 1911380
            print(end=" ")
            space = space-1
        star = num-row-1
        while star<num-1:
            print("*",end=" ")
            star = star+1
        row = row-1
        print()

##Function for traingle
def trian(num):
    row = 0
    while row<num:
        space = num-row-1
        while space>0:
            #dinkarTaneja 1911380
            print(end=" ")
            space = space-1
        star = row+1
        while star>0:
            print("*", end=" ")
            star= star-1
        row=row+1
        print() 


##################################################################################
'''
first function is making reverse triangle
*****
 ***
  *

second function is making triangle

  *
 ***
*****


both 1 time make bow
2 time make candy and so on

'''
###################################################################################

a=0
num= int(input("Enter the length of width: "))
turn= int(input("Enter the number of turns(1 for bowtie, 2 for candy,): "))

'''
if turn == 1:
    opptrian(num)
    trian(num)

if turn == 2:
    opptrian(num)
    trian(num)
    opptrian(num)
    trian(num)
'''

#with while u can make spirals as well  but if u want only bow and candy, u can use if aswell.(but it wont work if u put 3 for turns)
#dinkarTaneja 1911380
while a <  turn:
    opptrian(num)
    trian(num)
    a = a+1