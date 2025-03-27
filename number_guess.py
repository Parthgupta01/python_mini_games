import random

num = input("Enter any number ")
if num.isdigit():
     num = int(num)
     if num <= 0:
        print("Please enter number grater than 0 next time!")
        quit()
else:
    print('Please enter a digit next time')
    quit()
r = random.randint(0,num)
guesss = 0
while(True):
       guesss+=1
       guess = input("Make a guess: ")
       if guess.isdigit():
           guess = int(guess)
         
       else:
           print('Please enter a digit next time')
           continue
       
       if guess == r:
           print('you got it!')
           break
       else:
          if guess > r:
            print('you are above the number')
          else:
              print('you are below the number')

print('You got it in', guesss, "guesss")
       
