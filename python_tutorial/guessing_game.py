# word_list = ['giraffe', 'elefant', 'dog', 'cat']
secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter a guess: ').lower()
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('\nOut of Guesses, YOU LOSE!')
else:
    print('\nYou win!')
