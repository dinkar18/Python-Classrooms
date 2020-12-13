print("################QUIZ 1################\n\n")


print("##########Question 2##########\n")

m = int(input("Enter the month(between march to june only): "))
if(m>=3 and m<=6):
    if (m == 3):
        d = int(input("enter a day: "))
        if (d in range (21,30)):
            print("True")
        else:
            print("false")
    if (m == 4):     
        d = int(input("enter a day: "))  
        if (d in range (1,30)):
                print("True")
        else:
            print("false")
    if (m == 5):       
        d = int(input("enter a day: "))
        if (d in range (1,31)):
                print("True")
        else:
            print("false")
    if (m == 6):   
        d = int(input("enter a day: "))    
        if (d in range (1,20)):
                print("True")
        else:
            print("false")
else:
    print("Wrong month entered")