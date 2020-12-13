'''Hello, i am submitting this after the exam because there was a very minor error
in my code which i missed during testing just bceause of the shortage of time. i have done a very
minor edit in lenght of word. As i have applied the code to solve the issue of even and odd
lenght of code, whenever it was odd lenght of code, it adds 1 to the lenght which leads to
index range error in for x in range(0, lngth_word): as range gets out of lenght so
i have solved the error by giving a different variable. you can compare the codes.
this version is error free and working flawlessly 
'''

##no idea why an error wa coming just coz of comments in 40th line so did some commenting with #
#and you might see my name in previous files because..well, sometimes you have to share even when u dont want to and 
# i hope u will understand why writting name at such place matters 
import random

#made by dinkartaneja 1911380
value=int(input("\n---------Would you like to play Hangman--------- \n Press 1 for yes \t 0 for No \t"))

#if user choose not to play
if (value==0):
    print("\n\n You choose not to play!! \n See you next time\n ") 



#if user choose to play
elif(value==1):
#made by dinkartaneja 1911380
    print("\n Lets play Hangman \n\n")
    


    listOfWords=["python","scripting","mississippi","umbrella","examination","sunlight","teacher","morning","goodluck"]
#made by dinkartaneja 1911380
    guess_word = []
    word = random.choice(listOfWords)
    lngth_word = len(word)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []
    #odd even issue solved

#i have made an edit here by new variable lngth.. 
#1. doing so, now it show odd and even number of charcters in line 47. Previously it just showed even(it add 1 if its odd). 
#2. not it doesnt create error of out of range in line 67,68.


    if (lngth_word%2==0):
        length_word = lngth_word
    else:
        length_word = lngth_word+1

#using each char in word
    for character in word:
        guess_word.append("_")
#telling count of everything
    print("\nThe word you have to guess has",lngth_word, "characters\n")
    print(guess_word)
#made by dinkartaneja 1911380
    gus=(length_word)/2
    guess_taken = 1
#loops of everything
    while guess_taken <= (length_word)/2:

        print("\nYou can make upto ",gus,"guesses")
        guess = input("Pick a letter \n").lower()
        #made by dinkartaneja 1911380
        if not guess in alphabet:
            print("Enter a letter from a-z alphabet's only")
        elif guess in letter_storage:
            print("You have already guessed that letter! Please choose a different alphabet")
        else: 

            letter_storage.append(guess)
            if guess in word:
                print("You guessed the right aphabet")
                for x in range(0, lngth_word):
                    if word[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)
#made by dinkartaneja 1911380
                if not '_' in guess_word:
                    print("Congratulations!! You had",gus," attempts left but you had already won the Game!!")
                    print("\n\n   ¯\_(~_~)_/¯")
                    print("      |   | ")
                    print("      /   \ \n\n")
                    print("Saved")
                    break
            else:
                print("The letter is not in the word. Try again!")
                gus -= 1
                guess_taken += 1
            
                if guess_taken > (length_word)/2:
                    print("Sorry, You have made all the gusses. The word was",word)
                    print("\n\n   (-_-)")
                    print(" --|  |-- ")
                    print("   /  \ \n\n")
                    print("Man hanged")





#if user choose anythinf else from 0 and 1
else:
    print("\nChoose between 0 and 1 only\n")








    first_pass = True
while first_pass or condition:
    first_pass = False
    do_stuff()