name = input('Enter your name: ')
print('WELCOME',name,'TO THIS ADVENTURE')

answer = input('You are on a dirt road, it has come to an end and you can go either left or right. Would you like to go (left/right) ').lower()
if answer == 'left':
    answer = input("Now you come to a river. you can walk around it or swim across? would you like to (walk/swim) ").lower()
    if answer == 'walk':
        print('you walked for many miles and ran out of water and you lost the game!')
    elif answer == 'swim':
        print('you swam across and eaten by an crocodile!')
        print("opps! you lose the game")
    else:
        print('Not a valid option, you lose the game!')

elif answer == 'right':
    answer = input("Now you come to a bridge. it looks wobbly do you want to cross it or want to go back? would you like to (cross/back) ").lower()
    if answer == 'cross':
        answer = input('you cross the bridge and meet a stranger would you like to talk to stranger? (yes/no) ').lower()
        if answer == 'yes':
           answer = input('you talk to stranger and they tells you a roadmap to reach the heaven. would to like to follow the roadmap? (yes/no) ').lower()
           if answer == 'yes':
               print('you follow and reach to heaven')
               print("Congratulation! YOU WON")
           elif answer == 'no':
               print('you cannot follow the path and you lost the way. and you lose!')
           else:
                print('Not a valid option, you lose!')



        elif answer == 'no':
            print('you ignore stranger and they are offended and you lose!')
        else:
            print('Not a valid option, you lose!')

    elif answer == 'back':
        print('you go back and back and come to dead end and you lose!')
    else:
        print('Not a valid option, you lose!')
else:
    print('Not a valid option, you lose!')
