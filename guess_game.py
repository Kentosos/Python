secret = 'Horse'
guess = ''
guess_count = 0
guess_limit = 5
out_guesses = False
print('Try to guess an animal!')

while guess != secret:

    if guess_count <= guess_limit:
        guess = input('Enter an animal: ')
        guess_count += 1
    else:
        out_guesses = True

if out_guesses:
    print('You LOOOOSE')
else:
    print('You won from this try:', guess_count)
