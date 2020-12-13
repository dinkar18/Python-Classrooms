i=int(input("Enter number of rows: "))
a=[]
#dinkarTaneja 1911380
for n in range(i):
    a.append([])
    a[n].append(1)
    for k in range(1,n):
        a[n].append(a[n-1][k-1]+a[n-1][k])
    if(i!=0):
        #dinkarTaneja 1911380
        a[n].append(1)
for n in range(i):
    print(end=" ",sep=" ")
    for k in range(0,n+1):
        print('{0:6}'.format(a[n][k]),end=" ",sep=" ")
    print()