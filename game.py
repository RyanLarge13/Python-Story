print('Welcome to my first game...')
name = input('What is your name?? ')
age = int(input('What is your age?? '))

isOlder = age >= 18
health = 10

if isOlder:
    print('Hello', name, 'You are old enough to play this game.')
    wantsToPlay = input('Do you want to play?? ')
    if wantsToPlay.lower() == 'yes':
        print('let us play!!')
        print('Keep in mind you are starting with', health, 'health')
        leftOrRight = input('First choice... Left or Right?? ')
        if leftOrRight.lower() == 'left':
            ans = input('Good job! You followed the path and came to a lake... What will you do? Swim across or swim around?? ')
            if ans.lower() == 'across':
                health -= 2
                print('You managed to get across, but you were bit by a fish and and you lost health, your health is now at', health)
            else:
                print('You went around and reached the other side of the lake.')
                ans = input('There is a house and a river... To which do you travel?')
                if ans.lower() == 'river':
                    health -= health
                    print('you fall in and die.. Health is now at', health)
                    print('Goodbye...')
                else: 
                    print('You have gone inside of the house stepped on a nail... Survived off of food for 2 months and died from tetnus.. You lose... Goodbye..')
        else:
            print('You are drowning! Do you not remeber how to swim?? You lose, Goodbye.')
    else: 
        print('You are welcome to close the game, but I warn you... If the game is closed  will be back to find you and your information has been stored..')
        leave = input('Are you sure you want to leave and take the risk?? ')
        if leave.lower() == 'yes':
            print('I will find you... Goodbye..')
        else: 
            print('Good, let us continue...')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('ERR')
            print('You attempted to close the game.. Someone will come find you shortly.. RUN!!!!')
else:
    print('You are not old enough to play this game', name)