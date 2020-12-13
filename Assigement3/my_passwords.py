import string
import random

def pwd_check(passwd):
    SpecialSym =['$', '@', '#', '%', '!', '^', '&', '*', '(' , ')'] 
    val = True
      
    if len(passwd) < 6: 
        print('\nINVALID PASSWORD (length should be at least 6)') 
        val = False
          
    if len(passwd) > 20: 
        print('\nINVALID PASSWORD (length should be not be greater than 8)') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('\nINVALID PASSWORD (Password should have at least one numeral)') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('\nINVALID PASSWORD (Password should have at least one uppercase letter)') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('\nINVALID PASSWORD (Password should have at least one lowercase letter)') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('\nINVALID PASSWORD (Password should have at least one of the symbols ! ^ * ( ) $ @ #)') 
        val = False
    else:
        print("\nwooohooo!!!!You have entered a Valid Password\n") 
  


def random_pwd(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    print("A good password for you could be: ",''.join(random.choice(chars) for _ in range(size)))

option=int(input("\n1.Checking whether or not your password is “good” \n2.Generating a random password instead.\n"))
if (option == 1):
    passwd = input("\nPlease enter your password: ")
    pwd_check(passwd)
elif (option == 2):
    print(random_pwd(int(input('\nHow many characters would you like to have in your password ?\n'))))
else:
    print("\nyou have to choose between 1 and 2 only")
    