print("WELCOME TO MY COMPUTER QUIX!")
playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! let's play :)")
score =0

answer = input('What does CPU stands for? ')
if(answer.lower() == 'central processing unit'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

answer = input('did India won t20 worldcup2024? ')
if(answer.lower() == 'yes'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

answer = input('What does GUI stands for? ')
if(answer.lower() == 'graphical user interface'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

answer = input('What does RAM stands for? ')
if(answer.lower() == 'random access memory'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

answer = input('how many colour rainbow does? ')
if(answer.lower() == '7'):
    score+=1
    print("Correct!")
else:
    print('Incorrect!')

answer = input('What does OS stands for? ')
if(answer.lower() == 'operating system'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

answer = input('What does IIT stands for? ')
if(answer.lower() == 'indian institute of tecnology'):
    print("Correct!")
    score+=1
else:
    print('Incorrect!')

print("You got "+ str(score) + " questions correct! ")
print("You got "+ str((score/8) *100) + " % ")