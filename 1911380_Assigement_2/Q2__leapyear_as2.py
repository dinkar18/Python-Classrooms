''' def is_leapyear(i):
    while (i%4) == 0 and (i%400) == 0:
        return (bool(True))
    else:
        return (bool(False))

####################################################
print("\n +++++++++++++  Leap year checker  +++++++++++++ \n\n")

year=int(input("Enter the year you want to check: "))

print(is_leapyear(year))
##########################################
'''

####function


def isLeapYear(year):
    return ((year%4==0 and year%100 !=0) or (year%400==0))

#############################################################
#dinkarTaneja 1911380
print("\n +++++++++++++  Leap year checker  +++++++++++++ \n\n")
year=int(input("Enter the year you want to check: "))
print(isLeapYear(year))