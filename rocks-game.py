print ('--------------------------------------')
print ('Welcome to Rock-Scissors-Paper Game v1')
print ('--------------------------------------')
print()

player1 = input("Player 1, what is your name? ")
print()
player2 = input("Player 2, what is your name? ")
print()

rolls = ['rock', 'paper', 'scissors']

def validate_roll(player):
    roll = input(f'{player}, choose your roll (rock,paper,scissors) ')
    while roll not in rolls:
        print(f'{player}, {roll} is not a roll')
        roll = input('Please choose a valid roll (rock, paper, scissors) ')
        print()
    return roll

roll1 = validate_roll(player1)

roll2 = validate_roll(player2)