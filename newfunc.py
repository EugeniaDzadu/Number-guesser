import random
def begin_game():
    game_level = int(input('*****Game Menu***** \n'
                        '1. Beginner(1-10) \n'
                        '2. Intermediate(1-100) \n'
                        '3. Hard(1-1000) \n'
                        '4. Exit App \n\n'
                        'Provide menu: '))
    return game_level


def level_options(level):
    guess_number = 0
    if level == 1:
        guess_number == 10
    elif level == 2:
        guess_number == 100
    elif level == 3:
        guess_number == 1000
    elif level == 4:
        exit
    else:
        print('undefined level')
        
        generate = get_random_number(guess_number)
        procedure(generate, guess_number)
        
def get_random_number(end_point):
    return random.randint(1, end_point)

def procedure(right_guess, level):
    i=0
    chances = 0
    while i<5:
        user_input = int(input(f'Enter the your guessed number(1-{level}): '))
        chances += 1
        if user_input == right_guess:
            print('Your guess is correct!!')
            break
        else:
            print('Guess is wrong')
        if user_input > right_guess:
            print('You are out of range!!')
        else:
            print('Your guess is too high, try again!!')
    i=i+1
            
options = begin_game()
level_options(options)
