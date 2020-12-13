print("\n\n ######WELCOME TO FORMULA 1#####")
print("\n Hey Racer..You have to complete a total of 305km (or more) to complete the race")
length=int(input("\n Enter the total length of current track(in Km): "))
ask=int(input("\n Have you just started the race ? \n press 1 for yes, Any other integer for no : "))
laps=int((305/length)+1)
totallen=int(laps*length)
if (ask == 1):
    print("\n\n Let's start the race. You have a long way to go. In total, you have to cover a distance of ",int(totallen),"km for which you have to complete ",laps," laps")
else:
    done=int(input("Please enter the number of km you have already completed : "))
    if(done >=(laps*length)):
        print("Hey racer, you have already completed the race. Please stop at the next stoppage!!")
    else:
        print("\n\n Hey racer, you have already covered ",done,"km and you just need to cover ",int((totallen)-done)," more km for which you have to complete",int(((totallen-done)/length)+1)," more tracks")

