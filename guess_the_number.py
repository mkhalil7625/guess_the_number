import random

correct = 'you guessed correctly!'
too_low = 'Too Low!'
too_high = 'too high!'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:

        try:
            userInput = int(input('Guess the secret number? '))
            if userInput in range(1, 11):
                return userInput
            else:
                print('Please enter an integer between 1 and 10')
        except:
            print("Please enter an integer!")



def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high





def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    count = 1
    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break
        count += 1
    print(f'you guessed {count} guesses')

if __name__ == '__main__':
    main()
