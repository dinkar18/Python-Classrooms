list = [11, 22, 33, 44, 55,66,77,88,99,110,121,132,143,154,165,176,187,198,209,220]
#dinkarTaneja 1911380
print ("Original list")
print (list)


for i  in list:
	if(i%2 == 0):
	    list.remove(i)

#dinkarTaneja 1911380
print ("list after removing EVEN numbers")
print (list)