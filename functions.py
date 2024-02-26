import random
def start_game():
    game_level = int(input('*****Game Menu***** \n'
                        '1. Beginner(1-10) \n'
                        '2. Intermediate(1-100) \n'
                        '3. Hard(1-1000) \n'
                        '4. Exit App \n\n'
                        'Provide menu: '))
    return game_level




def user_option(level):
    option_level = 0
    if level == 1:
        option_level = 10
    elif level == 2:
        option_level = 100
    elif level == 3:
        option_level = 1000
    elif level == 4:
        exit
    else:
        print('level not defined')
    generate = generate_random_number(option_level)
    proceed_game(generate,option_level)
      
def generate_random_number(end_point):
    return random.randint(1, end_point)

def proceed_game(correct_guess, level):
    for i in range(5):
        user_input = int(input(f'Enter your guess(1-{level}): '))
        if user_input == correct_guess:
            print('Your guess is correct')
            break
        else:
            print('Guess is wrong')
        if user_input > correct_guess:
            print('Your are out of range')
        elif user_input < correct_guess:
            print('Your guess is too low, try again!!')
        else:
            print('Your guess is too high, try again!!')
            
    print('Program ended, Thanks for guessing') 
option = start_game()
user_option(option)


    