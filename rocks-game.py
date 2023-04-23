import random
print ('--------------------------------------')
print ('Welcome to Rock-Scissors-Paper Game v1')
print ('--------------------------------------')
print()

player1 = input("Player 1, what is your name? ")
print()
player2 = "Computer"
print(f'{player1} versus {player2}')
print()

rolls = ['rock', 'paper', 'scissors']

def validate_roll(player):
    roll = input(f'{player}, choose your roll (rock,paper,scissors) ')
    roll = roll.lower().strip()
    while roll not in rolls:
        print(f'{player}, {roll} is not a roll')
        roll = input('Please choose a valid roll (rock, paper, scissors) ').lower().strip()
        print()
    return roll

roll1 = validate_roll(player1)

roll2 = random.choice(rolls)

result = {'rock':'scissors','paper':'rock','scissors':'paper'}

def check_winner(roll1,roll2):
    if roll1 == roll2:
        return "It's a tie"
    elif result[roll1] == roll2:
        return f'{player1} won the round'
    else:
        return "Computer won the round"
    
print(f'{player1} -> {roll1}')
print(f'{player2} -> {roll2}')
print()
print(check_winner(roll1,roll2))


