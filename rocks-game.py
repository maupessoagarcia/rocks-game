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
result = {'rock':'scissors','paper':'rock','scissors':'paper'}

def validate_roll(player):
    roll = input(f'{player}, choose your roll (rock,paper,scissors) ')
    roll = roll.lower().strip()
    while roll not in rolls:
        print(f'{player}, {roll} is not a roll')
        roll = input('Please choose a valid roll (rock, paper, scissors) ').lower().strip()
        print()
    return roll

def check_winner(roll1,roll2):
    if roll1 == roll2:
        return "It's a tie"
    elif result[roll1] == roll2:
        return f'{player1} won the round'
    else:
        return "Computer won the round"

rounds = 3
p1_wins = 0
p2_wins = 0

while p1_wins<rounds and p2_wins<rounds:

    roll1 = validate_roll(player1)
    roll2 = random.choice(rolls)
    print(f'{player1} -> {roll1}')
    print(f'{player2} -> {roll2}')
    print()
    phrase = check_winner(roll1, roll2)
    print(phrase)
    if player1 in phrase:
        p1_wins+=1
    elif player2 in phrase:
        p2_wins+=1
    print()
    print(f"Score is {player1} {p1_wins} X Computer {p2_wins}")
    print()


print(f'{player1 if p1_wins>p2_wins else player2} won the game by a score of {p1_wins if p1_wins==rounds else p2_wins} x {p1_wins if p1_wins!=rounds else p2_wins}')
    



